import logging

logging.basicConfig(filename="leap_year.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def leap_year(year):
    """
       function to calculate leap year with exception and logging
       :param year: using parameter 'year' to take year from user to check it is leap year or not
       :return: return leap year
      """
    try:
        if ((year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0))):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")


    except Exception as e:
        logging.exception(e)

if __name__ == '__main__':
    try:
        year = int(input("Enter year to check it is leap year or not"))
        leap_year(year)
    except ValueError:
        logging.error("Enter valid year")

