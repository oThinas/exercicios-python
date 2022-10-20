import list
list = list.Constants().LIST

def quickSort(list):
  if len(list) <= 1:
    return list
  else:
    pivot = list.pop()
    itemsGreater = []
    itemsLower = []

    for item in list:
      if item > pivot:
        itemsGreater.append(item)
      else:
        itemsLower.append(item)

    return quickSort(itemsLower) + [pivot] + quickSort(itemsGreater)

print(list)
print(quickSort(list[:]))
print(list)