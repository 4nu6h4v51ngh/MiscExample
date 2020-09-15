def rec(n):
	if n==1:
		return n
	else:
		return n*rec(n-1)
num=int(input('Enter no'))
if num>0:
	print(rec(num))
elif num==0:
	print('1')
else:
	print('no fact exist')