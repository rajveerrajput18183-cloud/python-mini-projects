import random

user_score = 0
computer_score = 0

def game_win(user, computer):
    # draw
    if user == computer:
        return None

    # snake vs water
    if user == "s" and computer == "w":
        return True
    if user == "w" and computer == "s":
        return False

    # water vs gun
    if user == "w" and computer == "g":
        return True
    if user == "g" and computer == "w":
        return False

    # gun vs snake
    if user == "g" and computer == "s":
        return True
    if user == "s" and computer == "g":
        return False


while True:
    rand_no = random.randint(1, 3)
    print("Computer's turn: Snake(s), Water(w), Gun(g)")

    if rand_no == 1:
        computer = "s"
    elif rand_no == 2:
        computer = "w"
    else:
        computer = "g"

    try:
        user = input("Your turn Snake(s), Water(w), Gun(g): ").lower()
        if user not in ["s", "w", "g"]:
            raise ValueError
    except ValueError:
        print("Invalid input! Choose s, w, or g")
        continue

    result = game_win(user, computer)

    print("Computer chose:", computer)

    if result is None:
        print("It's a draw")
    elif result:
        print("You win 🎉")
        user_score += 1
    else:
        print("You lose 😢")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

    choice = input("Play again? (y/n): ").lower()
    if choice == "n":
        break