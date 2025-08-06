"""
File: testinputfunctions.py

Defines a function for robust input of ints.
"""

def inputInt(prompt):
    """Guarantees that the user inputs an integer,
    using the given prompt. Returns the integer."""
    while True:
        theString = input(prompt)
        if theString.isdigit():
            return int(theString)
        else:
            print("Error: the input must only contain digits.")

def inputFloat(prompt):
    """This function repeatedly prompts the user for input until a valid
    floating-point number (digits only or digits and a single decimal point)
    is entered. It handles potential ValueError exceptions during conversion.
    """
    while True:
        try:
            value = input(prompt)
            # Check if the input string is valid for float conversion
            if all(c.isdigit() or c == '.' for c in value) and value.count('.') <= 1:
                return float(value)
            else:
                print("Invalid input. Please enter a valid floating-point number (e.g., 3.14 or 5).")
        except ValueError:
            print("Invalid input. Please enter a valid floating-point number (e.g., 3.14 or 5).")    
    
def main():
    n = inputInt("Please enter a number for intrger function: ")
    print(n)
    nfloat = inputFloat("Please enter a number for float function: ")
    print(nfloat)

if __name__ == "__main__":
    main()
