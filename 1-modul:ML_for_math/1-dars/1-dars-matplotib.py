import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
u = np.array([2.0, 1.0])
v = np.array([1.0, 3.0])
c = -1.5

fig, ax = plt.subplots(figsize=(6, 6))

def arrow(vec, start=(0, 0), color="k", label=None, alpha=1.0):
    # angles="xy", scale_units="xy", scale=1 SHART: aks holda matplotlib
    # strelkani o'zi masshtablaydi va uzunlik noto'g'ri chiqadi
    ax.quiver(*start, *vec, angles="xy", scale_units="xy", scale=1,
              color=color, label=label, alpha=alpha, width=0.012)

arrow(u, color="tab:blue", label="u = [2, 1]")
arrow(v, color="tab:purple", label="v = [1, 3]")
arrow(v, start=u, color="tab:purple", alpha=0.4)        # v ni u uchiga ko'chiramiz
arrow(u + v, color="tab:green", label="u + v = [3, 4]")
arrow(c * u, color="tab:orange", label=f"{c}·u = {(c * u).tolist()}")

ax.set_xlim(-4, 5)
ax.set_ylim(-3, 5)
ax.set_aspect("equal")                  # x va y birligi bir xil bo'lsin
ax.axhline(0, color="gray", lw=0.8)
ax.axvline(0, color="gray", lw=0.8)
ax.grid(alpha=0.3)
ax.legend(loc="upper left")
ax.set_title("Vektor qo'shish va songa ko'paytirish")
plt.show()