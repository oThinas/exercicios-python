import list
list = list.Constants().LIST

def insertionSort(list):
  for i in range(1, len(list)):
    target = list[i]
    j = i - 1
    while j >= 0 and list[j] > target:
      list[j + 1] = list[j]
      j -= 1
    list[j + 1] = target
  return list

print(list)
print(insertionSort(list[:]))
print(list)