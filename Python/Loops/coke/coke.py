def main():
    amount = 50
    print(f"Amount due: {amount}")
    while True:
        coins = input("Insert Coin: ")

        if coins == 5 or coins == 10 or coins == 25:
            amount_due = 50 - coins
            print(f"Amount due: {amount_due}")


            
        coins = input("Insert Coin: ")

main()
