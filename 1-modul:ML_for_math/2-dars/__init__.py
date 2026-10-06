"""Muammo: CSV'ni "qo'lda" o'qish. Uchta yashirin xato va xotira narxi."""
import tracemalloc

tracemalloc.start()
with open("tranzaksiyalar.csv", encoding="utf-8") as f:
    qatorlar = f.readlines()                      # butun fayl birdan xotiraga
_, cho_qqi = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"readlines: {len(qatorlar):,} qator, xotira cho'qqisi {cho_qqi / 1e6:.1f} MB")

sarlavha = qatorlar[0].strip().split(",")
yozuvlar = [q.strip().split(",") for q in qatorlar[1:]]
buzuq = [y for y in yozuvlar if len(y) != len(sarlavha)]
print(f"ustunlar soni noto'g'ri: {len(buzuq):,} qator")   # 1-xato: izohdagi vergul
print("misol:", buzuq[0])

summalar = []
for y in yozuvlar:
    try:
        summalar.append(float(y[5]))
    except ValueError:                             # 2-xato: "" va "n/a" jim tashlanadi
        pass
print(f"o'qilgan summa: {len(summalar):,}")

matnlar = [y[5] for y in yozuvlar if y[5] not in ("", "n/a")]
print("TOP-3 (str):  ", sorted(matnlar, reverse=True)[:3])   # 3-xato: matn sifatida
print("TOP-3 (float):", sorted(summalar, reverse=True)[:3])