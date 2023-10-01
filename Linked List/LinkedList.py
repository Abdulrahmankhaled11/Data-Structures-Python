class Node : #the class of the node 
    def __init__(self,data=None) :
        self.data = data
        self.next = None


class SinglyLinkedList : #the class of the list 
    def __init__(self) :
        self.tail= None
        self.size = 0

    def append(self, data): # append function 
        node = Node(data)

        if self.tail== None:
            self.tail = node
        else:
            current= self.tail
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def delete(self, data): # deletion function 
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    current = None
                    self.size -= 1
                    return
                else:
                    prev.next = current.next
                    self.tail =prev
                    current = None
                    self.size -= 1
                    return
        
   
#test the code           
l = SinglyLinkedList()  # create an object
#adding values 
l.append("aa") 
l.append("bb")

print(l.size) # get the size after appending

#delete a value
l.delete("aa")

print(l.size) # get the size after deletion

