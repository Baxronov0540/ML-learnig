"""Ko'p uchraydigan xatolar: noto'g'ri va to'g'ri variantlar."""
import numpy as np

# --- 1. Slice view'ni o'zgartirib, asl ma'lumotni buzish
X = np.array([[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]])
ustun = X[:, 1]                    # NOTO'G'RI: bu view
ustun /= 100                       # "faqat nusxani normallashtiraman" deb o'ylaymiz
print("1 noto'g'ri, X[:,1] =", X[:, 1])        # asl X buzildi
X = np.array([[1.0, 200.0], [2.0, 300.0], [3.0, 400.0]])
ustun = X[:, 1].copy()             # TO'G'RI: aniq nusxa
ustun /= 100
print("1 to'g'ri,   X[:,1] =", X[:, 1])

# --- 2. Zanjirli indekslash bilan yozish (fancy/mask nusxasiga yoziladi)
a = np.array([5, -3, 8, -1])
a[a < 0][0] = 0                    # NOTO'G'RI: a[a<0] nusxa, 0 nusxaga yozildi
print("2 noto'g'ri:", a)
idx = np.flatnonzero(a < 0)        # TO'G'RI: indekslarni olib, bitta [] bilan yozish
a[idx[0]] = 0
print("2 to'g'ri:  ", a)

# --- 3. Jim overflow: kichik butun tur ustida arifmetika
kliklar = np.array([30_000, 5_000], dtype=np.int16)
print("3 noto'g'ri:", kliklar * 2)                   # 60000 int16 ga sig'maydi -> manfiy
print("3 to'g'ri:  ", kliklar.astype(np.int64) * 2)  # avval kengaytiramiz
print("   int16 max =", np.iinfo(np.int16).max, "| sum() dtype:", kliklar.sum().dtype)

# --- 4. Pul summalarini float32 da saqlash
balans = np.array([99_999_999.99], dtype=np.float32)
print("4 noto'g'ri:", f"{balans[0]:.2f}")
balans_tiyin = np.array([9_999_999_999], dtype=np.int64)    # TO'G'RI: tiyinda int64
print("4 to'g'ri:  ", balans_tiyin[0] // 100, "so'm", balans_tiyin[0] % 100, "tiyin")

# --- 5. Kichik view katta massivni xotirada ushlab qoladi
katta = np.zeros(10_000_000)                  # 80 MB
bosh = katta[:5]                               # NOTO'G'RI: 40 bayt kerak, lekin...
print("5 noto'g'ri: bosh.base.nbytes =", f"{bosh.base.nbytes:,}")   # 80 MB tirik qoladi
bosh = katta[:5].copy()                         # TO'G'RI: copy, keyin `del katta`
print("5 to'g'ri:   bosh.base =", bosh.base, "| bosh.nbytes =", bosh.nbytes)

# --- 6. In-place amal va dtype
narx = np.array([100, 250, 990])               # int64
try:
    narx *= 1.12                                 # NOTO'G'RI: float natijani int ga yozib bo'lmaydi
except TypeError as e:                           # UFuncTypeError TypeError'dan meros oladi
    print("6 noto'g'ri:", type(e).__name__)
narx = narx * 1.12                               # TO'G'RI: yangi float64 massiv
print("6 to'g'ri:  ", narx, narx.dtype)
