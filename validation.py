from bankomat_management import CLIENT_LIST, CLIENT_OPTIONS
from ui import take_user_name, take_user_pin
from database import withdrawal_operation, pay_in_operation, balance_operation
from typing import Tuple


def validate_user_name() -> Tuple[bool, int]:
    index_name = 0
    valide_name = False
    valide_name_index = (valide_name, index_name)
    name = take_user_name()
    for i in range(len(CLIENT_LIST)):
        if name in CLIENT_LIST[i]:
            print('OK')
            valide_name = True
            index_name = i
            valide_name_index = (valide_name, index_name)
    return valide_name_index


def validate_user_pin(index_p: int) -> bool:
    correct_pin = False
    for pin_try in range(3):
        pin = take_user_pin()
        if CLIENT_LIST[index_p][1] == pin:
            correct_pin = True
            print('OK')
            return correct_pin
        else:
            print('Incorrect Pin! Please try again')
    return correct_pin


def is_user_option_menu_input_valid(user_option_input: str) -> bool:
    if not user_option_input.isdigit():
        return False
    user_option_input_num = int(user_option_input)
    # print(CLIENT_OPTIONS[user_option_input_num])
    if user_option_input_num <= 0 or user_option_input_num >= len(CLIENT_OPTIONS) + 1:
        return False
    print(CLIENT_OPTIONS[user_option_input_num - 1])
    return True


def map_user_input(select_option: int, correct_name_index: int):
    print('Selected user option')
    if select_option == 1:
        withdrawal_operation(correct_name_index)
    elif select_option == 2:
        pay_in_operation(correct_name_index)
    elif select_option == 3:
        balance_operation(correct_name_index)
    else:
        raise RuntimeError(f"Unknown option {select_option}")


def print_inventory():
    for i, user_data in enumerate(CLIENT_LIST, start=1):
        print(f"{i} {user_data}")
