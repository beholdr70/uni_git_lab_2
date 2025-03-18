from api_file import some_api_func
from auth_file import some_auth_func
from database_file import some_database_func


def some_main_func(string: str):
    print(f'this is main function: {some_main_func_dependency(string)}')

def some_main_func_dependency(string: str):
    return string[::-1]

if __name__ == '__main__':
    some_api_func('test string')
    some_main_func('Hello, World!')

    #auth_file test
    some_auth_func('Username', "12324341")
    some_database_func()