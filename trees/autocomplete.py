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
			parent_node = None  #initialize parent_node as None on every string to built
			for char in string:
				#with each new string start building from root
				if parent_node == None:
					#create root node if not exist
					if self.root == None:
						parent_node = Node(None) #create root node
						parent_node.branches = {} #initialize hash
						self.root = parent_node

					else:
						#refer to root node
						parent_node = self.root 
					#check if the next char to add is now within parent node branches
					next_node = parent_node.branches.get(char, False)
					if next_node == False:
						#if do not exist that branch in root node, create
						next_node = Node(char)
						next_node.branches = {}
						#assign new node as a branch of root node
						parent_node.branches[char] = next_node
					#refer parent_node to next_node
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
			
			#mark as terminal node if is the last node of string
			next_node.is_terminal = True
	


		
	
	def get_next(self, string):
		parent_node = self.root
		if parent_node.branches != {}:

			#reach the last node of string following the keys
			for char in string:
				parent_node = parent_node.branches[char]
			
			#print last level keys
			for key in parent_node.branches:
				print(key, end=', ')


	
	def print_valid(self, node):
		
		if node == None:
			node = self.root
		
		#print value of terminal node
		if node.is_terminal == True:
			print(node.value)
		
		if node.branches == {}:
			return None
		
		#recursive function to reach the full path of a node
		for key in node.branches:
			self.print_valid(node.branches[key])

	
	def get_autocomplete(self, string):

		parent_node = self.root

		if parent_node.branches != {}:

			#reach the last node of string following the keys
			for char in string:
				parent_node = parent_node.branches[char]

			
			for key in parent_node.branches:
				#acces to recursive function to reach the full path of a node
				self.print_valid(parent_node.branches[key])






instance = Autocomplete()

strings = ['car', 'cartier','cat', 'catamaran', 'bus', 'mouse']
print('Cadenas: ', strings)
instance.built(strings)

characters = 'ca'
print('Next nodes  of: ', characters )

instance.get_next(characters)
print('\n')
print('Autocomplete of: ',characters )
instance.get_autocomplete(characters)