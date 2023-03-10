def bubbleSort(elements):
    length = len(elements)
    print(length)
    for i in range(length):
        for j in range(i+1, length):
            if elements[j] < elements[i]:
                temp = elements[i]
                elements[i] = elements[j]
                elements[j] = temp
    
    return elements


elems = [15, 17, 1, 20, 45]
print("List before sort : ", elems)
sortedList = bubbleSort(elems)
print("List after sorting : ", sortedList)
