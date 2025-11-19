import numpy as np
import matplotlib.pyplot as plt

arr = np.array([1,2,3,4,5])
print("Array: ", arr)
print("Mean: ", np.mean(arr))

plt.plot(arr, color='red')
plt.title("Simple Line Graph")
plt.show()