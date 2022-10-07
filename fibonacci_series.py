# Program for fibonacci series

import logging

logging.basicConfig(filename="fibonacci_series.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def fibonacci_series(num):
    """
      function to calculate fibonacci series with exception and logging
      :param num: using parameter 'num' as a int datatype to take a number from user
      :return: fibonacci series of given user input or number
    """

    a = 0
    b = 1
    try:
        for i in range(1, num):
            c = a + b
            print(c)
            a = b
            b = c

    except NameError:
        logging.error("Invalid varible")
    except Exception as Argument:
        logging.exception("invalid input")


if __name__ == '__main__':
    try:
        num = int(input("Enter a number to calculate fibonacci series"))
        fibonacci_series(num)
    except ValueError:
        logging.error("Please enter valid input")
