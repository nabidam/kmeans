import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from kmeans import K_Means as km
X = np.array([20, 50, 109, 182, 200, 220, 228, 310, 340, 380, 410, 460])

# plt.scatter(X, s=150)
# plt.show()

# colors = 10*["g","r","c","b","k"]

clf = km(k=4)
clf.fit(X)
