import time
print("Hi, my name is Vincent.")
time.sleep(1)
print("What´s your name?")
user = input()
if user == "Joachim":
    print("Good morning my creator!")
    print('')
elif user == 'Mieke':
    print("Oh, what a pleasure! It feels great to have the Hello World Academy in the house.")
    time.sleep(1)
    print("Is Joachim somewhere around too?")
    answer = input()
    if answer == 'yes':
        print('Great, a strong team!')
    elif answer == 'no':
        print('OK, if you see him make sure he knows that we miss him.')
    else:
        print("Well, did not get that, but thats's fine. See you buddy!")
    print('')
else:
    print(f"Nice to meet you {user}.")
    print('')
time.sleep(1)
