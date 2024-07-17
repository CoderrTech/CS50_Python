def main():
    time = convert(input("What time is it? "))
    
    if time >= 7 and time <= 8:
        print("Breakfast time")
    elif time >= 12 and time <= 13:
        print("Lunch time")
    elif time >= 18 and time <= 19:
        print("Dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(':')
    
    hours = int(hours)
    minutes = int(minutes)

    time = hours + minutes / 60
    return time    




if __name__ == "__main__":
    main()

