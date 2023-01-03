from matplotlib import pyplot as plt
import numpy as np

x = np.arange(6)
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
salePrice = [90, 88, 75, 55, 89, 95]
ratio = [18.5, 19.5, 17.6, 22.3, 52.8, 19.5]

plt.bar(x, salePrice)
plt.xticks(x, month)
plt.plot(x, ratio, marker = 'o', linestyle = '--', color = 'r')

plt.title("Monthly Sales Report")
plt.xlabel("Month")
plt.ylabel("Sale amount")

plt.show()

