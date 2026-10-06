"""O'rta mashq: ustunni xavfsiz eng kichik butun turga tushirish (downcast)."""
import numpy as np


def downcast_int(x: np.ndarray) -> np.ndarray:
    """Qiymatlar sig'adigan eng kichik butun dtype'ga o'tkazadi."""
    if not np.issubdtype(x.dtype, np.integer):
        raise TypeError(f"butun son kutilgan, keldi: {x.dtype}")
    lo, hi = x.min(), x.max()
    turlar = [np.uint8, np.uint16, np.uint32, np.uint64] if lo >= 0 else \
             [np.int8, np.int16, np.int32, np.int64]
    for t in turlar:
        info = np.iinfo(t)
        if info.min <= lo and hi <= info.max:
            return x.astype(t)                 # copy: yangi, kichikroq massiv
    return x


rng = np.random.default_rng(42)
yosh = rng.integers(18, 90, size=1_000_000)           # mijoz yoshi
filial = rng.integers(0, 1_200, size=1_000_000)       # filial ID
balans = rng.integers(-5_000_000, 50_000_000_000, size=1_000_000)  # tiyin

jami_old = jami_yangi = 0
for nom, x in [("yosh", yosh), ("filial", filial), ("balans", balans)]:
    y = downcast_int(x)
    assert np.array_equal(x, y)                # qiymat yo'qolmaganini tekshiramiz
    jami_old += x.nbytes; jami_yangi += y.nbytes
    print(f"{nom:7} {str(x.dtype):6} -> {str(y.dtype):7} {x.nbytes:>10,} -> {y.nbytes:>10,} bayt")
print(f"jami: {jami_old / 1e6:.1f} MB -> {jami_yangi / 1e6:.1f} MB")
