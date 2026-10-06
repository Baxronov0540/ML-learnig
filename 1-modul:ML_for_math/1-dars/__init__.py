import numpy as np
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

np.random.seed(42)  # Set a random seed for reproducibility
X = load_iris().data
u = np.array([1,5,23,1])
v = np.array([2,3,5,6])

print(u+v) # vektoralrni bir biriga qoshish numpy orqali  bu  biz yozganimizdan ancha osonroq

print(3*u) # bu bir vektorni  odiy songa sklayar kopaytmasini chiqrib beradi
print(u -v)  # bu oddiy ikkita vektorni bir birdan ayirsish

mu = X.sum(axis=0)/len(X)

sd= X.std(axis=0)

X_manual =  (X-mu) / sd

X_sklearn = StandardScaler().fit_transform(X)

print(np.allclose(X_manual, X_sklearn))  # True chiqadi bu degani ikkisi bir xil ekanligini bildiradi
print(X_manual.round(3))  # bu bizga 2 xonali sonlarni chiqarib beradi")




