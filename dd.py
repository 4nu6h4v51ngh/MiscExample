class test:
	def input(self):
		self.salary=int(input('salary '))
		self.name=input('name ')
	def opr1(self):
		if self.salary>=100000:
			salary1=self.salary-(self.salary//20)
			print(salary1,self.name)
			self.sal1=self.salary-salary1
		elif self.salary<100000 and self.salary>=70000:
			salary2=self.salary-(self.salary//10)
			print(salary2,self.name)
			self.sal2=self.salary-salary2
		elif self.salary<70000 and self.salary>50000 :
			salary3=self.salary-(self.salary//5)
			print(salary3,self.name)
			self.sal3=self.salary-salary3
		elif self.salary<=50000:
			salary4=self.salary+(self.salary//20)
			print(salary4,self.name)
			self.sal4=self.salary-salary4
	def get(self):
		print(self.sal1+self.sal2+self.sal3+self.sal4)
s=test()
s.input()
s.opr1()
s.get()
