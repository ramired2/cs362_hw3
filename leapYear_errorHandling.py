msg = "Please enter a year: "
# year = input(msg)


while True:
    year = input(msg)

    if int(year) >= 0 and len(year) >= 4:
        if int(year) % 4 == 0:
            
            if int(year) % 100 == 0:
                if int(year) % 400 == 0:
                    print(year + " is a leap year")
                    break
                else:
                    print(year + " is not a leap year")
                    break
            else:
                print(year + " is a leap year")
                break

        else:
            print(year + " is not a leap year")
            break
