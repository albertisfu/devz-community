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
        
    
    #remove duplicates elements form the linked list
    def delete_duplicates(self):
        uniq_values = {}
        if self.head != None:
            current_node = self.head
           
            while current_node != None:

                #check if current.data is inside uniq_values dict (duplicate)
                exist = uniq_values.get(current_node.data, True)
                if exist != True:
                    #delete node if is duplicate
                    self.delete(current_node)
                
                else:
                    #add current data to uniq_values dict
                    uniq_values[current_node.data] = None
                
                #change reference to next Node(data)
                current_node = current_node.next_node
            




#test 1
new_list = LinkedList()

n1 = new_list.append(4)
n2 = new_list.append(5)
n3 = new_list.append(9)
n4 = new_list.append(0)
n5 = new_list.append(5)
n5 = new_list.append(1)
n6 = new_list.append(2)

print("-------- TEST 1 ------------")
print('Original Linked List')
new_list.print_list()

print('After remove Duplicates:')
new_list.delete_duplicates()
new_list.print_list()


new_list2 = LinkedList()

n12 = new_list2.append(1)
n22 = new_list2.append(2)
n32 = new_list2.append(3)
n42 = new_list2.append(3)
n52 = new_list2.append(2)
n52 = new_list2.append(1)

print("-------- TEST 2 ------------")
print('Original Linked List')
new_list2.print_list()

print('After remove Duplicates:')
new_list2.delete_duplicates()
new_list2.print_list()
