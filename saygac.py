while True:

	bill = 0.0

	def result(bill):
		print("Amount billed: $", end='')
		print(bill,'\n')

	def residential(used):
		bill = 5 + used*0.0005
		result(bill)

	def commercial(used):
		if used <= 4000000:
			bill = 1000
			result(bill)
		else:
			bill = 1000 + (used-4000000)*0.00025
			result(bill)
		
	def industrial(used):
		if used <= 4000000:
			bill = 1000
			result(bill)
		elif used <= 10000000:
			bill = 2000
			result(bill)
		else:
			bill = 2000 + (used-10000000)*0.00025
			result(bill)

	category = input("Enter customer code: ").lower()
	if (category == 'q'):
		break
	elif (category == 'r' or category == 'c' or category == 'i'):
		customer = category
	else:
		print("Wrong code!\n")
		continue

	begin = int(input('Beginning meter reading: '))
	end = int(input('Ending meter reading: '))

	if ( end >= begin ):
		used = (end-begin)/10
	else:
		used = (999999999 - begin + end)/10

	print("Gallons of water used:", used)

	if (customer == 'r'):
		residential(used)
	elif (customer == 'c'):
		commercial(used)
	else:
		industrial(used)
	
	option = input("Do you want to use again? [y,n]")
	if option == 'n':
		break
		
