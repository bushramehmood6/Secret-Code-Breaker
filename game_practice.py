import random
easy_level=["apple","banana","grape","islamabad","laptop"]
moderate_level=["chocolate","strawberry","mango","karachi","mobile"]
hard_level=["pomegranate","watermelon","blueberry","multan","headphones"]

print(f"Welcome to the Password Guessing Game!")
user_input=input(f"\nEnter your choice:1/2/3 : ")
if user_input=="1":
    secret=random.choice(easy_level)
elif user_input=="2":
    secret=random.choice(moderate_level)
elif user_input=="3":
    secret=random.choice(hard_level)
else:
    print("invalid choice,Reset to default mode-EASY LEVEL")
    secret=random.choice(easy_level)

attempt=0
print(f"Now we are going  to start our guessing game ")

while True:
    guess=input(f"Enter your password guess: ").lower()
    attempt += 1
    if guess==secret:
        print(f"Congratulations! You've guessed the password '{secret}' in {attempt} attempts.")
        break

    hint = ""
    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
           hint += guess[i]
        else:
            hint += "_"
    print("hint:", hint)


print("thank you for playing")