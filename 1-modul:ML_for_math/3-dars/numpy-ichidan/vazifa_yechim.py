"""Amaliy topshiriq yechimi: view va copy farqini ko'rsatuvchi 5 ta misol."""
import numpy as np


def holat(nom, asl, yangi):
    """Yangi massiv asl bilan xotirani bo'lishadimi: VIEW yoki COPY."""
    tur = "VIEW" if np.shares_memory(asl, yangi) else "COPY"
    print(f"{nom:33} -> {tur}")
    return tur


# 1-misol: oddiy slicing (start:stop:step) -> VIEW
a = np.arange(10)
s = a[2:5]
holat("1) a[2:5]", a, s)
s[0] = -1                                # view orqali yozish...
print("   a =", a)                       # ...asl a ham o'zgardi

# 2-misol: fancy indexing (indekslar ro'yxati) -> COPY
a = np.arange(10)
f = a[[2, 3, 4]]
holat("2) a[[2, 3, 4]]", a, f)
f[0] = -1
print("   a =", a)                       # a o'zgarmadi

# 3-misol: boolean mask -> COPY, lekin mask bilan YOZISH asl massivga tushadi
a = np.arange(10)
m = a[a % 2 == 0]
holat("3) a[a % 2 == 0]", a, m)
m[:] = 0                                  # nusxani o'zgartirdik, a o'zgarmaydi
a[a % 2 == 0] = 0                         # __setitem__: to'g'ridan-to'g'ri a ga yozadi
print("   a =", a)

# 4-misol: reshape -> uzluksiz massivda VIEW, transpozitsiyadan keyin COPY
a = np.arange(6)
holat("4a) a.reshape(2, 3)", a, a.reshape(2, 3))
b = a.reshape(2, 3).T                     # (3, 2), F-tartib, C emas
holat("4b) a.reshape(2, 3).T.reshape(6)", a, b.reshape(6))

# 5-misol: ravel() imkon bo'lsa VIEW, flatten() har doim COPY
a = np.arange(6).reshape(2, 3)
holat("5a) a.ravel()", a, a.ravel())
holat("5b) a.flatten()", a, a.flatten())

# ---------------- B qism: 1 mln son, list va NumPy ----------------
import timeit

rng = np.random.default_rng(42)
arr = rng.random(1_000_000)
lst = arr.tolist()


def ms(fn):
    return min(timeit.repeat(fn, number=3, repeat=5)) / 3 * 1000


for nom, f_list, f_np in [
    ("yig'indi", lambda: sum(lst), lambda: arr.sum()),
    ("x*2 + 1", lambda: [x * 2 + 1 for x in lst], lambda: arr * 2 + 1),
    ("filtr x > 0.5", lambda: [x for x in lst if x > 0.5], lambda: arr[arr > 0.5]),
]:
    tl, tn = ms(f_list), ms(f_np)
    print(f"{nom:14} list {tl:7.2f} ms | NumPy {tn:6.2f} ms | {tl / tn:4.0f}x")

# Bonus: view yaratish O(1), copy O(n)
print(f"arr[::2]        (view): {ms(lambda: arr[::2]) * 1000:8.2f} mks")
print(f"arr[::2].copy() (copy): {ms(lambda: arr[::2].copy()) * 1000:8.2f} mks")
