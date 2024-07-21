def main():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
        
            x, y = int(x), int(y)
            if  x <= y and y != 0:
                frc = (x / y) * 100

                if frc >= 99:
                    print("F")
                elif frc <= 1:
                    print("E")
                else:
                    print(f"{frc: .0f}%")
                break
        
        except (ValueError, ZeroDivisionError):
            print("error")
      

main()
