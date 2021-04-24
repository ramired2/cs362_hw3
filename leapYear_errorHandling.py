msg = "Please enter a year: "


while True:
    year = input(msg)
    
    try:
        yr = int(year)
    except ValueError:
        print("That was not a valid input. Please enter a numeric value.\n")
        continue

    else:
        if yr >= 0 and len(year) >= 4:
            if yr % 4 == 0:
                
                if yr % 100 == 0:
                    if yr % 400 == 0:
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
