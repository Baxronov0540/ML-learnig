"""Dars uchun sintetik bank tranzaksiyalari CSV faylini yaratadi (seed=42)."""
import csv
import random
import sys
from datetime import datetime, timedelta

N = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000   # qatorlar soni
random.seed(42)                                           # har safar bir xil fayl

SHAHARLAR = ["Toshkent", "Samarqand", "Buxoro", "Andijon", "Namangan", "Farg'ona", "Nukus"]
VAZN = [40, 12, 8, 11, 10, 12, 7]                         # Toshkent ko'proq
KATEGORIYA = ["oziq-ovqat", "transport", "kommunal", "elektronika", "restoran", "o'tkazma"]
IZOHLAR = ["", "", "", "Chilonzor, 9-kvartal", 'Do\'kon "Makro"', "naqd emas"]

boshi = datetime(2026, 9, 1)
with open("tranzaksiyalar.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)                                     # vergul va qo'shtirnoqni o'zi ekranlaydi
    w.writerow(["tx_id", "vaqt", "mijoz_id", "shahar", "kategoriya", "summa", "izoh"])
    for i in range(1, N + 1):
        vaqt = boshi + timedelta(seconds=random.randrange(30 * 24 * 3600))
        summa = round(random.lognormvariate(11.5, 1.0), -2)   # UZS, ko'p kichik, kam katta                                                                                                                                             
        r = random.random()
        if r < 0.004:
            summa_str = ""                                # bo'sh qiymat
        elif r < 0.005:
            summa_str = "n/a"                             # yaroqsiz qiymat
        else:
            summa_str = f"{summa:.2f}"
        w.writerow([i, vaqt.isoformat(timespec="seconds"), random.randint(1, 5_000),
                    random.choices(SHAHARLAR, VAZN)[0], random.choice(KATEGORIYA),
                    summa_str, random.choice(IZOHLAR                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    )])
print(f"tranzaksiyalar.csv: {N:,} qator yozildi")