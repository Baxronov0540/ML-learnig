"""Xuddi shu amallar NumPy bilan va MiniArray bilan solishtirish."""
import numpy as np

a = np.arange(12, dtype=np.int32).reshape(3, 4)
t = a.T                                  # view: strides almashdi
s = a[0:3:2]                             # view: qator qadami 2 baravar
print("a.T strides     :", t.strides)
print("a[0:3:2] strides:", s.strides)

t[1, 2] = 99
print("a[2,1] endi:", a[2, 1])
print("t.base is a:", t.base is a)                 # False! base = egasi, bevosita ota emas
print("a.flags.owndata:", a.flags.owndata, "| t.base is a.base:", t.base is a.base)
print("shares_memory(a, t):", np.shares_memory(a, t))  # ishonchli tekshiruv

# MiniArray'dagi formulani NumPy'ning o'ziga qo'llaymiz: xom baytlardan o'qish
raw = a.tobytes()                        # tobytes() C-tartibdagi NUSXA baytlarni beradi
off = 2 * a.strides[0] + 1 * a.strides[1]
print("xom baytlardan a[2,1]:", np.frombuffer(raw, dtype=np.int32, count=1, offset=off)[0])

# as_strided: strides'ni qo'lda berib, transpozitsiyani "o'zimiz" yasaymiz
from numpy.lib.stride_tricks import as_strided
mening_T = as_strided(a, shape=(4, 3), strides=(4, 16), writeable=False)
print("as_strided == a.T:", np.array_equal(mening_T, a.T))
