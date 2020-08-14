import random
secretNUMBER = random.randint(1 ,20)
print("$$$$$$\  $$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\       $$$$$$\$$$$\  $$\   $$\        $$$$$$\   $$$$$$$\  $$$$$$$ ")
print("$$  __$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|      $$  _$$  _$$\ $$ |  $$ |       \____$$\ $$  _____|$$  _____|")
print("$$ /  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\        $$ / $$ / $$ |$$ |  $$ |       $$$$$$$ |\$$$$$$\  \$$$$$$\ ")
print("$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\       $$ | $$ | $$ |$$ |  $$ |      $$  __$$ | \____$$\  \____$$\ ")
print("\$$$$$$$ |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |      $$ | $$ | $$ |\$$$$$$$ |      \$$$$$$$ |$$$$$$$  |$$$$$$$  | ")
print("\____$$ | \______/  \_______|\_______/ \_______/       \__| \__| \__| \____$$ |       \_______|\_______/ \_______/  ")
print("$$\   $$ |                                                            $$\   $$ |                                    ")
print("\$$$$$$  |                                                            \$$$$$$  |                 ")
print("\______/                                                              \______/         ")
print("                                        INSTAGRAM - @nanophanoxy  / AKASH          ")
print((""))
print("")
print("LET's PLAY A GAME GUESS A NUMBER WITHIN 1 AND 20")
for guessTaken in range(1,7):
    print("GUESS MY MIND")
    guess = int(input())
    if guess < secretNUMBER:
        print("YOUR GUESS IS LOW ")
    elif guess > secretNUMBER:
        print("YOUR GUESS IS HIGH ")
    else:
        break
#ask
    if guess == secretNUMBER:
        print("YOUR GUESS IS CORRECT")
    else:
        pass
print("THE NUMBER IS " + str(secretNUMBER))
