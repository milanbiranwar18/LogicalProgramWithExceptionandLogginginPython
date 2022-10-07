# Program for harmonic number
import logging

logging.basicConfig(filename="harmonic.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def harmonic_num(n):
    """
        function to calculate harmonic number with exception and logging
        :param n: using parameter 'n' as a int datatype to calculate harmonic number
        :return: harmonic series and sum of harmonic series
    """
    num = 0
    try:
        for x in range(1, n + 1):
            print(f'1/{x}')
            # print(1/x)
            num = num + (1 / x)

        print("Sum of Series upto terms", n, "is", num)


    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        n = int(input("Enter a number"))
        harmonic_num(n)
    except ValueError:
        logging.error("Invalid input, Please enter number")
