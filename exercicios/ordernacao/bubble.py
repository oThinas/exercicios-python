import list
list = list.Constants().LIST
            
def bubbleSort(list):
	aux = len(list)
	while aux > 1:
		for i in range(len(list) - 1):
			if list[i] > list[i + 1]:
				list[i], list[i + 1] = list[i + 1], list[i]
		aux -= 1
	return list

print(list)
print(bubbleSort(list[:]))
print(list)