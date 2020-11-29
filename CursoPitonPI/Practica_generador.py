def generapares(limite):

	num=1
	
	while num<limite:

		yield num*2

		num+=1
devuelvepares=generapares(10)

print(next(devuelvepares))
print("Aqui iria mas codigo")
print(next(devuelvepares))
print("Aqui iria mas codigo")
print(next(devuelvepares))
print("Aqui iria mas codigo")
