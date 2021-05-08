class Node:
	def __init__(self, value):
		self.value = value
		self.branches = None
		self.is_ceo = True

class HrChart:
	def __init__(self):
		self.root = None
		self.nodes = {}
		self.is_in_chain = False
		self.list_sub_employees = []
    

	#assembly of employees tree
	def built(self, tuplas):
		for tupla in tuplas:
			#check if exist or create employee node
			em_id = tupla[0]
			employee = self.nodes.get(em_id, False)
			if employee == False:
				employee= Node(em_id)
				employee.branches = {}
				self.nodes[em_id] = employee
			#if one id is in somepoint an employee can't be the CEO, by default True
			employee.is_ceo = False

			#check if exist or create manager node
			ma_id = tupla[1]
			manager = self.nodes.get(ma_id, False)
			if manager == False:
				manager = Node(ma_id)
				manager.branches = {}
				self.nodes[ma_id] = manager

			#assign employee to manager branches
			manager.branches[em_id] = employee

		#asign CEO
		for key in self.nodes:
			if self.nodes[key].is_ceo == True:
				print('CEO: ', key)
				self.root = self.nodes[key]

	

	def is_manager(self,manager_id, employee_id):
		#find for manager inside nodes of tree
		manager_node = self.nodes[manager_id]
		report_to = manager_node.branches.get(employee_id, False)

		#if employee id is within manager branches, return True
		if report_to != False:
			return True
		else:
			return False



	def is_in_management_chain(self, node, manager_id, employee_id):
		if node == None:
			node = self.root
			#start from manager node (parent node of interest), to avoid transverse the full tree if possible
			manager_node = self.nodes[manager_id]
		else:
			manager_node = node
		
		if node.branches == {}:
			return

		#check within branches node if is employee id
		for key in manager_node.branches:
			if manager_node.branches[key].value == employee_id:
				#assign is_in_chain flag to True
				self.is_in_chain = True
				return 

		#find recursively for employee id  in leaf nodes
		for key in manager_node.branches:
			self.is_in_management_chain(manager_node.branches[key], manager_id, employee_id)
	


	def get_sub_employees(self, node, manager_id):
		if node == None:
			node = self.root
			#start from manager node (parent node of interest), to avoid transverse the full tree if possible
			manager_node = self.nodes[manager_id]
		else:
			manager_node = node
		
		if node.branches == {}:
			return

		#transverse recursively tree from manager_id node to their leafs and append to get_sub_employees list
		for key in manager_node.branches:
			self.list_sub_employees.append(key)
			self.get_sub_employees(manager_node.branches[key], manager_id)


		
	


	

tuplas = [[4,7],[1,5],[5,3],[7,3],[6,3],[2,5]]

instance = HrChart()
instance.built(tuplas)


print('---------')
employee1 = 5
employee2 = 2
print('Empleado: ', employee2)
print('Reporta a: ', employee1, '?')
print(instance.is_manager(employee1,employee2))

print('---------')
employee1 = 5
employee2 = 4
print('Empleado: ', employee2)
print('Reporta directo o indirecto a: ', employee1, '?')
instance.is_in_management_chain(None, employee1,employee2)
print(instance.is_in_chain)


print('---------')
employee1 = 3
print('Sub Empleados de: ', employee1)
instance.get_sub_employees(None, employee1)
print(instance.list_sub_employees)