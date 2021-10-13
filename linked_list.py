#Create Node for linked list

class Node:
	def __init__ (self,data):
		self.data = data
		self.next = None


#Create linked list

class LinkedList:
	def __init__(self):
		self.head = None

#Function for add element last

	def push_last(self,newElement):
		newNode = Node(newElement)

		if (self.head ==None):
			self.head = newNode

		else:
			temp = self.head
			while (temp.next !=None):
				temp = temp.next
			temp.next = newNode


#Instert element in given position




	def push_at(self,newElement,position):
		newNode = Node(newElement)

		if (position< 1):
			print("Position should be greater or less than one")
#Maybe need some change
		elif (position ==1):
			newNode.next = self.head
			self.head = newNode
			

		else:
			temp = self.head

			

			if (temp !=None):
				newNode.next = temp.next
				temp.next = newNode

			else:
				print("Previous node is none")
#Function for printList
	def PrintList(self):
		temp = self.head
		if (temp!=None):
			print("The link list is contain : " ,end=" ")
			while(temp!=None):
				print(temp.data, end = " ")
				temp = temp.next
			print()
		else:
			print("The list is empty")




MyList = LinkedList()

MyList.push_last(22)
MyList.push_last(11)
MyList.push_last(21)
MyList.push_last(42)

MyList.PrintList()

MyList.push_at(50,1)

MyList.PrintList()

MyList.push_at(100,1)

MyList.PrintList()





