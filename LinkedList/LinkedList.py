class Node(object):
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList(object):
    """ A simple linked list """

    def __init__(self):
        self.head = None
    def append(self, data):
        """Add a node at the end of the list with data"""
        if self.head == None:
            self.head = Node(data)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)
    def prepend(self, data):
        """Add a node at the begening of the list with data"""
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead
    def deleteWithValue(self, data):
        """Delete a node with data as value"""
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
            current = current.next
    def printList(self):
        current = self.head
        while current != None:
            print(current.data, end='->')
            current = current.next
        print("None")
#if __name__ == '__main__':
#    Data = input("Enter your data : ").split(" ")
#    myList = LinkedList()
#    print("Your list is : ")
#    for data in Data:
#        myList.append(data)
#    myList.printList()
#    myList.deleteWithValue(input("enter something to delete : "))
#    myList.printList()
