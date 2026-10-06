"""3-dars topshirig'i: view va copy (A) + 1 mln son ustida tezlik (B)."""
import timeit

import numpy as np


def holat(nom, asl, yangi):
    """VIEW yoki COPY ekanini chiqaradi."""
    # TODO 1: np.shares_memory bilan tekshiring va "VIEW"/"COPY" chiqaring
    tur = "TODO"
    print(f"{nom:33} -> {tur}")
    return tur


# ---------------- A qism: 5 ta misol ----------------
a = np.arange(10)
# TODO 2: oddiy slicing a[2:5] -> holat(...), keyin view'ga yozib a ni chiqaring
# TODO 3: fancy indexing a[[2, 3, 4]] -> holat(...), nusxaga yozing, a o'zgarmasin
# TODO 4: boolean mask a[a % 2 == 0]: o'qish COPY, lekin a[mask] = 0 a ni o'zgartiradi
# TODO 5: reshape: a.reshape(2, 3) VIEW, a.reshape(2, 3).T.reshape(6) COPY
# TODO 6: ravel() va flatten() farqi

# ---------------- B qism: 1 mln son ----------------
rng = np.random.default_rng(42)
arr = rng.random(1_000_000)
lst = arr.tolist()


def ms(fn):
    # TODO 7: timeit.repeat(fn, number=3, repeat=5) dan eng kichigini olib, ms ga aylantiring
    return float("nan")


# TODO 8: yig'indi, x*2 + 1, filtr x > 0.5 uchun list va NumPy vaqtini va farqni chiqaring
# TODO 9 (bonus): arr[::2] va arr[::2].copy() vaqtini solishtiring
print("shablon ishladi: TODO'larni to'ldiring")
