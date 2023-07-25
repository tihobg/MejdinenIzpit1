from ui import user_name_input, take_user_option, user_options_list
from validation import validate_user_name, validate_user_pin, is_user_option_menu_input_valid, map_user_input, \
    print_inventory

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Valid User Names')
    user_name_input()
    correct_name = validate_user_name()
    if not correct_name:
        print('There is no such a client')
        exit()
    correct_p = validate_user_pin(correct_name[1])
    print(correct_name[1])
    if not correct_p:
        print('Your card has been blocked')
        exit()
    user_options_list()
    option_input = take_user_option()
    print(correct_name[1])
    if is_user_option_menu_input_valid(option_input):
        map_user_input(int(option_input), correct_name[1])
        print(f"User chose {option_input}")
    else:
        print('Wrong option')

    # print_inventory()
