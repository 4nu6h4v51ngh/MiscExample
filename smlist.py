list=[10,1,3,2,7]
list.sort()
l=[]
l1=min(list)
for i in list:
	if i==l1:
		i=l1
	l.append(l1)
list=l
print(l)