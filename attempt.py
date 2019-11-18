def get_options():
  print ('1. Add items to a list (Addition finishes upon typing code 999)')

  print ('2. Separate item based on New or Used status (need to add items first)')
  
  print ('3. Show current list')

  print ('4. Exit')
  return int(input('Select choice: '))

def mainmenu():
  _add_item = 1
  _separate_items = 2
  _print_current_list = 3
  _exit = 4
  current_list = []
  used_list = []
  new_list = []
  selection = get_options()
  while selection!=_exit:
    if selection == _add_item:
      current_list = add_to_list()
    elif selection== _separate_items:
      used_list,new_list=item_type(current_list)
      print ('Separated product type lists :')
      print ('Used items')
      print used_list
      print ('New Items')
      print new_list
    elif selection== _print_current_list:
      _print_current_list = current_status(current_list)
    selection = get_options()

def add_to_list():
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

def item_type(list):
  lista_u = []
  lista_n = []
  for x in list:
    if x[4] == 'U':
      lista_u.append(x)
    if x[4] == 'N':	
      lista_n.append(x)
  return [lista_n,lista_u]

def current_status(lista):
  print ('Your current item list is the following : ')
  print lista

##########################
# Main code below here :)
##########################

mainmenu()
