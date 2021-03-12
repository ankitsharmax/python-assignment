while True:  
    try: 
        budget = float(input("Enter Your budget : "))
        temp_budget = budget  
    except ValueError: 
        print("ENTER A VALID AMOUNT.") 
        continue
    else: 
        break

a ={"name":[], "quantity":[], "price":[]} 
 
b = list(a.values()) 

names = b[0] 
quantities = b[1] 
prices = b[2] 

while True: 
	try: 
		choice = int(input("1.Add an item\n2.Exit\nEnter your choice : ")) 
	except ValueError: 
		print("\nERROR: PLEASE ENTER A VALID CHOICE.") 
		continue
	else: 
		if choice == 1 and temp_budget>0:
			productName = input("\n\nEnter product : ")
			productQuant = input("Enter quantity : ") 
			productPrice = float(input("Enter Price : ")) 

			if productPrice > temp_budget: 
				print("\nCan't Buy the product  ###(because budget left is {})\n\n".format(int(temp_budget))) 
				continue
			else: 
				if productName in names:  
					ind = names.index(productName) 
					quantities.remove(quantities[ind]) 
					prices.remove(prices[ind]) 
					quantities.insert(ind, productQuant) 
					prices.insert(ind, productPrice) 
					temp_budget = budget-sum(prices) 
					print("\nAmount left : {}\n".format(int(temp_budget))) 
				else: 
					names.append(productName) 
					quantities.append(productQuant)
					prices.append(productPrice)	 

					temp_budget = budget-sum(prices) 

					print("\nAmount left : {}\n".format(int(temp_budget))) 

		# If budget goes zero 
		elif temp_budget<= 0: 
			print("\nNO BUDGET") 
		else: 
			break

 
print("\nAmount left : {}\n".format(int(temp_budget))) 

if temp_budget in prices: 
	print("\nAmount left can buy you ", names[prices.index(temp_budget)]) 

print("\n\nGROCERY LIST is:")
print("Product name\t Quantity\tPrice")
for i in range(len(names)): 
	print("{:<16} {:<15} {}".format(names[i],quantities[i],int(prices[i]))) 
