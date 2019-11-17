def mainmenu():
	print ('1. Add items to a list')
	print ('2. Separate item based on New or Used status')
	print ('3. Exit')
	selection=int(input('Select choice: '))
	if selection==1:
		list()
	elif selection==2:
			list2()
	elif selection==3:
		quit()
mainmenu()

def list():
	
	lista=[]
	code=raw_input('insert item id code')
	while code<>"999":
		description=raw_input('Insert item description')
		price_cost=raw_input('Insert the product cost')
		price_sell=raw_input('insert the selling price of the product')
		item_type=raw_input('Insert type of product (N if new or U if used): ')
		lista.append([code,description,price_cost,price_sell,item_type])
		
		code=raw_input('insert item id code')
	return lista

lista=list()

print lista

mainmenu()
