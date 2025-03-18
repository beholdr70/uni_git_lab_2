def some_main_func(string: str):
    print(f'this is main function: {some_main_func_dependency(string)}')

def some_main_func_dependency(string: str):
    return string[::-1]

if __name__ == '__main__':
    some_main_func('Hello, World!')