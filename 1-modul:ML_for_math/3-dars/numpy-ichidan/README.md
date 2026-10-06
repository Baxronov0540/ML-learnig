# Dars 3: NumPy ichidan — list va ndarray

Nega NumPy oddiy Python list'dan tezroq va kamroq xotira oladi? Bu darsda `ndarray`ning ichki tuzilishini (bayt bufer, `dtype`, `shape`, `strides`) ko'rib chiqamiz va uni noldan soddalashtirilgan holda yozamiz.

*English: Lesson 3 of my ML engineering path. What a NumPy array really is (a byte buffer + dtype + shape + strides), why it is faster and smaller than a Python list, and a tiny `MiniArray` written from scratch.*

## Fayllar

| Fayl | Nimani ko'rsatadi |
|---|---|
| `01_muammo.py` | 1 mln tranzaksiya komissiyasi: list va NumPy vaqti |
| `02_xotira.py` | List va ndarray xotirada qancha joy oladi |
| `03_dtype.py` | `dtype`: har bir element necha bayt va qanday o'qiladi |
| `04_strides.py` | `shape`, `strides`, C va F tartibi |
| `05_noldan.py` | `MiniArray`: ndarray'ning noldan yozilgan modeli |
| `06_numpy_bilan.py` | Xuddi shu amallar NumPy va `MiniArray` bilan |
| `07_tezlik.py` | `timeit` bilan tezlik solishtiruvi + grafik |
| `08_xatolar.py` | Ko'p uchraydigan xatolar: view'ni bilmasdan o'zgartirish va boshqalar |
| `mashq_oson.py` | Mashq: VIEW yoki COPY? |
| `mashq_orta.py` | Mashq: ustunni eng kichik butun turga tushirish |
| `mashq_qiyin.py` | Mashq: nusxasiz 7 kunlik sirpanuvchi o'rtacha |
| `vazifa.py` / `vazifa_yechim.py` | Uy vazifasi va yechimi |

## Ishga tushirish

Repo ildizidan (uv loyiha):

```bash
uv sync
uv run "1-modul:ML_for_math/3-dars/numpy-ichidan/01_muammo.py"
```
