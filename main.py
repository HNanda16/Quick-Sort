def partition(myArray, start, end):
  pivot = myArray[start]
  leftMark = start + 1
  done = False
  rightMark = end

  while(done == False):
    while(leftMark <= rightMark and myArray[leftMark] <= pivot):
      leftMark += 1
    while(rightMark >= leftMark  and myArray[rightMark] >= pivot):
      rightMark -= 1
      
    if(leftMark > rightMark):
      done = True
    else:
      temp = myArray[leftMark]
      myArray[leftMark] = myArray[rightMark]
      myArray[rightMark] = temp
  
  temp = myArray[start]
  myArray[start] = myArray[rightMark]
  myArray[rightMark] = temp
  return rightMark


def quickSort(myArray, start, end):
  if(start < end):
    split = partition(myArray, start, end)
    quickSort(myArray, start, split)
    quickSort(myArray, split+1, end)
  return myArray


aList = [9, 1, 6, 2, 8, 4, 0]
print(quickSort(aList, 0, len(aList)-1))