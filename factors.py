import logging

logging.basicConfig(filename="factor.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def factors(num, num1):
    """
    function to check that how many factors had a number with exception and logging
    :param num: using parameter 'num' as a int datatype to take a number from user to check it's factor
    :param num2: using parameter 'num2' as a int datatype to get range till what number user want's to check factors
    :return: Factors of a number till the range given by user
    """
    try:
        for i in range(1, num1):
            if num == 0:
                if num % i == 0:
                    print(i)

    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        num = int(input("Enter a number to check it's factor"))
        num1 = int(input("Enter range till which number you want factor"))
        factors(num, num1)
    except ValueError:
        logging.error("Wrong input, enter numeric value only")