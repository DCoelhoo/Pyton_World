print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First Number: ")
    if first_number == "q":
        break
    
    second_number = input("Second Number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) + int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except ValueError:
        print("You can only use numbers!")
    else:    
        print(answer)