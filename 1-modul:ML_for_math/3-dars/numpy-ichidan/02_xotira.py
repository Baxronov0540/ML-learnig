"""List va ndarray xotirada qancha joy oladi."""
import sys
import tracemalloc

import numpy as np

N = 1_000_000

tracemalloc.start()                                   # Python ajratgan baytlarni sanashni boshlaymiz
lst = [float(i) for i in range(N)]                    # 1 mln alohida float obyekti + ko'rsatkichlar
list_bytes, _ = tracemalloc.get_traced_memory()       # (hozirgi, eng yuqori) juftligi
tracemalloc.stop()

arr = np.arange(N, dtype=np.float64)                  # bitta uzluksiz 8 MB blok

print("sys.getsizeof(lst)   :", f"{sys.getsizeof(lst):>11,}")   # faqat ko'rsatkichlar massivi
print("sys.getsizeof(1.5)   :", f"{sys.getsizeof(1.5):>11,}")   # bitta float obyekti
print("list jami (tracemalloc):", f"{list_bytes:>9,}")
print("arr.nbytes           :", f"{arr.nbytes:>11,}")           # faqat ma'lumot baytlari
print("sys.getsizeof(arr)   :", f"{sys.getsizeof(arr):>11,}")   # + ndarray sarlavhasi
print(f"nisbat               : {list_bytes / arr.nbytes:.1f} marta")
