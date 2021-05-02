

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


class StackQueue:
    
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def push(self, data):
        self.in_stack.push(data)
    
    def  pop(self):
        while self.in_stack.peek() != None:
            value = self.in_stack.pop()
            self.out_stack.push(value)
        
        return self.out_stack.pop()
    

    def peek(self):
        while self.in_stack.peek() != None:
            value = self.in_stack.pop()
            self.out_stack.push(value)
        
        return self.out_stack.peek()
    






new_stack = StackQueue()

new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)


print('peek: ', new_stack.peek() )
print('pop: ', new_stack.pop() )
print('peek: ', new_stack.peek() )
