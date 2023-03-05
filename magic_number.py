import os, random
os.system("cls")

tries = 3
min = 1
max = 10
magic_number = random.randint(min, max)

print("="*50, "MAGIC NUMBER GAME", "="*50)
print(f"I have a number between {min} and {max}. Can you guess it?")
print(f"You have {tries} tries.")

player_guess = input("Your guess?")

while player_guess != str(magic_number):
    os.system("cls")
    tries -= 1
    if tries == 0:
        print(f"My number was {magic_number}.")
        print("Game Over :(")
        exit()

    print(f"Wrong guess. You have {tries} tries left. Try again!")
    player_guess = input("Your guess?")

os.system("cls")
print(f"You win! {magic_number} was my number! :)))")