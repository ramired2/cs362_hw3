msg = "Please enter a year: "
# year = input(msg)


while True:
    year = input(msg)
    
    try:
        yr = int(year)
        # int(year) >= 0
        # break
    except ValueError:
        print("That was not a valid input. Please enter a numeric value.\n")
        continue

    else:
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
        else:
            print("That was not a valid input. A year must be a positive number of at least four values.\n")
