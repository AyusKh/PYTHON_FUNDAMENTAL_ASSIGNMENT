def classify_number():
            num = int(input("Enter a number: "))
            if num > 0:
                print("The number is positive.")
            elif num < 0:
                print("The number is negative.")
            else:
                print("The number is zero. Exiting the program.")
classify_number()