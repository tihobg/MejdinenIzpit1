from bankomat_management import CLIENT_LIST
# new_balance_data = []


def withdrawal_operation(index_name: int):
    balance_index = False

    while not balance_index:
        withdrawal_amount = int(input('Please enter withdrawal amount:\n'))
        if withdrawal_amount <= CLIENT_LIST[index_name][2]:
            balance = CLIENT_LIST[index_name][2] - withdrawal_amount
            print(f"New balance is: {balance}")
            balance_index = True
        else:
            print('There is not enough money! Please try again')


def pay_in_operation(index_name: int):
    pay_in_amount = int(input('Please enter pay in amount:\n'))
    balance = CLIENT_LIST[index_name][2] + pay_in_amount
    # new_balance_data.append(CLIENT_LIST[index_name][0])
    # new_balance_data.append(CLIENT_LIST[index_name][1])
    # new_balance_data.append(balance)
    
    # print('New balance')
    # print(new_balance_data)
    print(f"New balance is: {balance}")


def balance_operation(index_name: int):
    print(f"The balance is: {CLIENT_LIST[index_name][2]}")
