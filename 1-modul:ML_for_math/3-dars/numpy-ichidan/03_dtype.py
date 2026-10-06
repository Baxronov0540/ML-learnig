"""dtype: har bir element necha bayt va qanday talqin qilinadi."""
import numpy as np

a = np.array([1, 2, 3])                       # Python int'lardan -> standart int64 (Linux)
b = np.array([1.0, 2, 3])                     # bitta float bo'lsa -> hammasi float64
c = np.array([1, 2, 3], dtype=np.int8)        # dtype'ni o'zimiz tanlaymiz
for nom, x in [("a", a), ("b", b), ("c", c)]:
    print(nom, x.dtype, "itemsize =", x.itemsize, "nbytes =", x.nbytes)

# Chegaralar: har bir tur qaysi oraliqni sig'diradi
print("int8 oralig'i:", np.iinfo(np.int8).min, "..", np.iinfo(np.int8).max)
print("int32 max:", np.iinfo(np.int32).max)
print("float32 aniq raqamlar:", np.finfo(np.float32).precision,
      "| float64:", np.finfo(np.float64).precision)

# 1) Butun son to'lib ketishi (overflow): xato chiqmaydi, aylanib ketadi
yosh = np.array([120, 125], dtype=np.int8)
print("int8 + 10:", yosh + 10)                # [-126 -121]  jim xato!

# 2) float32 aniqligi: 2**24 dan keyin butun sonlar "sakraydi"
print("float32(16_777_217) =", np.float32(16_777_217))
summa = np.array([123_456_789.37], dtype=np.float32)
print("float32 summa:", f"{summa[0]:.2f}")    # tiyinlar yo'qoldi

# 3) astype har doim YANGI massiv qaytaradi (copy)
f = a.astype(np.float32)
print("astype:", f, f.dtype, "| bir xotira?", np.shares_memory(a, f))

# 4) Aralash turlar: list ichida str bo'lsa, butun massiv str bo'ladi
m = np.array([1, "2", 3])
print("aralash:", m, m.dtype)                 # <U21: unicode satr, son emas

# 5) object dtype: NumPy faqat ko'rsatkich saqlaydi -> list tezligi
o = np.array([1, "2", 3.0], dtype=object)
print("object:", o.dtype, "itemsize =", o.itemsize)
