def some_database_func():
    phrase = 'This func call from database file' if __name__ == '__main__' else 'This func call from outside of database file'
    print(f'This is some database function: {phrase}')


if __name__ == '__main__':
    some_database_func()
