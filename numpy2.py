import numpy as np

csvdata = np.loadtxt('abc.csv',delimiter=',', dtype=str, skiprows=1)

print(csvdata[0:5:])



# transpose =>matrix 2d row ==columns

# arr = np.array([[4,6,8],[6,8,9],[2,3,4],[5,7,9]])
# print(arr)
# print(arr.T)

# arr= np.array([[[11,98],[4,8]],[[6,0],[3,8]]])
# print(arr.ndim)
# print(arr.itemsize)
# print(arr.shape)


# arrF = np.array([1.1,6.78,9.768],dtype=np.float16)
# print(arrF.dtype)

# arr = np.array([1,20,31,128,255],dtype=np.uint8)
#
# print(arr)
# print(arr.dtype)


# int8  = > 127 <-> -128
# unsigned int 8  => 0-255
# 8 = > 2^8
# 64 = 8bytes ,    ram  = > 4GB => 4*1024*1024*1024B
#
#  2.1 km => 219378675534234567

