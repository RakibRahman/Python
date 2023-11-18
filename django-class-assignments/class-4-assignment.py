store = list()

while True:
    operation = str(input('Chose Operation: \n 1 - CREATE\n 2 - READ\n 3 - UPDATE\n 4 - DELETE\n--->'))
    print(operation)
    if operation == '1' or operation == 'CREATE':
        value = input('Enter Value: ')
        store.append(value)
        print(store)

    if operation == '2' or operation == 'READ':
        print(store)

    if operation == '3' or operation == 'UPDATE':
        currentValue = input('Enter Current Value: ')
        if currentValue in store:
            index = store.index(currentValue)
            updateValue = input('Enter Update value: ')
            store[index] = updateValue
        else:
            print('Invalid value')

    if operation == '4' or operation == 'DELETE':
        value = input('Enter Value: ')
        store.remove(value)
        print('delete opt')

