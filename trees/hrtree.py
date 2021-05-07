class Node:
	def __init__(self, value):
		self.value = value
		self.branches = None
		self.is_ceo = True

class HrChart:
	def __init__(self):
		self.root = None
		self.nodes = {}
    

	def built(self, tuplas):
		for tupla in tuplas:
			em_id = tupla[0]
			#print('em_id: ', em_id)
			employee = self.nodes.get(em_id, False)
			if employee == False:
				#print('create em')
				employee= Node(em_id)
				employee.branches = {}
				self.nodes[em_id] = employee
			employee.is_ceo = False

			ma_id = tupla[1]
			#print('ma_id: ', ma_id)
			manager = self.nodes.get(ma_id, False)
			if manager == False:
				#print('create ma')
				manager = Node(ma_id)
				manager.branches = {}
				self.nodes[ma_id] = manager

			manager.branches[em_id] = employee

		#asign CEO
		for key in self.nodes:
			if self.nodes[key].is_ceo == True:
				print('CEO: ', key)
				self.root = self.nodes[key]

	

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
	

	def is_manager(self,manager_id, employee_id):
		manager_node = self.nodes[manager_id]

		report_to = manager_node.branches.get(employee_id, False)

		if report_to != False:
			return True
		else:
			return False






		


	

tuplas = [[4,7],[1,5],[5,3],[7,3],[6,3],[2,5]]

instance = HrChart()
instance.built(tuplas)

#instance.print_branches(None)

print('---------')
employee1 = 5
employee2 = 2
print('Empleado: ', employee1)
print('Reporta a: ', employee2, '?')
print(instance.is_manager(employee1,employee2))