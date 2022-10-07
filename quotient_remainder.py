import logging

logging.basicConfig(filename="quotient_remainder.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def quotient_remainder(num1, num2):
    """
     function for quotient and remainder with exception and logging
     :param num1: using parameter 'num1' to take number from user
     :param num2: using parameter 'num2' to take number from user
     :return: return Quotient and Remainder
     """
    try:
        quotient = num1 / num2
        remainder = num1 % num2
        print("Quotient is", quotient)
        print("Remainder is", remainder)

    except ZeroDivisionError as o:
        logging.error(o)
    except NameError as e:
        logging.error(e)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        num1 = int(input("Enter divident number"))
        num2 = int(input("Enter divisor number"))
        quotient_remainder(num1, num2)
    except ValueError:
        logging.error("Enter numeric value only")
