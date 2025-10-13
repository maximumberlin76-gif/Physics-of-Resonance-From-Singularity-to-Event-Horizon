#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# RPU · Minimal Resonant Core (v0.5, balanced ternary control)
# License: Apache-2.0 (see /LICENSE_CODE)
import numpy as np
import argparse
TAU = 2*np.pi
def power_iteration_radius(A, iters=128, rng=None):
    rng = np.random.default_rng(None if rng is None else rng)
    x = rng.normal(size=A.shape[0]); x /= np.linalg.norm(x) + 1e-12; r = 0.0
    for _ in range(iters):
        x = A @ x; n = np.linalg.norm(x) + 1e-12; x /= n; r = n
    return float(r)
def quantize_balanced(x, t0=0.0, t1=0.33):
    q = np.zeros_like(x, dtype=np.int8); q[x >=  t1] =  1; q[x <= -t1] = -1; return q
def quantize_W(W, thresh=0.2):
    S = np.zeros_like(W, dtype=np.int8); S[W >=  thresh] =  1; S[W <= -thresh] = -1; return S
class RPUCore:
    def __init__(self, N, seed=42, k_global=0.6, dt=5e-3, sigma=0.02,
                 sparsify=0.0, threshold=None, norm_iters=128, gamma=np.pi*0.3,
                 anti_R=0.90, anti_duration=200, anti_amp_scale=0.7, anti_sigma_boost=0.01,
                 mod_amp_freq=0.1, mod_amp_depth=0.1, mod_freq_depth=0.02,
                 ternary=True, wq_thresh=0.25, state_tau=0.33):
        self.rng = np.random.default_rng(seed)
        self.N, self.dt, self.kg = N, dt, k_global
        self.sigma_base = float(sigma); self.gamma = float(gamma)
        self.omega = self.rng.normal(TAU*1.0, TAU*0.10, N)
        self.theta = self.rng.uniform(0, TAU, N)
        W = self.rng.normal(0.0, 1.0, (N, N)); W = (W + W.T)/2.0
        np.fill_diagonal(W, 0.0); W /= (np.max(np.abs(W)) + 1e-12)
        if threshold is not None:
            mask = np.abs(W) >= float(threshold); W = W * mask
        elif sparsify > 0.0:
            q = np.quantile(np.abs(W), sparsify); W = W * (np.abs(W) >= q)
        rho = power_iteration_radius(W, iters=norm_iters, rng=seed)
        if rho > 1.0: W = W / (rho + 1e-12)
        self.W = W
        self.ext_freq  = np.zeros(N); self.ext_amp   = np.zeros(N); self.ext_phase = np.zeros(N)
        self.mod_amp_freq, self.mod_amp_depth, self.mod_freq_depth = float(mod_amp_freq), float(mod_amp_depth), float(mod_freq_depth)
        self.anti_R, self.anti_duration = float(anti_R), int(anti_duration)
        self.anti_amp_scale, self.anti_sigma_boost = float(anti_amp_scale), float(anti_sigma_boost)
        self._antilock_timer = 0; self._amp_scale_dyn  = 1.0
        self.use_ternary = bool(ternary); self.state_tau = float(state_tau)
        self.Wq = quantize_W(self.W, thresh=float(wq_thresh))
        self.s  = quantize_balanced(np.cos(self.theta), t1=self.state_tau)
        self.t = 0.0
    def mix(self, a, b, alpha=0.5):
        a = np.asarray(a, float); b = np.asarray(b, float); return (1-alpha)*a + alpha*b
    def lock(self, freq_profile=None, amp_profile=None, reset_phase=False):
        if freq_profile is not None:
            fp = np.asarray(freq_profile, float); 
            if fp.size != self.N: raise ValueError("freq_profile size mismatch"); self.ext_freq = fp
        if amp_profile is not None:
            ap = np.asarray(amp_profile, float); 
            if ap.size != self.N: raise ValueError("amp_profile size mismatch"); self.ext_amp = ap
        if reset_phase: self.ext_phase = np.zeros(self.N)
    def reset_phases(self, theta=None):
        self.theta = self.rng.uniform(0, TAU, self.N) if theta is None else np.asarray(theta, float) % TAU
    def _order_param(self, theta=None):
        th = self.theta if theta is None else theta
        z = np.exp(1j*th); zm = np.mean(z); return float(np.abs(zm)), float(np.angle(zm))
    def measure(self, kind="order"):
        if kind == "order": R, phi = self._order_param(); return {"R": R, "phi": phi}
        if kind == "clusters": sign = np.sign(np.cos(self.theta)); return {"labels": sign.astype(int).tolist()}
        if kind == "phases": return {"theta": self.theta.copy()}
        if kind == "ternary": return {"s": self.s.copy(), "Wq_nnz": int(np.count_nonzero(self.Wq))}
        raise ValueError("unknown metric")
    def imprint(self, pattern, gain=0.25):
        v = np.asarray(pattern, float); v = (v - v.mean()) / (v.std()+1e-12)
        H = np.outer(v, v); np.fill_diagonal(H, 0.0)
        H /= (np.max(np.abs(H)) + 1e-12)
        self.W = np.tanh(self.W + gain*H); self.Wq = quantize_W(self.W, thresh=0.25)
    def _dtheta(self, theta, ext_phase, amp_now, freq_now):
        phase_diff = theta[:, None] - theta[None, :]
        coup = np.sum(self.W * np.sin(-phase_diff - self.gamma), axis=1)
        pll  = amp_now * np.sin(ext_phase - theta)
        return self.omega + self.kg*coup + pll
    def _ternary_controller(self):
        u_raw = self.Wq @ self.s; deg = np.maximum(np.sum(np.abs(self.Wq), axis=1), 1)
        x = u_raw / deg; u = quantize_balanced(x, t1=0.2).astype(float)
        phi_bump = 0.15 * u; return phi_bump
    def step(self, steps=1, stability_guard=True):
        for _ in range(steps):
            if self._antilock_timer > 0:
                amp_scale = self.anti_amp_scale; sigma = self.sigma_base + self.anti_sigma_boost; self._antilock_timer -= 1
            else:
                amp_scale = 1.0; sigma = self.sigma_base
            t = self.t
            amp_mod = 1.0 + self.mod_amp_depth*np.sin(TAU*self.mod_amp_freq*t)
            amp_now = self.ext_amp * amp_scale * amp_mod
            freq_now = self.ext_freq * (1.0 + self.mod_freq_depth*np.sin(TAU*self.mod_amp_freq*0.5*t))
            phi_bump = self._ternary_controller() if self.use_ternary else 0.0
            if stability_guard:
                fac = (self.kg + float(np.max(np.abs(amp_now)))) * self.dt
                if fac > 0.1: self.dt = 0.1 / max(self.kg + float(np.max(np.abs(amp_now))), 1e-12)
            self.ext_phase = (self.ext_phase + self.dt*freq_now + phi_bump) % TAU
            k1 = self._dtheta(self.theta, self.ext_phase, amp_now, freq_now)
            theta_p = (self.theta + self.dt*k1) % TAU
            k2 = self._dtheta(theta_p, self.ext_phase, amp_now, freq_now)
            dtheta = 0.5*(k1 + k2)
            dtheta += sigma * self.rng.normal(0.0, 1.0, self.N)
            self.theta = (self.theta + self.dt*dtheta) % TAU
            self.t += self.dt
            if self.use_ternary: self.s = quantize_balanced(np.cos(self.theta), t1=self.state_tau)
            R, _ = self._order_param()
            if R > self.anti_R and self._antilock_timer == 0: self._antilock_timer = self.anti_duration
def run_once(args):
    N = args.N
    rpu = RPUCore(
        N, seed=args.seed, k_global=args.k, dt=args.dt, sigma=args.sigma,
        sparsify=args.sparsify, threshold=args.threshold, norm_iters=args.norm_iters,
        gamma=args.gamma, anti_R=args.anti_R, anti_duration=args.anti_duration,
        anti_amp_scale=args.anti_amp_scale, anti_sigma_boost=args.anti_sigma_boost,
        mod_amp_freq=args.mod_amp_freq, mod_amp_depth=args.mod_amp_depth,
        mod_freq_depth=args.mod_freq_depth, ternary=not args.no_ternary,
        wq_thresh=args.wq_thresh, state_tau=args.state_tau
    )
    x = np.linspace(0, TAU, N, endpoint=False)
    profile_A = 1.0 + 0.2*np.sin(3*x); profile_B = 1.0 + 0.2*np.sin(7*x + np.pi/4)
    rpu.imprint(np.sin(3*x), gain=0.25); rpu.imprint(np.sin(7*x + np.pi/4), gain=0.25)
    mix_ab = rpu.mix(profile_A, profile_B, alpha=args.alpha)
    rpu.lock(freq_profile=TAU*mix_ab, amp_profile=args.amp*np.ones(N), reset_phase=True)
    log_R, log_phi = [], []
    for t in range(1, args.steps+1):
        rpu.step(1, stability_guard=not args.no_guard)
        if t % args.log_every == 0 or t == args.steps:
            m = rpu.measure("order"); log_R.append(m["R"]); log_phi.append(m["phi"])
    m = rpu.measure("order"); cls = rpu.measure("clusters"); mt = rpu.measure("ternary")
    uniq = np.unique(cls["labels"]).tolist()
    print(f"[run] R={m['R']:.3f}, meanφ={m['phi']:.3f} rad; clusters={uniq} (sample {cls['labels'][:24]})")
    print(f"[ternary] nnz(Wq)={mt['Wq_nnz']}, s-sample={mt['s'][:24].tolist()}")
    print(f"[diag] R(t) samples={len(log_R)} → {np.array2string(np.array(log_R), precision=3, separator=', ')}")
    print(f"[diag] φ(t) samples={len(log_phi)} → {np.array2string(np.array(log_phi), precision=3, separator=', ')}")
def run_scan(args):
    N = args.N
    rpu = RPUCore(
        N, seed=args.seed, k_global=args.k, dt=args.dt, sigma=args.sigma,
        sparsify=args.sparsify, threshold=args.threshold, norm_iters=args.norm_iters,
        gamma=args.gamma, anti_R=args.anti_R, anti_duration=args.anti_duration,
        anti_amp_scale=args.anti_amp_scale, anti_sigma_boost=args.anti_sigma_boost,
        mod_amp_freq=args.mod_amp_freq, mod_amp_depth=args.mod_amp_depth,
        mod_freq_depth=args.mod_freq_depth, ternary=not args.no_ternary,
        wq_thresh=args.wq_thresh, state_tau=args.state_tau
    )
    x = np.linspace(0, TAU, N, endpoint=False)
    profile_A = 1.0 + 0.2*np.sin(3*x); profile_B = 1.0 + 0.2*np.sin(7*x + np.pi/4)
    rpu.imprint(np.sin(3*x), gain=0.25); rpu.imprint(np.sin(7*x + np.pi/4), gain=0.25)
    alphas = np.linspace(0.0, 1.0, args.scan_points); Rvals, Kvals = [], []
    for a in alphas:
        mix_ab = rpu.mix(profile_A, profile_B, alpha=a)
        rpu.lock(freq_profile=TAU*mix_ab, amp_profile=args.amp*np.ones(N), reset_phase=True)
        rpu.reset_phases()
        for _ in range(args.scan_steps): rpu.step(1, stability_guard=not args.no_guard)
        m = rpu.measure("order"); cls = rpu.measure("clusters")
        Rvals.append(m["R"]); Kvals.append(len(set(cls["labels"])))
        print(f"[scan] α={a:.3f} → R={m['R']:.3f}, clusters={Kvals[-1]}")
    Rvals = np.array(Rvals); Kvals = np.array(Kvals)
    dR = np.diff(Rvals); jumps = np.where(np.abs(dR) > args.jump_thresh)[0]
    kswitch = np.where(np.diff(Kvals) != 0)[0]
    idx = sorted(set(jumps.tolist() + kswitch.tolist()))
    print(f"[scan] candidate bifurcations at α≈ {[round(float(alphas[i]),3) for i in idx]}")
    print(f"[scan] R(α) = {np.array2string(Rvals, precision=3, separator=', ')}")
    print(f"[scan] K(α) = {Kvals.tolist()}")
def parse_args():
    ap = argparse.ArgumentParser(description="RPU · Minimal Resonant Core v0.5 (balanced ternary)")
    ap.add_argument("--N", type=int, default=256); ap.add_argument("--k", type=float, default=0.6)
    ap.add_argument("--dt", type=float, default=5e-3); ap.add_argument("--steps", type=int, default=3000)
    ap.add_argument("--alpha", type=float, default=0.35); ap.add_argument("--amp", type=float, default=0.28)
    ap.add_argument("--sigma", type=float, default=0.03); ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--log-every", type=int, default=50)
    ap.add_argument("--sparsify", type=float, default=0.8); ap.add_argument("--threshold", type=float, default=None)
    ap.add_argument("--norm-iters", type=int, default=96); ap.add_argument("--no-guard", action="store_true")
    ap.add_argument("--gamma", type=float, default=np.pi*0.3)
    ap.add_argument("--anti-R", type=float, default=0.90); ap.add_argument("--anti-duration", type=int, default=200)
    ap.add_argument("--anti-amp-scale", type=float, default=0.7); ap.add_argument("--anti-sigma-boost", type=float, default=0.01)
    ap.add_argument("--mod-amp-freq", type=float, default=0.1); ap.add_argument("--mod-amp-depth", type=float, default=0.1)
    ap.add_argument("--mod-freq-depth", type=float, default=0.02)
    ap.add_argument("--no-ternary", action="store_true"); ap.add_argument("--wq-thresh", type=float, default=0.25)
    ap.add_argument("--state-tau", type=float, default=0.33)
    ap.add_argument("--scan", action="store_true"); ap.add_argument("--scan-points", type=int, default=21)
    ap.add_argument("--scan-steps", type=int, default=1000); ap.add_argument("--jump-thresh", type=float, default=0.05)
    return ap.parse_args()
if __name__ == "__main__":
    args = parse_args()
    if args.scan: run_scan(args)
    else: run_once(args)
