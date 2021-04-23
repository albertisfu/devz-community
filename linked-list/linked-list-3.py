# Alberto Islas 
# Linked List and remove duplicates of a linked list



#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


#LinkedList Class
class LinkedList:
    def __init__(self):
        self.head = None

    #append new elements to linked list method
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return new_node
        else:
            current_node =self.head

            while current_node.next_node != None:
                current_node = current_node.next_node
            
            current_node.next_node = new_node

            return new_node
            
    #print elements of linked list
    def print_list(self):
        if self.head != None:
            current_node = self.head
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next_node
    
    #delete a node from linked list
    def delete(self, node_to_delete):

        prev_node = None
        current_node =self.head
        while current_node !=None:
            
            if current_node == node_to_delete:
                if prev_node == None:
                    #if is head node, change linked list head
                    self.head = current_node.next_node
                else:
                    #if is not head node, change prev node reference to current.next_node
                    prev_node.next_node = current_node.next_node
            
                
            prev_node = current_node
            current_node = current_node.next_node
        
    

def count_places(list1, target):

    counter = 0
    gap_flag = False
    if list1.head != None:
        current_node = list1.head
        behind_node = list1.head
        while current_node !=None:
            #transverse list whith two pointers, one k places behind current node.
            counter = counter + 1

            #start second pointer when k places gap is reached
            if counter  == target+2 or gap_flag == True:
                gap_flag = True
                behind_node = behind_node.next_node
            
           
            current_node = current_node.next_node
        

    #return value of second pointer
    return behind_node.data

    #Solution O(n) on time and O(1) on memory








#test 1
print("- TEST 1 -")
new_list = LinkedList()
n1 = new_list.append(1)
n2 = new_list.append(2)
n3 = new_list.append(3)
n4 = new_list.append(4)
n5 = new_list.append(5)
n6 = new_list.append(6)
n7 = new_list.append(7)
n8 = new_list.append(8)
n9 = new_list.append(9)
n10 = new_list.append(10)

print("-------- List 1 ------------")
new_list.print_list()

target = 9
print('K values: ', target )

print('El nodo con K lugares antes del ultimo nodo es: ', count_places(new_list, target))





#test 1
print("- TEST 2 -")
new_list = LinkedList()
n1 = new_list.append(2)
n2 = new_list.append(3)
n3 = new_list.append(1)
n4 = new_list.append(4)
n5 = new_list.append(9)
n6 = new_list.append(10)
n7 = new_list.append(11)


print("-------- List 2 ------------")
new_list.print_list()

target = 2
print('K values: ', target )

print('El nodo con K lugares antes del ultimo nodo es: ', count_places(new_list, target))
