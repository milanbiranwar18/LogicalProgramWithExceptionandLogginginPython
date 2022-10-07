# Program for larger number
import logging

logging.basicConfig(filename="larger_num.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def larger_num(num1, num2, num3):
    """
      function to find larger number from 3 numbers
      :param num1: using parameter 'num' as a int datatype to take first number
      :param num2: using parameter 'num' as a int datatype to take second number
      :param num3: using parameter 'num' as a int datatype to take third number
      :return: return larger number from 3 numbers
    """
    try:
        if num1 > num2:
            print(num1, "is larger")
        elif num2 > num3:
            print(num2, "is larger")
        else:
            print(num3, "is larger")


    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))
        num3 = int(input("Enter third number"))
        larger_num(num1, num2, num3)
    except ValueError:
        logging.error("Please enter number only")
