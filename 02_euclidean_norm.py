def euclidean_norm(vector):
#place your code here
  result=0
  for n in vector:
    result+= (n**2)
  return result**.5

import numpy as np
my_vector = [0.5, -1.2, 3.3, 4.5]
# The result should be roughly 5.729746940310715
euclidean_norm(my_vector)
