import logging

logging.basicConfig(filename="vowel_consonant.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def vowel_consonant(char):
    """
        function to check vowel or consonant with exception and logging
        :param char: using parameter 'char' to take alphabet from user
        :return: return vowel or consonant
    """

    try:
        if (
                char == 'A' or char == 'a' or char == 'E' or char == 'e' or char == 'I' or char == 'i' or char == 'O' or char == 'o' or char == 'U' or char == 'u'):
            print(char, "is a vowel")
        else:
            print(char, "is a consonant")


    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    try:
        char = input("Enter any alphabet ")
        vowel_consonant(char)
    except ValueError:
        logging.error("Please enter alphabet only")
