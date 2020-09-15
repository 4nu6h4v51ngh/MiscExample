class test:
	def input(self):
		self.salary=int(input('salary '))
		self.name=input('name ')
	def opr1(self):
		if self.salary>100000:
			salary1=self.salary-(self.salary//20)
			print(salary1,self.name)
#			self.sal1=salary1
		else:
			pass
	def opr2(self):
		if self.salary<100000 and self.salary>70000:
			salary2=self.salary-(self.salary//10)
			print(salary2,self.name)
#			self.sal2=salary2
		else:
			pass
	def opr3(self):
		if self.salary<70000 and self.salary>50000 :
			salary3=self.salary-(self.salary//5)
			print(salary3,self.name)
#			self.sal3=salary3
		else:
			pass
	def opr4(self):
		if self.salary<50000:
			salary4=self.salary+(self.salary//20)
			print(salary4,self.name)
#			self.sal4=salary4
		else:
			pass
#	def opr5(self):
#		print(self.sal1+self.sal2+self.sal3+self.sal4)
salary=test()
salary.input()
salary.opr1()
salary.opr2()
salary.opr3()
salary.opr4()
#salary.opr5()