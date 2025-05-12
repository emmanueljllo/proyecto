#Variables globales
list = []

#Create a function main
def main():
    menu()

#Create a function that asks the user if they want to continue    
def exit_():
    print("\n")
    #Validate the option to consult
    validate = True
    while validate:
        print('-'*30)
        option = input('¿Desea continuar? (s/n): ')
        optionFinal = option.lower()
        if optionFinal == 's': #If the opcion is 's' show the menu
            menu()
        elif optionFinal == 'n': #If the opcion is 'n' exit the program
            print('Saliendo...')
            print('-'*30)
            exit()
        else:
            print('Opcion no valida') #If the opcion is not 's' or 'n' ask again
            exit_()
        break

#Create a function that shows the menu
def menu():
    print('-'*20)
    print('GESTION DE INVENTARIO')
    print('-'*20)
    print('Opciones:')
    print('-'*20)
    print('1. Añadir producto')
    print('2. Buscar producto')
    print('3. Actualizar producto')
    print('4. Eliminar producto')
    print('5. Calcular valor total del inventario')
    print('6. Mostrar inventario')
    print('7. Salir')
    print('-'*20)
    option = (input('Ingrese una opcion: '))
    print('-'*20)
    validate = True
    while validate:
        match option:
            case '1': #if the opcion is '1' call the function add
                add()
            case '2':
                search() #if the opcion is '2' call the function search
            case '3':
                update() #if the opcion is '3' call the function update
            case '4':
                delete() #if the opcion is '4' call the function delete
            case '5':
                total_value() #if the opcion is '5' call the function total_value
            case '6':
                show() #if the opcion is '6' call the function show
            case '7':
                print('Seguro que desea salir?') 
                exit_() #If the opcion is '7' call the function exit
            case _:
                print('-'*20)
                print('Opcion no valida') #if the opcion is not valid ask again
                print('-'*20)
                main()
                break
        break
    print('-'*20)

#Create a function that adds a product to a list of products    
def add(name:str='',price:float=0,quantity:int=0):
    validate = True
    while validate:
        print('REGISTRAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto: ') 
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto: ')
        else: #If the name is valid break the loop
            validate = False
        break
    
    validate = True
    while validate:
        price = input('Ingrese el precio del producto: ')
        if price == '': #validate the price is not empty, if it is empty ask again
            print('Precio no puede estar vacio')
            price = input('Ingrese el precio del producto: ')
        elif not price.isnumeric(): #validate the price is number, if it is not a number ask again
            print('Precio solo puede contener numeros')
            price = input('Ingrese el precio del producto: ')
        elif float(price) < 0: #validate the price is not negative, if it is negative ask again
            print('Precio no puede ser negativo')
            price = input('Ingrese el precio del producto: ')
        else: #If the price is valid break the loop
            validate = False
        break

    validate = True
    while validate:
        quantity = input('Ingrese la cantidad del producto: ')
        if quantity == '': #validate the quantity is not empty, if it is empty ask again
            print('Cantidad no puede estar vacio')
            quantity = input('Ingrese la cantidad del producto: ')
        elif not quantity.isnumeric(): #validate the quantity is number, if it is not a number ask again
            print('Cantidad solo puede contener numeros')
            quantity = input('Ingrese la cantidad del producto: ')
        elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
            print('Cantidad no puede ser negativa')
            quantity = input('Ingrese la cantidad del producto: ')
        else: #If the quantity is valid break the loop
            validate = False 
        break

    tupla = (float(price), int(quantity)) #create a tuple with the price and quantity
    #create a dictionary with the name, price and quantity
    dict = {
        'name': name,
        'price':tupla[0],
        'quantity': tupla[1]
    }
    list.append(dict) #add the dictionary to the list
    print('-'*20)
    print(f"Producto agregado: {name}, Precio: {tupla[0]}, Cantidad: {tupla[1]}")
    
    exit_()

    return list

#Create a function that searches for a product in the list of products
def search():
    validate = True
    while validate:
        print('-'*20)
        print('BUSCAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto a buscar: ')
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto a buscar: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto a buscar: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto a buscar: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto a buscar: ')
        else: #If the name is valid break the loop
            validate = False
        break

    for i in list: #search for the product in the list
        if i['name'] == name: 
            print(f"Producto encontrado: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}")
            exit_()
            break
    else: #If the product is not found in the list
        print('Producto no encontrado')
    exit_()
        
    return list

#Create a function that updates a product in the list of products
def update():
    validate = True
    while validate:
        print('-'*20)
        print('ACTUALIZAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto a actualizar: ')
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto a actualizar: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto a actualizar: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto a actualizar: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto a actualizar: ')
        else: #If the name is valid break the loop
            validate = False
        break

    for i in list: #search for the product in the list
        if i['name'] == name:
            print(f"Producto encontrado: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}")
            validate = True
            while validate:
                price = input('Ingrese el nuevo precio del producto: ')
                if price == '': #validate the price is not empty, if it is empty ask again
                    print('Precio no puede estar vacio')
                    price = input('Ingrese el nuevo precio del producto: ')
                elif not price.isnumeric(): #validate the price is number, if it is not a number ask again
                    print('Precio solo puede contener numeros')
                    price = input('Ingrese el nuevo precio del producto: ')
                elif float(price) < 0: #validate the price is not negative, if it is negative ask again
                    print('Precio no puede ser negativo')
                    price = input('Ingrese el nuevo precio del producto: ')
                else: #If the price is valid break the loop
                    price = float(price)
                    validate = False
                break

            validate = True
            while validate:
                quantity = input('Ingrese la nueva cantidad del producto: ')
                if quantity == '': #validate the quantity is not empty, if it is empty ask again
                    print('Cantidad no puede estar vacio')
                    quantity = input('Ingrese la nueva cantidad del producto: ')
                elif not quantity.isnumeric(): #validate the quantity is number, if it is not a number ask again
                    print('Cantidad solo puede contener numeros')
                    quantity = input('Ingrese la nueva cantidad del producto: ')
                elif int(quantity) < 0: #validate the quantity is not negative, if it is negative ask again
                    print('Cantidad no puede ser negativa')
                    quantity = input('Ingrese la nueva cantidad del producto: ')
                else: #If the quantity is valid break the loop
                    quantity = int(quantity)
                    validate = False
                break

            print(f"Producto actualizado: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}")
            
            exit_()
            break

#create a function that deletes a product from the list of products
def delete():
    validate = True
    while validate:
        print('-'*20)
        print('ELIMINAR PRODUCTO')
        print('-'*20)
        name = input('Ingrese el nombre del producto a eliminar: ')
        if name == '': #validate the name is not empty, if it is empty ask again
            print('Nombre no puede estar vacio')
            name = input('Ingrese el nombre del producto a eliminar: ')
        elif not name.isalpha(): #validate the name is not a number, if it is a number ask again
            print('Nombre solo puede contener letras')
            name = input('Ingrese el nombre del producto a eliminar: ')
        elif len(name) < 3: #validate the name is not less than 3 characters, if it is less than 3 ask again
            print('Nombre debe tener al menos 3 caracteres')
            name = input('Ingrese el nombre del producto a eliminar: ')
        elif len(name) > 20: #validate the name is not more than 20 characters, if it is more than 20 ask again
            print('Nombre no puede tener mas de 20 caracteres')
            name = input('Ingrese el nombre del producto a eliminar: ')
        else: #If the name is valid break the loop
            validate = False
        break

    for i in list: #search for the product in the list
        if i['name'] == name:
            list.remove(i) #remove the product from the list
            print(f"Producto eliminado: {i['name']}")
            exit_()
            break
    else: #If the product is not found in the list
        print('Producto no encontrado')
    exit_()
        
    return list

#create a function that calculates the total value of the inventory
def total_value():
    total = 0
    for i in list: #calculate the total value of the inventory
        total += i['price'] * i['quantity'] #multiply the price by the quantity of each product
    print(f'El valor total del inventario es: {total}')
    exit_()
    return total

#create a function that shows the inventory
def show():
    if len(list) == 0: #validate the inventory is not empty, if it is empty show a message
        print('-'*20)
        print('Inventario vacio')
    else:
        print('-'*20)
        print('Inventario:')
        for i in list: #show the inventory
            print('-'*40)
            print(f"Nombre: {i['name']}, Precio: {i['price']}, Cantidad: {i['quantity']}\n")
    exit_()
    return list

#Call the main function
main()
