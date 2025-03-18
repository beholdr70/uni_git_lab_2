def some_database_func():
    phrase = 'This func called from database file' if __name__ == '__main__' else 'This func called from outside of database file'
    print(f'This is some database function: {phrase}')
    if __name__ != '__main__':
        print(f'The end of database function')


if __name__ == '__main__':
    some_database_func()
