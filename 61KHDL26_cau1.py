# Đề 26 câu 1
import numpy as np
import matplotlib.pyplot as plt
A = np.random.uniform(0,10,10)	
print(A)
B = np.random.uniform(0,10,10)
print(B)
# b euclid giữa 2 dãy số np.
dist = np.linalg.norm(A-B)
print(dist)
# c phương sai các phân tử trong dãy số a
import statistics
print("Phuong sai: ",statistics.variance(A))
# d vẽ
plt.plot([A[i] for i in range(0,10)], label='Dãy A')
plt.plot([B[i] for i in range(0,10)], label='Dãy B')
plt.title('Biểu đồ tương quan của A và B')
plt.legend(loc='best')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#e  tìm số chính phương trong 2 list
import math
LCP = []
for i in A:
  root = math.sqrt(i)
  if int(root)**2 == i:
    LCP.append(i)
for i in B:
  root = math.sqrt(i)
  if int(root)**2 == i:
    LCP.append(i)
tu = set(LCP)
print(tu) # tranh trung lap
