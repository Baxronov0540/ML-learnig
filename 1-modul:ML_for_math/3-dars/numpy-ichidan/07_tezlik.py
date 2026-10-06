"""1 mln son: list va NumPy tezlik solishtiruvi (timeit bilan) + grafik."""
import timeit

import matplotlib
matplotlib.use("Agg")                    # oynasiz backend: faylga chizadi (server/CI uchun)
import matplotlib.pyplot as plt
import numpy as np

N = 1_000_000
rng = np.random.default_rng(42)
arr = rng.random(N)                      # [0, 1) oraliqdagi 1 mln float64
lst = arr.tolist()

testlar = {
    "yig'indi":       (lambda: sum(lst),                     lambda: arr.sum()),
    "x*2 + 1":        (lambda: [x * 2 + 1 for x in lst],     lambda: arr * 2 + 1),
    "filtr x > 0.5":  (lambda: [x for x in lst if x > 0.5],  lambda: arr[arr > 0.5]),
    "skalyar ko'p.":  (lambda: sum(x * y for x, y in zip(lst, lst)), lambda: arr @ arr),
    "saralash":       (lambda: sorted(lst),                  lambda: np.sort(arr)),
}


def ms(fn, number=3, repeat=5):
    # timeit.repeat: `repeat` marta, har birida fn `number` marta; min eng ishonchli
    return min(timeit.repeat(fn, number=number, repeat=repeat)) / number * 1000


natija = {}
print(f"{'amal':15} {'list, ms':>9} {'NumPy, ms':>10} {'farq':>7}")
for nom, (f_list, f_np) in testlar.items():
    tl, tn = ms(f_list), ms(f_np)
    natija[nom] = (tl, tn)
    print(f"{nom:15} {tl:9.2f} {tn:10.2f} {tl / tn:6.0f}x")

# Tuzoqlar: konvertatsiya narxi va NumPy massivi ustida Python sikli
print(f"np.array(lst)      : {ms(lambda: np.array(lst)):7.2f} ms  (list -> ndarray narxi)")
print(f"for x in arr: x*2  : {ms(lambda: [x * 2 for x in arr], number=1):7.2f} ms  (list'dan ham sekin!)")

# Grafik: log shkala, chunki farq 10-100 baravar
nomlar = list(natija)
y = np.arange(len(nomlar))
fig, ax = plt.subplots(figsize=(7, 3.6), dpi=110)
ax.barh(y - 0.2, [natija[k][0] for k in nomlar], height=0.38, label="Python list", color="#B42318")
ax.barh(y + 0.2, [natija[k][1] for k in nomlar], height=0.38, label="NumPy", color="#0B7A66")
ax.set_yticks(y, nomlar)
ax.set_xscale("log")
ax.set_xlabel("vaqt, ms (log shkala, kamroq = yaxshi)")
ax.invert_yaxis()
ax.legend(loc="upper right")   # pastki o'ngda saralash ustuni bor
ax.set_title("1 000 000 ta float64: list va NumPy")
fig.tight_layout()
fig.savefig("tezlik.png")
print("saqlandi: tezlik.png")
