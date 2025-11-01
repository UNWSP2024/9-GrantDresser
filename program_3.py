# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
def sum_numbers_from_file():
    try: 
        total = 0
        count = 0

        with open('numbers.txt', 'r') as file:
            for line in file:
                line = line.strip() 
                if not line:
                    continue

                number = int(line)
                total += number
                count += 1

            if count == 0:
                print ('The file has no numbers to average.')
            else:
                average = total / count
                print(f'The total of the numbers: {total}')
                print(f'The average of the numbers: {average:.2f}')
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' was not found.")
    except ValueError:
        print("Error: One or more lines in the file are not valid integers.")
    except IOError:
        print("Error: A problem occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()