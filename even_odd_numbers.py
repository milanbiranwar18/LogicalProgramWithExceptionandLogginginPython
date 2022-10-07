import logging

logging.basicConfig(filename="odd_even.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def even_odd_num(num):
    """
    function to check that number is even or odd with exception and logging
    :param num: using parameter 'num' as a int datatype
    :return: Number given by user is even or odd
   """
    try:
        if num % 2 == 0:
            print(num, "is a even number")

        else:
            print(num, "is a odd number")


    except:
        logging.error("invalid input")
'''
    else:
        print("Everything looks like fine")
        # logging.info("Everything looks like good")

    finally:
        print("Program executed successfully")
        # logging.debug("Program executed successfully")
'''

if __name__ == '__main__':
    try:
        num = int(input("Enter a number to check it is even or odd"))
        even_odd_num(num)
        # print(even_odd_num.__doc__)
    except ValueError:
        logging.error("Enter a number")



'''
def even_odd_num(num):

        try:
            #if num%0 == 0:
            if num % 2 == 0:
                print(num, "is a even number")
            else:
                print(num, "is a odd number")

        #except ZeroDivisionError:
            #print("Division by zero not allowed")
        # except ZeroDivisionError as obj:
        # print(obj)

        except:
            print("something went wrong")

        else:
            print("Everything looks like good")

        finally:
            print("Program executed successfully")


if __name__ == '__main__':
        num = int(input("Enter a number to check it is even or odd"))
        even_odd_num(num)
        
        '''

'''
logging.basicConfig(filename="odd_even.txt", #.log
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def even_odd_num(num):
        if num%2 == 0:
            logging.info("is even number")
        #elif num%2 ==1:
            #logging.info("is a odd number")
        else:
            logging.info("is a odd number")
            #logging.error("Enter valid value")


if __name__ == '__main__':
    num = int(input("Enter a number to check it is even or odd"))
    even_odd_num(num)
'''
