import os, random
os.system("cls")

print("="*50, "MAGIC NUMBER GAME", "="*50)

# set a min and max number for the dificulty
min = 1
max = 10
print(f"I have a number between {min} and {max}. Can you guess it?")

# Start Game Loop
while True:
    # get a random number
    magic_number = random.randint(min, max)
    magic_number = 5   # TODO Remove this!!!

    # set maximum tries to 3
    tries = 3
    print(f"You have {tries} tries.")

    # ask player guess
    player_guess = input("Your guess?")

    # check player guess
    while player_guess != str(magic_number):
        os.system("cls")

        # remove one tries
        tries -= 1
        if tries == 0:
            break

        print(f"Wrong guess. You have {tries} tries left. Try again!")
        player_guess = input("Your guess?")

    os.system("cls")
    if player_guess == str(magic_number):
        print(f"You win! {magic_number} was my number! :)))")
    else: 
        print(f"My number was {magic_number}.")
        print("Game over :((")
    
    # Ask player if he/she wants to play again
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice == "n":
        exit()
    os.system("cls")