"""Muammo: 1 mln tranzaksiya komissiyasini list va NumPy bilan hisoblash."""
import time

import numpy as np

rng = np.random.default_rng(42)                               # seed: natija har safar bir xil
summa_np = rng.uniform(1_000, 5_000_000, size=1_000_000)      # 1 mln summa (so'm), float64
summa_list = summa_np.tolist()                                # aynan shu sonlar, oddiy list


def eng_tez(fn, takror=5):
    """fn'ni bir necha marta ishlatib, eng kichik vaqtni (ms) qaytaradi."""
    vaqtlar = []
    for _ in range(takror):
        t0 = time.perf_counter()
        fn()
        vaqtlar.append(time.perf_counter() - t0)
    return min(vaqtlar) * 1000                                # min: fon shovqini eng kam bo'lgan urinish


t_list = eng_tez(lambda: [x * 0.01 + 500 for x in summa_list])   # 1% + 500 so'm, Python sikli
t_np = eng_tez(lambda: summa_np * 0.01 + 500)                    # bitta vektor ifoda, sikl C ichida

print(f"list : {t_list:6.1f} ms")
print(f"NumPy: {t_np:6.1f} ms")
print(f"farq : ~{t_list / t_np:.0f} marta")
kom_list = [x * 0.01 + 500 for x in summa_list]
kom_np = summa_np * 0.01 + 500
print("natija bir xilmi:", np.allclose(kom_list, kom_np))
