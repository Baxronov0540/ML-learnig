"""Oson mashq: har bir ifoda VIEW yoki COPY? Avval taxmin qiling, keyin tekshiring."""
import numpy as np

a = np.arange(24).reshape(4, 6)
ifodalar = {
    "a[1]": a[1],
    "a[:, 0]": a[:, 0],
    "a[[0, 1]]": a[[0, 1]],
    "a[a > 10]": a[a > 10],
    "a.T": a.T,
    "a[::-1]": a[::-1],
    "a.astype(np.int64)": a.astype(np.int64),
    "a.view(np.uint64)": a.view(np.uint64),
    "a.reshape(6, 4)": a.reshape(6, 4),
    "a[:, ::2].reshape(-1)": a[:, ::2].reshape(-1),
}
for nom, v in ifodalar.items():
    print(f"{nom:24} {'VIEW' if np.shares_memory(a, v) else 'COPY':5} strides={v.strides}")
