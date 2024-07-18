def main():
    # ask the user for the camelCase variable
    camel_case = input("camelCase: ")
    snake_case = to_snake_case(camel_case)

    print(f"snake_case: {snake_case}")

def to_snake_case(str):
    result = ""
    for c in str:
        
        if c.isupper():
            result += "_" + c.lower()
        else:
            result += c
    return result        

main()

