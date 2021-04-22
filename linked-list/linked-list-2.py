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
            





def sum_linked(list1, list2):
    new_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    carry  = 0

    #traverse list until last element of one list 
    while current1 !=None and current2 != None:
        val1 = current1.data
        val2 = current2.data

        #the sum consist of adding each component of each list to each component of the other list plus adding the carry from previous sum
        suma = val1 + val2 + carry

        #in order to conserve reverse order, convert the sum to their reversed equivalent
        suma_reversed =  str(suma)[::-1]

        #append the first element of sum to the  sum result list
        new_list.append(int(suma_reversed[0]))


        #if the sum result is two digits
        if len(suma_reversed) >1:

            #check if the next nodes are not None, then store the accumulted to next iteration
            if current1.next_node !=None and current2.next_node !=None:
                carry =  int(suma_reversed[1])   
            else:
                #in case one of the next nodes are None (edge case with list of different sizes), complete the sum with carry with the next remain elements of list
                carry =  int(suma_reversed[1])

                #check if next node of current1 list  is not None but current2 list is (edge case with list of different sizes)
                if current1.next_node !=None and current2.next_node ==None:

                    #complete the sum of the remain elements of current 1 list
                    while current1.next_node != None:
                        sum_carry = current1.next_node.data + carry
                        sum_carry_reversed =  str(sum_carry )[::-1]
                        new_list.append(int(sum_carry_reversed[0]))
                        carry = int(sum_carry_reversed[1])
                        current1 = current1.next_node
                        if current1.next_node == None:
                            new_list.append(carry)

                        

                #check if next node of current2 list  is not None but current1 list is (edge case with list of different sizes)
                elif current2.next_node !=None and current1.next_node ==None:

                    #complete the sum of the remain elements of current w list
                    while current2.next_node != None:
                        sum_carry = current2.next_node.data + carry
                        sum_carry_reversed =  str(sum_carry )[::-1]
                        new_list.append(int(sum_carry_reversed[0]))
                        carry = int(sum_carry_reversed[1])
                        current2 = current2.next_node
                        if current2.next_node == None:
                            new_list.append(carry)
                
                else:
                    #if both list are same size and remain a carry
                    new_list.append(carry)    
                        
                        
        else:
            #if we don't have carry
            #check if next node of current1 list  is not None but current2 list is (edge case with list of different sizes)
            if current1.next_node !=None and current2.next_node ==None:
                #add the remain values of current1 list to sum list
                while current1.next_node != None:
                    new_list.append(current1.next_node.data)
                    current1 = current1.next_node
            #check if next node of current2 list  is not None but current1 list is (edge case with list of different sizes)
            elif current2.next_node !=None and current1.next_node ==None:
                #add the remain values of current2 list to sum list
                while current2.next_node != None:
                    new_list.append(current2.next_node.data)
                    current2 = current2.next_node
        
        #asign next nodes
        current1 = current1.next_node
        current2 = current2.next_node
        

    
    
    return new_list
    # BigO O(A+B) ya que ambas listas son completamente recorridas





#test 1
print("- TEST 1 -")
new_list = LinkedList()
n1 = new_list.append(9)
n1 = new_list.append(9)
n1 = new_list.append(9)
print("-------- List 1 ------------")
new_list.print_list()

new_list2 = LinkedList()
n12 = new_list2.append(1)
print("-------- List 2 ------------")
new_list2.print_list()
print("--------------------")
print('Suma:')
suma_list = sum_linked(new_list, new_list2)
suma_list.print_list()



#test 2
print("- TEST 2 -")
new_list = LinkedList()
n1 = new_list.append(2)
n1 = new_list.append(3)
n1 = new_list.append(1)
print("-------- List 1 ------------")
new_list.print_list()

new_list2 = LinkedList()

n12 = new_list2.append(6)
n22 = new_list2.append(0)
n32 = new_list2.append(3)
print("-------- List 2 ------------")
new_list2.print_list()
print("--------------------")
print('Suma:')
suma_list = sum_linked(new_list, new_list2)
suma_list.print_list()




#test 2
print("- TEST 3 -")
new_list = LinkedList()
n1 = new_list.append(9)
n1 = new_list.append(9)
n1 = new_list.append(9)
print("-------- List 1 ------------")
new_list.print_list()

new_list2 = LinkedList()

n12 = new_list2.append(0)
n22 = new_list2.append(1)
n32 = new_list2.append(1)
print("-------- List 2 ------------")
new_list2.print_list()
print("--------------------")
print('Suma:')
suma_list = sum_linked(new_list, new_list2)
suma_list.print_list()