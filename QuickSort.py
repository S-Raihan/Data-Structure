#Most using sorting algorithm
#Time complexity is O(nlogn)



def QuickSort(MyList, left,right):
	if left<right:
		pivot = Partition(MyList,left,right)
		QuickSort(MyList,left,pivot-1)
		QuickSort(MyList,pivot+1,right)


def Partition(MyList,left,right):
	i = left
	pivot = MyList[right]
	for j in range(left,right):
		if MyList[j]<pivot:
			MyList[i],MyList[j] = MyList[j], MyList[i]
			i+=1
			

	MyList[i], MyList[right] = MyList[right], MyList[i]
	return i 

def PrintList(MyList):
	for i in MyList:
		print(i,end = " ")
	print()

ListForQuickSort= [55,70,12,17,18,65,45,50]
PrintList(ListForQuickSort)
n = len(ListForQuickSort)
QuickSort(ListForQuickSort,0,n-1)
PrintList(ListForQuickSort)
