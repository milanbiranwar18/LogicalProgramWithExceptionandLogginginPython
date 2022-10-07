# Program for power of 2
import logging

logging.basicConfig(filename="power_of_2.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def power_of_2(number):
    """
      function to calculate power of 2 with exception and logging
      :param number: using parameter 'number' to take number from user
       :return: return power of 2
    """

    num = 1
    try:
        for i in range(number):
                num = num * 2
                print(num)

    except NameError as b:
        logging.error(b)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        number = int(input("Enter the number"))
        power_of_2(number)
    except ValueError:
        logging.error("Please enter numeric value")

