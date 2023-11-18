store = list()

while True:
    operation = str(input('Chose Operation: \n 1 - CREATE\n 2 - READ\n 3 - UPDATE\n 4 - DELETE\nType "exit" to close program \n---> '))

    if operation == 'exit':
        print('Program exited')
        break
    if operation == '1' or operation.upper() == 'CREATE':
        value = input('Enter Value: ')
        store.append(value)
        print(value,' is added!')

    if operation == '2' or operation.upper() == 'READ':
        print('Your Information==>',store)

    if operation == '3' or operation.upper() == 'UPDATE':
        currentValue = input('Enter value you want to update: ')
        if currentValue in store:
            index = store.index(currentValue)
            updateValue = input('Enter Update value: ')
            store[index] = updateValue
            print('value is updated!')
        else:
            print('Value does not exist!')

    if operation == '4' or operation.upper() == 'DELETE':
        value = input('Enter Value you want to delete: ')
        store.remove(value)
        print('value deleted')

