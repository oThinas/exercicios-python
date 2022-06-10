from inventarioFuncoes import *

op = 1

while op in range(1, 4):
  op = exibirMenu()
  
  if op == 1:
    registrarItem()
  
  elif op == 2:
    incluirItem()
  
  elif op == 3:
    exibirItem()
  
  op = 1