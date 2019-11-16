def info():
	lista=[]
	codigo=raw_input('Insert the product code: ')
	while codigo<>"999":
		descripcion=raw_input('Insert the product description: ')
		precio_c=input('Insert the product cost: ')
		precio_v=input('Insert the selling price of the product: ')
		tipo=raw_input('Insert type of product (N if new or U if used): ')
		lista.append([codigo,descripcion,precio_c,precio_v,tipo])
		
		codigo=raw_input('Insert the product code: ')
		
	return lista
lista=info()
	

print ('Product management program')
print ('----------------------------')

task = raw_input ('Select the task you want to do by entering a number')

if task == 1:
	lista=info()

