class Node:
	def __init__(self, value):
		self.value = value
		self.is_terminal = False
		self.branches = None


class Autocomplete:
	def __init__(self):
		self.root = None

	def built(self, strings):
		for string in strings:

			parent_node = None  #initialize at the begining of new string

			for char in string:
				
				#with each new string start building from root
				if parent_node == None:
					#C
					#C
					#created root and refer new node C
					if self.root == None:
						parent_node = Node(None) #create root node
						parent_node.branches = {} #initialize hash
						self.root = parent_node

						#temp_node = new_node
					else:
						parent_node = self.root #refer to root node
				
					next_node = parent_node.branches.get(char, False)

					if next_node == False:
						#do not exist that branch in root node
						next_node = Node(char)
						next_node.branches = {}
						#assign new node as a branch of root node
						parent_node.branches[char] = next_node
					
					parent_node = next_node
				
				#for following characters start from last node
				else:
					#new node is not None for following characters, search for new char
					next_node = parent_node.branches.get(char, False)

					if next_node == False:
						#do not exist that branch in root node
						next_node = Node(parent_node.value + char)
						next_node.branches = {}
						#assign new node as a branch of root node
						parent_node.branches[char] = next_node
			
					parent_node = next_node
			
			#mark as terminal node
			next_node.is_terminal = True
	

	def print_valid(self, node):
		
		if node == None:
			node = self.root
		
		if node.is_terminal == True:
			print(node.value)
		
		if node.branches == {}:
			return None
		
		for key in node.branches:
			self.print_valid(node.branches[key])
		
	
	def get_next(self, string):

		parent_node = self.root

		if parent_node.branches != {}:

			for char in string:
				parent_node = parent_node.branches[char]
			

			for key in parent_node.branches:
				print(key, end=', ')

	
	def get_autocomplete(self, string):

		parent_node = self.root

		if parent_node.branches != {}:

			for char in string:
				parent_node = parent_node.branches[char]
				#get lastes node
			
			for key in parent_node.branches:
				#print(key, end='- ')
				self.print_valid(parent_node.branches[key])







	




instance = Autocomplete()
instance.built(['car', 'cat', 'cayo', 'cayopar', 'bus'])

#instance.get_next('ca')
instance.get_autocomplete('c')