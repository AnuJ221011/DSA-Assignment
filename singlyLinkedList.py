class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.__head__=None
        self.__tail__=None
        self.__size__=0

    def __iter__(self):
        self.__trav__ = self.__head__
        return self

    def __next__(self):
        x=self.__trav__
        if self.__trav__ is None:
            raise StopIteration
        self.__trav__ = self.__trav__.next
        return x

    def InsertAtIndex(self, index, data):
        if index < 0 or index > self.__size__:
            raise IndexError
        if index == 0:
            self.InsertAtBeginning(data)
        elif index == self.__size__:
            self.Append(data)
        else:
            trav = self.__head__
            idx=0
            while idx < index-1:
                trav = trav.next
                idx+=1
            newNode = Node(data)
            newNode.next = trav.next
            trav.next = newNode
            self.__size__+=1

    def InsertAtBeginning(self, data):
        newNode = Node(data)
        if self.__head__ is None:
            self.__head__ = newNode
            self.__tail__ = newNode
        else:
            newNode.next = self.__head__
            self.__head__ = newNode
        self.__size__+=1

    def Append(self, data):
        newNode = Node(data)
        if self.__head__ is None:
            self.__head__ = newNode
            self.__tail__ = newNode
        else:
            self.__tail__.next = newNode
            self.__tail__ = newNode
        self.__size__+=1

    def Size(self):
        return self.__size__
    
    def IsEmpty(self):
        return self.__size__ == 0
    
    def RemoveAtIndex(self, index):
        if index < 0 or index >= self.__size__:
            raise IndexError
        if index == 0:
            self.RemoveFirst()
        elif index == self.__size__-1:
            self.RemoveLast()
        else:
            trav = self.__head__
            idx=0
            while idx < index-1:
                trav = trav.next
                idx+=1
            trav.next = trav.next.next
            self.__size__-=1

    def RemoveFirst(self):
        if self.IsEmpty():
            raise Exception("Empty List")
        if self.__head__ == self.__tail__:
            self.__head__ = None
            self.__tail__ = None
        else:
            self.__head__ = self.__head__.next
        self.__size__-=1

    def RemoveLast(self):
        if self.IsEmpty():
            raise Exception("Empty List")
        if self.__head__ == self.__tail__:
            self.__head__ = None
            self.__tail__ = None
        else:
            trav = self.__head__
            while trav.next != self.__tail__:
                trav = trav.next
            self.__tail__ = trav
            trav.next = None
        self.__size__-=1

    def rotateRightbyK(self, k):
        if self.IsEmpty():
            return
        k = k % self.__size__
        if k == 0:
            return
        trav = self.__head__
        for i in range(self.__size__-k-1):
            trav = trav.next
        self.__tail__.next = self.__head__
        self.__head__ = trav.next
        trav.next = None
        self.__tail__ = trav

    def Reverse(self):
        if self.IsEmpty():
            return
        trav = self.__head__
        prev = None
        while trav is not None:
            next = trav.next
            trav.next = prev
            prev = trav
            trav = next
        self.__head__ = prev


    
    def __str__(self):
        list=[]
        trav = self.__head__
        while trav is not None:
            list.append(trav.data)
            trav=trav.next
        return " ---> ".join([str(i) for i in list])
    
    def MiddleElement(self):
        if self.IsEmpty():
            return
        trav = self.__head__
        for i in range(self.__size__//2):
            trav = trav.next
        return trav
    
    def IndexOf(self, data):
        if self.IsEmpty():
            return -1
        idx = 0
        trav = self.__head__
        while trav is not None:
            if trav.data == data:
                return idx
            trav = trav.next
            idx+=1
        return -1
    
    def MergeTwoSorted(self, other):
        merged_list = LinkedList()
        trav1, trav2 = self.__head__, other.__head__
        while trav1 is not None and trav2 is not None:
            if trav1.data <= trav2.data:
                merged_list.Append(trav1.data)
                trav1 = trav1.next
            else:
                merged_list.Append(trav2.data)
                trav2 = trav2.next
        while trav1 is not None:
            merged_list.Append(trav1.data)
            trav1 = trav1.next
        while trav2 is not None:
            merged_list.Append(trav2.data)
            trav2 = trav2.next
        return merged_list

    def Interleave(self, other):
        interleaved_list = LinkedList()
        trav1, trav2 = self.__head__, other.__head__
        while trav1 is not None and trav2 is not None:
            interleaved_list.Append(trav1.data)
            interleaved_list.Append(trav2.data)
            trav1 = trav1.next
            trav2 = trav2.next
        while trav1 is not None:
            interleaved_list.Append(trav1.data)
            trav1 = trav1.next
        while trav2 is not None:
            interleaved_list.Append(trav2.data)
            trav2 = trav2.next
        return interleaved_list

    def Split(self, index):
        if index < 0 or index > self.__size__:
            raise IndexError("Index out of bounds")
        left = LinkedList()
        right = LinkedList()
        trav = self.__head__
        for i in range(index):
            left.Append(trav.data)
            trav = trav.next
        while trav is not None:
            right.Append(trav.data)
            trav = trav.next
        return left, right
    

l=LinkedList()
print(l.Size())
print(l.IsEmpty())
l.InsertAtBeginning(5)
l.InsertAtBeginning(6)
l.InsertAtBeginning(7)
l.InsertAtBeginning(8)
l.InsertAtBeginning(9)
print(l.Size())
l.Append(100)
l.InsertAtIndex(0, 10)
l.InsertAtIndex(1, 20)
l.InsertAtIndex(2, 30)
l.InsertAtIndex(3, 40)
l.InsertAtIndex(4, 50)
print(l.Size())
print(l.IsEmpty())  
print(l)

# Creating two sorted linked lists
list1 = LinkedList()
list1.Append(1)
list1.Append(2)
list1.Append(5)
list1.Append(7)

list2 = LinkedList()
list2.Append(3)
list2.Append(4)
list2.Append(7)
list2.Append(8)

# Merging two linked lists
merged_list = list1.MergeTwoSorted(list2)
print("Merged List: ", merged_list)  

# Interleaving two linked lists
interleaved_list = list1.Interleave(list2)
print("Interleaved List: ", interleaved_list)  

# Splitting a linked list into two at index 3
left_list, right_list = merged_list.Split(3)
print("Left List: ", left_list)    
print("Right List: ", right_list)

print(l.MiddleElement())
print(l.IndexOf(50))
l.rotateRightbyK(3)
print(l)
l.Reverse()
print(l)
