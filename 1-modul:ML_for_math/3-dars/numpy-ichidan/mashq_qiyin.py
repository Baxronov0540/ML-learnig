"""Qiyin mashq: 7 kunlik sirpanuvchi o'rtacha (moving average) nusxasiz."""
import time

import numpy as np
from numpy.lib.stride_tricks import as_strided, sliding_window_view

rng = np.random.default_rng(42)
kunlik = rng.normal(1_000, 150, size=1_000_000)       # kunlik buyurtmalar soni
w = 7


def sikl_bilan(x, w):
    return np.array([x[i:i + w].mean() for i in range(len(x) - w + 1)])


def strided_bilan(x, w):
    n = len(x) - w + 1
    s = x.strides[0]
    oyna = as_strided(x, shape=(n, w), strides=(s, s), writeable=False)  # (n, 7) view, 0 nusxa
    return oyna.mean(axis=1)


oyna = sliding_window_view(kunlik, w)                 # xavfsiz rasmiy variant
print("oyna shape:", oyna.shape, "strides:", oyna.strides,
      "view:", np.shares_memory(kunlik, oyna))

t0 = time.perf_counter(); r1 = sikl_bilan(kunlik[:100_000], w); t1 = time.perf_counter() - t0
t0 = time.perf_counter(); r2 = strided_bilan(kunlik, w); t2 = time.perf_counter() - t0
t0 = time.perf_counter(); r3 = oyna.mean(axis=1); t3 = time.perf_counter() - t0
print(f"sikl (100k)     : {t1 * 1000:7.1f} ms  -> 1 mln uchun ~{t1 * 10 * 1000:.0f} ms")
print(f"as_strided (1 mln): {t2 * 1000:5.1f} ms")
print(f"sliding_window  : {t3 * 1000:7.1f} ms")
print("natijalar teng:", np.allclose(r1, r2[:len(r1)]), np.allclose(r2, r3))
