def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    # check if the string has enough characters
    if is_enough_char(s):

        # Set a variable to track the first funded digit
        has_number = False
        
        # Loop over string characters
        for i in range(len(s)):
                
            # check if the current char is invalid or the char in index 0 is a digit
            if is_invalid_char(s[i]) or (i == 0 and is_number(s[i])):
                return False

            # set the has_number to true if the current char is digit 
            if is_number(s[i]):
                has_number = True

                # check if all remaining characters are digits.
                if not s[i:].isdigit():
                    return False

        return has_number
    
    # return false if the str does not have enough characters
    else:
        return False

# check for invalid characters
def is_invalid_char(c):
    invalid_char = [" ", ",", "." "%", "/", "!"]
    return c in invalid_char

# check for enough characters
def is_enough_char(str):
    return 2 <= len(str) <= 6

# check if a given char is a digit
def is_number(c):
    return c.isdigit()

main()
