def convert(input_str):
    converted_str = input_str.replace(':)', '🙂').replace(':(', '🙁')

    return converted_str

def main():
    user_input = input(":> ")

    output = convert(user_input)

    print(output)

main()
