class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        if self.length == 0:
            print("The linked list is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = None
        self.length += 1


    def pop(self):
        if self.head is None:
            print("No node in the linked list")
        else:
            temp = self.head
            popped = self.tail
            while temp is not None:
                if temp.next is self.tail:

                    self.tail = temp
                    self.tail.next = None
                temp = temp.next

        self.length -= 1
        if self.length == 0:
            print (f"The length of the list is 0 and the popped value is {popped.value}")

        else:
            # print (f"The popped value is {popped.value}")
            return popped

    def prepend(self,value):
        first_node = Node(value)
        if self.length == 0:
            self.head = first_node
            self.tail = first_node
        else:
            first_node.next = self.head
            self.head = first_node
        self.length += 1

    def pop_first(self):
        popped = self.head
        if self.length == 0:
            return None
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.length -= 1
        return popped

    def get(self,index):
        if self.length == 0:
            return None
        elif index < 0 or index > self.length -1:
            return None
        temp = self.head
        i = 0
        while i < index:
            temp = temp.next
            if temp is None:
                return "Index not found in linked list"
            i+=1
        return temp

    def set_value(self, index, value):
        noob = self.get(index)
        if noob is not None:
            noob.value = value
        else:
            return None
        return noob
        # temp = self.head
        # if index > self.length -1 or index < 0:
        #     return None
        # else:
        #     i = 0
        #     while i < index:
        #         temp = temp.next
        #         if temp is None:
        #             return "THe index not found int he linked list"
        #         i += 1
        #     temp.value = value
        # return temp.value

    def insert(self, index, value):
        temp = self.head
        prev = self.head
        i = 0
        if index > self.length or index < 0:
            return None
        elif i == 0:
            self.prepend(value)
        elif i == self.length:
            self.append(value)
        else:
            while i < index:
                temp = temp.next
                prev.next = temp
                i+=1
            new_node = Node(value)
            prev.next = new_node
            new_node.next = temp
        self.length+=1

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return None
        if index == 0:
            removed = self.head
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            i = 0
            prev = self.head
            while i < index - 1:
                prev = prev.next
                i += 1
            removed = prev.next
            prev.next = removed.next
            if removed.next is None:
                self.tail = prev
        self.length -= 1
        return removed.value



my_linked_list = LinkedList(5)
# my_linked_list.pop()
my_linked_list.append(23)
my_linked_list.append(6)
my_linked_list.append(44)
my_linked_list.print_list()
print("HELLOW new list")
# print(my_linked_list.pop())
my_linked_list.prepend(10)
my_linked_list.prepend(20)
my_linked_list.prepend(25)
my_linked_list.print_list()
print("THE get value is ",my_linked_list.get(1))
print("the value is set ",my_linked_list.set_value(2, 56))

print(f"The value inserted", my_linked_list.insert(1,21))
my_linked_list.print_list()

print(f"The value deleted", my_linked_list.remove(3))


# print(f"the first value popped is {my_linked_list.pop_first().value}")


# my_linked_list.pop()
# my_linked_list.print_list()
# my_linked_list.pop()
# my_linked_list.pop()
my_linked_list.print_list()
print(f"The length of the list is {my_linked_list.length}")

# print('Head:', my_linked_list.head.value)
# print('Tail:', my_linked_list.tail.value)
# print('Length:', my_linked_list.length)
