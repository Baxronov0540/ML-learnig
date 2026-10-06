"""shape, strides va xotira tartibi (C/F order)."""
import time

import numpy as np

a = np.arange(12, dtype=np.int32).reshape(3, 4)  # 3 qator, 4 ustun, har element 4 bayt
print(a)
print("shape:", a.shape, "strides:", a.strides)  # (16, 4): keyingi qator +16 bayt, keyingi ustun +4

# Element manzili: offset = i*strides[0] + j*strides[1]
i, j = 2, 1
offset = i * a.strides[0] + j * a.strides[1]
print(f"a[{i},{j}] offset = {offset} bayt -> element #{offset // a.itemsize}")
print("tekshiruv:", a[i, j], "==", a.ravel()[offset // a.itemsize])

# Turli ko'rinishlar (view) bir xil baytlarga boshqa "ko'zoynak" bilan qaraydi
for nom, v in [("a.T", a.T), ("a[::2]", a[::2]), ("a[:, ::2]", a[:, ::2]), ("a[:, 1:3]", a[:, 1:3])]:
    print(f"{nom:10} shape={v.shape!s:7} strides={v.strides!s:9} "
          f"C={v.flags['C_CONTIGUOUS']!s:5} F={v.flags['F_CONTIGUOUS']!s:5} "
          f"view={np.shares_memory(a, v)}")

# reshape: uzluksiz massivda view, uzluksiz bo'lmaganda majburan copy
r1 = a.reshape(4, 3)
r2 = a.T.reshape(12)
print("a.reshape(4,3) view?", np.shares_memory(a, r1))
print("a.T.reshape(12) view?", np.shares_memory(a, r2))

# Kesh (cache) effekti: qator bo'yicha o'qish va ustun bo'yicha o'qish
rng = np.random.default_rng(0)
big = rng.random((4000, 4000))                   # 128 MB, C-tartib
def vaqt(fn):
    best = float("inf")
    for _ in range(3):
        t0 = time.perf_counter(); fn(); best = min(best, time.perf_counter() - t0)
    return best * 1000
t_row = vaqt(lambda: [big[k, :].sum() for k in range(4000)])  # qator: baytlar ketma-ket
t_col = vaqt(lambda: [big[:, k].sum() for k in range(4000)])  # ustun: har element 32 000 bayt sakrab
print(f"qatorlar bo'yicha: {t_row:6.1f} ms | ustunlar bo'yicha: {t_col:6.1f} ms "
      f"| ~{t_col / t_row:.1f} marta sekin")
