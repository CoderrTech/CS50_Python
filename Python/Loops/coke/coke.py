def main():
    
    amount = 50
    print(f"Amount due: {amount}")
    accepted_coins = [5, 10, 25]
    while amount > 0:

        coins = int(input("Insert Coin: "))

        if coins in accepted_coins:
            amount -= coins 
            if amount > 0:
                print(f"Amount due: {amount}")
            else:
                print("Change owed:", abs(amount))


        else:
            print(f"Amount due: {amount}")
        

main()
