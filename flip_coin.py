import logging
import random

logging.basicConfig(filename="flip_coin.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def flip_coin(flips):
    """
       function for flip coin program and to calculate head and tail percentage with exception and logging
       :param flips: using parameter 'flips' as a int datatype to take user input for how many times user wants to flip a coin
       :return: calculating head tail count and head tail percentage
    """

    headCount = 0
    tailcount = 0
    headpercentage = 0
    tailpercentage = 0

    try:
        for i in range(flips):
            # num=int(input("Enter 1 for Tail or 2 for Head"))
            num = random.randint(1, 2)
            if num == 1:
                print("Tail")
                tailcount = tailcount + 1
            else:
                print("Head")
                headCount = headCount + 1

        headpercentage = (headCount * 100) / flips
        tailpercentage = (tailcount * 100) / flips

        print("HeadPercentage is ", headpercentage)
        print("TailPercentage is ", tailpercentage)


    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        flips = int(input("Enter the number of flips"))
        flip_coin(flips)
    except ValueError:
        logging.error("Invalide input, Please enter valid numeric value only")

