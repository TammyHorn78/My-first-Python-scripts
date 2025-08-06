from functools import reduce

def compute_average_from_file(filename):
    """
    Computes the average of numbers in a text file using higher-order functions.

    Args:
        filename (str): The name of the text file containing numbers.
                        Each number should be on a separate line.

    Returns:
        float: The average of the numbers in the file.
               Returns 0 if the file is empty or contains no valid numbers.
    """
    try:
        with open(filename, 'r') as file:  # Use 'with' for automatic file closing
            # Read lines and convert to floats using map()
            # filter out empty strings in case of empty lines
            # map(float, ...) applies the float conversion to each item
            numbers = list(map(float, filter(lambda x: x.strip(), file.readlines()))) 
            
            if not numbers:
                return 0.0  # Handle empty file or no valid numbers

            # Calculate sum using reduce()
            # reduce(lambda x, y: x + y, ...) cumulatively applies the sum operation
            total_sum = reduce(lambda x, y: x + y, numbers)  

            return total_sum / len(numbers)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0.0  # Or raise an exception, depending on desired error handling
    except ValueError:
        print(f"Error: File '{filename}' contains non-numeric data.")
        return 0.0  # Or raise an exception

if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    average = compute_average_from_file(file_name)

    if average != 0.0: # Check if a valid average was computed
        print(f"The average of the numbers in '{file_name}' is: {average}")
