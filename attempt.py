def mainmenu():
	print ('1. Add items to a list (Addition finishes upon typing code 999)')
	print ('2. Separate item based on New or Used status (need to add items first)')
	print ('3. Exit')
	selection=int(input('Select choice: '))
	if selection==1:
		list()
	elif selection==2:
		list2(list)
		lista_u,lista_n=list2(list)
		print ('Separated product type lists :')
		print ('Used items')
		print lista_u
		print ('New Items')
		print lista_n
		mainmenu()
	elif selection==3:
		quit()
mainmenu()

def list():
	
	lista = []
	code = raw_input('insert item id code')
	while code<>"999":
		description = raw_input('Insert item description')
		price_cost = raw_input('Insert the product cost')
		price_sell = raw_input('insert the selling price of the product')
		item_type = raw_input('Insert type of product (N if new or U if used): ')
		lista.append([code,description,price_cost,price_sell,item_type])
		
		code = raw_input('insert item id code')
	return lista

lista=list()
print ('Your current item list is the following : ')
print lista


def list2(list):
	lista_u = []
	lista_n = []
	for x in lista:
		if x[4] == "U":
			lista_u.append(x)
		
		elif x[4] == "N":	
			lista_n.append(x)
		return lista_u,lista_n





mainmenu()
			
