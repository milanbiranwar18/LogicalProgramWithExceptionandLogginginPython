# Program for prime number
import logging

logging.basicConfig(filename="prime_number.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def prime_num(first, last):
    """
       function to find prime number exception and logging
       :param first: using parameter 'first' to take first input
       :param last: using parameter 'last' to take second input
       :return: return all prime number between given range
      """
    try:
        for i in range(first, last + 1):
                num = 0
                for j in range(2, i):
                    if (i % j == 0):
                        num = 1
                    break
                if (num == 0):
                    print(i)


    except NameError as c:
        print("Some variable not defined")
        logging.exception(c)

    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    try:
        first = int(input("Enter a number from where you wanna start to check that it's prime or not"))
        last = int(input("Enter a number till you wanna check that it's prime or not"))
        prime_num(first, last)
    except ValueError:
        logging.error("Enter a number")

