def tens():
	list=[1,2,3,4,5,6,7,8,9]

	for x in list:
		tens=(x*10)
		print(tens)


def list():
	
	square=[number*number for number in range(10)]
	print(square)


def sort():
	a=[9,1,4,7,3]
	b=[5,2,6,8,0]
	c=[]
	c=a+b
	c.sort()
	print(c)


def range_sum(n):
	range_sum=range(1,n+1)
	total_sum=sum(range_sum)
	print (total_sum)


def largest():
	list=[1,3,6,8,2,4,5.7]
	print(max(list))	


def smallest():
	list=[1,3,6,8,2,4,5.7]
	print(min(list))


def my_modulus():
	a=dict()
	numbers=range(10,20)
	for number in numbers:
		a[number]=number%3
		print(a)


def students():
	Student1={"balance":1000,"name":"Irene"}
	Student2={"balance":2000,"name":"Pauline"}
	Student3={"balance":3000,"name":"Naima"}
	Student4={"balance":1000,"name":"Rose"}
	Students=[Student1,Student2,Student3,Student4]
	
	for Student in Students:
		print("Hello {},your balance is {}.".format(Student["name"],Student["balance"]))