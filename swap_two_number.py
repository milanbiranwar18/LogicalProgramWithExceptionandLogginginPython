import logging

logging.basicConfig(filename="swap_two_number.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def swap_two_num(a, b):
    """
       function for swapping the number with exception and logging
       :param a and b: using parameter 'a and b' to take number from user
       :return: return value of a in b and the value of b in a
    """
    try:
        c = a
        x = b
        y = c
        print("Before swaping value of a is ", a)
        print("Before swaping value of b is ", b)
        print("After swaping value of a is ", x)
        print("After swaping value of b is ", y)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        a = int(input("Enter number to swap"))
        b = int(input("Enter number to swap with another number"))
        swap_two_num(a, b)
    except ValueError:
        logging.error("Invalid input, please enter number only")
