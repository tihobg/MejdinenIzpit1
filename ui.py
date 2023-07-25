from bankomat_management import CLIENT_LIST, CLIENT_OPTIONS


def user_name_input():

    for i, user_name in enumerate(CLIENT_LIST, start=1):
        print(f"{i} {user_name[0]}")


def take_user_name() -> str:
    name = input('Please, enter your name:\n')
    return name


def take_user_pin() -> int:
    pin = int(input('Please, enter your pin:\n'))
    return pin


def take_user_option() -> str:
    # user_options_list()
    user_option = input('What kind of operation do you want to select?\n')
    return user_option


def user_options_list():
    print('List with user options!')
    for i, user_option in enumerate(CLIENT_OPTIONS, start=1):
        print(f"{i} {user_option}")
