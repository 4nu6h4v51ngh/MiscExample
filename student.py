class student:
	def get(self):
		self.name=input('enter name ')
		self.rno=int(input('enter rno '))
		self.ma1=int(input('enter marks1 '))
		self.ma2=int(input('enter marks2 '))
		self.ma3=int(input('enter marks3 '))
		self.ma4=int(input('enter marks4 '))
		self.ma5=int(input('enter marks5 '))
class stud:
	def show(self):
		a=student()
		a.get()
		print(a.name)
		print(a.rno)
		print(a.ma1)
		print(a.ma2)
		print(a.ma3)
		print(a.ma4)
		print(a.ma5)

b=stud()
b.show()
