import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

#Ejemplo 2---------------------------------------------
import numpy as np

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

#Ejemplo 3---------------------------------------------
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

#Ejemplo 4---------------------------------------------
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

#Ejemplo 5---------------------------------------------
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

#Ejemplo 6---------------------------------------------
import numpy as np

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype(int)

print(newarr)
print(newarr.dtype)

#Ejemplo 7---------------------------------------------
import numpy as np

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)
