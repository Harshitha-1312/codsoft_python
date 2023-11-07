def sum(a,b):
	return (a+b)
def difference(a,b):
	return (a-b)
def product(a,b):
	return (a*b)
def quotient(a,b):
	return (a/b)
flag=True
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
while flag:
	print("1.ADDITION")
	print("2.SUBTRACTION")
	print("3.MULTIPLICATION")
	print("4.DIVISION")
	print("5.EXIT")
	ch=int(input("Enter choice: "))
	if ch==1:
		print(sum(a,b))
	elif ch==2:
		print(difference(a,b))
	elif ch==3:
		print(product(a,b))
	elif ch==4:
		print(quotient(a,b))
	elif ch==5:
		flag=False
	else:
		print("Invalid choice")
