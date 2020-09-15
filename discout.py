class Item:
	def fruit(self):
		f=int(input('enter price '))
		f1=f-(f//5)
		print(f1)
	def veggies(self):
		v=int(input('enter price '))
		v1=v-(v//5)
		print(v1)
	def meds(self):
		m=int(input('enter price '))
		m1=m-(m//5)
		print(m1)
	def spw(self):
		s=int(input('enter price '))
		s1=s-(s//5)
		print(s1)
	def food(self):
		fo=int(input('enter price '))
		f01=f0-(f0//5)
		print(f01)
	def total(self):
		t=(f-f1)+(v-v1)+(m-m1)+(s-s1)+(fo-fo1)
		print(t)

	def set(self):
		i=eval(input("enter 1- fruit. 2-veggies. 3-Meds. 4-Sports wear. 5-food item"))
		if i==1:
			fruit()
		elif i==2:
			veggies()
		elif i==3:
			meds()
		elif i==4:
			spw()
		elif i==5:
			food()
		else:
			print('invailid ')
		total()
a=Item()
a.set()
a.fruit()
a.veggies()
a.meds()
a.spw()
a.food()
a.total()