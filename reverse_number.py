import logging

logging.basicConfig(filename="reverse_number.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def reverse_num(num):
    """
    function to reverse a number with exception and logging
    :param num: using parameter 'num' to take number from user
    :return: return reverse of given number
    """
    result = 0
    try:
        while num != 0:
            rem = num % 10
            result = result * 10 + rem
            num = num // 10
        print(result)


    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        num = int(input("Enter number to reverse"))
        reverse_num(num)
    except ValueError:
        logging.error("Enter a numeric value")
