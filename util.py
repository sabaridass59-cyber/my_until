import random
def number_guessing():
    scret_num=random.randint(1,100)
    for i in range(1,8):
        try:
            user_input=int(input("Enter a number:"))
            if user_input< 1 or user_input>100:
                print("only allowed 0 to 100 number only")
            elif user_input<scret_num:
                print("You are Enter a number is less")
            elif user_input>scret_num:
                print("You are Enter a number is higher")
            else:
                print("Congrates!!")
                break
        except ValueError:
            print("Strings not allow only enter number in 1 to 100!!")
    if scret_num == user_input:
        print(f"you are guess the number {scret_num} in {i} attemts")
    else:
        print("Sorry your attempts will be compeleted try again!!")

number_guessing()     