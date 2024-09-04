# ***********************************************
# if __name__ == '__main__':
# ***********************************************

# why?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found whithin __main__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# def hello():
#     print("Hello World")

# if __name__ == '__main__':
#     hello()

def main():
    print("Hello World")

if __name__ == '__main__':
    main()