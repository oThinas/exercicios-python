def sum(list):
  if len(list) == 1:
    return list[0]
  
  return list[0] + sum(list[1:])

def factorial(number):
  if number == 0 or number == 1:
    return 1
  return number * factorial(number - 1)

print(sum(
  [1, 2, 3]
))

print(factorial(5))