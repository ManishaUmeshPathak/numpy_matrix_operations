import numpy as np

#Create a 1-dimensional array:
def array_operations():
  arr_1d=np.array([1,2,3,4,5])
  print("1d Array:")
  print(arr_1d)


#Create a 2-dimensional array:
  arr_2d=np.array([[1,2,3],[4,5,6]])
  print("2d Array:")
  print(arr_2d)


#Perform element-wise addition:
  added_array=arr_1d+5
  print("1d Array+5:")
  print(added_array)


#Perform element-wise multiplication:
  multiplied_array=arr_1d*2
  print("1d Array*2:")
  print(multiplied_array)


#Compute basic statistics on array:
  print("Statistics on 1d array:")
  print(f"Mean: {np.mean(arr_1d)}")
  print(f"Standard Deviation: {np.std(arr_1d)}")
  print(f"Sum: {np.sum(arr_1d)}")


#Reshape the 1d Array to a 2d Array:
  reshaped_array=arr_1d.reshape(5,1)
  print("Reshaped 1d array to 2d array:")
  print(reshaped_array)


if __name__ == "__main__":
    array_operations()








