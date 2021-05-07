class Node:
	def __init__(self, value):
		self.value = value
		self.branches = None
		self.is_ceo = True

class HrChart:
	def __init__(self):
		self.root = None
    

	def built(self, tuplas):
		nodos = {}
		for tupla in tuplas:
			em_id = tupla[0]
			#print('em_id: ', em_id)
			employee = nodos.get(em_id, False)
			if employee == False:
				#print('create em')
				employee= Node(em_id)
				employee.branches = {}
				nodos[em_id] = employee
			employee.is_ceo = False

			ma_id = tupla[1]
			#print('ma_id: ', ma_id)
			manager = nodos.get(ma_id, False)
			if manager == False:
				#print('create ma')
				manager = Node(ma_id)
				manager.branches = {}
				nodos[ma_id] = manager

			manager.branches[em_id] = employee

		#asign CEO
		for key in nodos:
			if nodos[key].is_ceo == True:
				print('ceo: ', key)
				self.root = nodos[key]

	

	def print_branches(self, node):

		if node == None:
			node = self.root
			print(node.value)

		#print('ceso orint:', node.value)	

		if node.branches == {}:
			print('----')
			return None

		for key in node.branches:
			#print('entro aqui')
			print(node.branches[key].value)
			self.print_branches(node.branches[key])
	

	def is_manager1(self, node, manager_id, employee_id, flag):

		flag = flag
		if node == None:
			node = self.root
		
		if node.value == manager_id:
			print('manager_id: ', node.value )
			for key in node.branches:
				print('key: ', key)
				print('emplooye_id: ', employee_id)
				if node.branches[key].value == employee_id:
					print('entro true')
					flag = True
					break
				
		else:
			for key in node.branches:
				print('entro recursivo')
				self.is_manager1(node.branches[key], manager_id, employee_id, flag)

			
		if node.branches == {}:
			print('---- flag')
			return flag
		
		return flag




		


	

tuplas = [[4,7],[1,5],[5,3],[7,3],[6,3],[2,5]]

instance = HrChart()
instance.built(tuplas)

#instance.print_branches(None)

result = instance.is_manager1(None, 7, 4, False)
print('Is manger: ', result)