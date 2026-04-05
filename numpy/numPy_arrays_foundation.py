import numpy as np
import time


# Dimensions (axes)

a = np.array([1, 2, 3])  		# 1D - shape (3,)
b = np.array([[1, 2],[3, 4]])	# 2D - shape (2,2)
c = np.zeros((2, 3, 4))			# 3D - shape (2,3,4)

# Shape, dtype, ndim

a = np.array([[1.0, 2.0], [3.0, 4.0]])

print(a.shape)	#(2,2)
print(a.dtype)	# float 64
print(a.ndim)	# 2
print(a.size)	# total elemnts


# Vectorized operations — no loops needed
# The most important thing to internalize
# NumPy arrays let you express math directly instead of writing loops:
# This vectorization is why NumPy underpins nearly all of scientific Python 
# (pandas, scipy, scikit-learn, PyTorch, etc.).

a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)



n = 1_000_000
data_list = list(range(n))
data_np = np.arange(n, dtype=float)

t0 = time.perf_counter()
list_result = [x**2 + 2*x for x in data_list]
t1 = time.perf_counter()

t2 = time.perf_counter()
np_result = data_np**2 + 2*data_np
t3 = time.perf_counter()

print(f"List:  {(t1-t0)*1000:.1f} ms")
print(f"NumPy: {(t3-t2)*1000:.1f} ms")
print(f"Speedup: {(t1-t0)/(t3-t2):.1f}×")









