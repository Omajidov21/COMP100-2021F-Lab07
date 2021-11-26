# Fix the TO-DO parts below, there are three of them.

def input_matrix():
  M = []
  for i in range(4):
    valid_input = False
    while not valid_input:
      ## T0-DO: use a try-except block to get the right input from the user
      try:
        inp = input()
        M.append(float(inp))
      except:
        inp = input()
      else:  
        valid_input = True
 
  return tuple(M)

def inverse(M):  
  ## TO-DO: use a try-except block to catch zero division error     
  try: 
    det = M[0] * M[3] - M[1] * M[2]
    M_inv = [M[3], -M[1], -M[2], M[0]]
    for i in range(4):
      M_inv[i] /= det
  except:
    print('Determinant is 0, inverse does not exist')
    return None
  else:
    M_inv = [M[3], -M[1], -M[2], M[0]]
    for i in range(4):
      M_inv[i] /= det
    return tuple(M_inv)

def matmul(M1, M2):
  return (M1[0] * M2[0] + M1[1] * M2[2], M1[0] * M2[1] + M1[1] * M2[3], M1[2] * M2[0] + M1[3] * M2[2], M1[2] * M2[1] + M1[3] * M2[3])

def almost_identity(m, eps):
  ## TO-DO: do this check with assert
    ## TO-DO: do this check with assert
  assert( (abs(m[0] - 1) < eps and abs(m[1]) < eps and abs(m[2]) < eps and abs(m[3] - 1) < eps) ==False ,    'There is a problem in the inverse function')

  assert( (abs(m[0] - 1) < eps and abs(m[1]) < eps and abs(m[2]) < eps and abs(m[3] - 1) < eps) ==True , 'Matrix is equal to identity')

M = input_matrix()
M_inv = inverse(M)
identity = matmul(M, M_inv)
almost_identity(identity, 1e-4)