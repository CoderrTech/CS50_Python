def main():
    user_input = input("Input: ") 
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    result = ""

    for char in user_input:
        
        if char not in vowels:
            result += char
    
    print(f"Output: {result}")

main()
