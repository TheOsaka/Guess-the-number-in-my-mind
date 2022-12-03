answer = 24

soru = "Got a number on my mind, let's guess!"
print("Let's play the guessing game!!!")

while True: 
    guess = int(input(soru))

    if guess < answer:
        print("Little higher...")
    elif guess > answer:
        print("Little lower...")
    else:
        print("Congratulations, you know!!!")
        break
