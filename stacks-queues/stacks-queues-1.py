

#Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


#LinkedList Class
class Stack:
    def __init__(self):
        self.head = None

    #append new elements to linked list method

    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            prev_head = self.head
            self.head =  new_node
            new_node.next_node = prev_head
    
    def peek(self):
        if self.head != None:
            #print(self.head.data)
            return self.head.data
        else:
            #print('None')
            return None

    def pop(self):
        if self.head != None:
            last_node = self.head
            #print(last_node.data)
            self.head = last_node.next_node
            return last_node.data
        else:
            #print('None')
            return None


            
    #print elements of linked list
    def print_list(self):
        if self.head != None:
            current_node = self.head
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next_node



class CustomStack:
    def __init__(self):
        self.head = None
        self.base_stack = Stack()

    #append new elements to linked list method

    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            prev_head = self.head
            self.head =  new_node
            new_node.next_node = prev_head
        
        #set min value top top stack
        #check last value in base_stack
        last_value_stack = self.base_stack.peek()
        #check is base stack is not empty
        if last_value_stack != None:
            #check if new value is < last_value_stack, if true then add pushed value to stack
            if new_node.data < last_value_stack:
                self.base_stack.push(new_node.data)
            else:
                #pop last_value then push new value and then restore last_value to top
                self.base_stack.pop()
                self.base_stack.push(new_node.data)
                self.base_stack.push(last_value_stack)

        else:
            #if empty just add pushed value
            self.base_stack.push(new_node.data)

        

    
    def peek(self):
        if self.head != None:
            return self.head.data
        else:
            return None

    def pop(self):
        if self.head != None:
            last_node = self.head
            self.head = last_node.next_node


            #extract value from stack
            #check last value in base_stack
            last_value_stack = self.base_stack.peek()
            #check is base stack is not empty
            if last_value_stack != None:
                #check if extracted value is on top of base stack, if true then extract the value from base_stack
                if last_node.data == last_value_stack:
                    self.base_stack.pop()
                else:
                    #if false then, extract last value of base stack, confirm is the value extracted is now in top of base stack, if yes then extract it
                    self.base_stack.pop()
                    if last_node.data == self.base_stack.peek():
                        self.base_stack.pop()

                    #restore the previous value to the top of stack
                    self.base_stack.push(last_value_stack)

            return last_node.data
        else:
            return None
        

        
        
    
    def get_min(self):
        return self.base_stack.peek()


            
    #print elements of linked list
    def print_list(self):
        if self.head != None:
            current_node = self.head
            while current_node != None:
                print(current_node.data)
                current_node = current_node.next_node



new_stack = CustomStack()

new_stack.push(3)
new_stack.push(-1)
new_stack.push(2)
new_stack.push(-2)

print('Stack ---------------')
new_stack.print_list()

print('TEST---------------')

print('min value: ',new_stack.get_min())

print('pop: ', new_stack.pop() )
print('peek: ', new_stack.peek() )

print('push: 30 ' ) 
new_stack.push(30)
print('push: 10 ' ) 
new_stack.push(10)

print('min value: ',new_stack.get_min())

print('pop: ', new_stack.pop() )
print('peek: ', new_stack.peek() )

print('push: -5 ' ) 
new_stack.push(-5)

print('min value: ',new_stack.get_min())

print('pop: ', new_stack.pop() )
print('peek: ', new_stack.peek() )

print('min value: ',new_stack.get_min())