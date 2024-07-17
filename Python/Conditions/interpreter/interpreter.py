def main():
    x, y, z = input("Expression: ").split()
    x = int(x)
    z = int(z)

    if y == '+':
        return to_float(x + z)
    elif y == '-':
        return to_float(x - z)
    elif y == '*':
        return to_float(x * z)
    elif y == '/':
        return to_float(x / z)
    
    else:
        print("type in valid expression")
        


def to_float(n):

    n_float = float(n) 
    print(f"{n_float:.1f}")
    return

main()
