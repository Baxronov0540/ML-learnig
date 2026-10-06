import numpy as np
import time
# l = np.array([1,2,3,4,5,6,7,8,9])

# print(l.shape)

rng = np.random.default_rng(42)
summa_np = rng.uniform(1_000,5_000_000,size = 1000000)

summa_list= summa_np.tolist()


def eng_tez(fn,takror=5):
    
    vaqtlar = []
    for _ in range(takror):
        t0=time.perf_counter()
        
        fn()
        vaqtlar.append(time.perf_counter()-t0)
        
    return min(vaqtlar)*1000
t_list = eng_tez(lambda: [x * 0.01 + 500 for x in summa_list])   # 1% + 500 so'm, Python sikli
t_np = eng_tez(lambda: summa_np * 0.01 + 500)                    # bitta vektor ifoda, sikl C ichida

print(f"list : {t_list:6.1f} ms")
print(f"NumPy: {t_np:6.1f} ms")
print(f"farq : ~{t_list / t_np:.0f} marta")
kom_list = [x * 0.01 + 500 for x in summa_list]
kom_np = summa_np * 0.01 + 500
print("natija bir xilmi:", np.allclose(kom_list, kom_np))
