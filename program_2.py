# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

##
# Program 2: Random Number File Writer
# Grant Dresser
# 10/31/2025
##

import random

def main():
    write_random_numbers()

def write_random_numbers():
    try:
        amount = int(input('How many random numbers do you want to be written in the file (1-1000)? '))
        if amount < 1 or amount >1000:
            print ("Error: Please enter a number between 1 and 1000. ")
            return 
    
        with open('random_numbers.txt', 'w') as file:
            for _ in range(amount):
                number = random.randint(1, 500)
                file.write(str(number) + '\n')

        print (f'{amount} random numbers have been written to random_numbers.txt')
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")
    except ValueError:
        print("Error: One or more lines in the file are not valid integers.")
    except IOError:
        print("Error: A problem occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

main()



