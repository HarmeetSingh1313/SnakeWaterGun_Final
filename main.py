'''
-1 for water 💦
0 for gun 🔫
1 for snake 🐍
'''

import random

youDict = {"s": 1, "g": 0, "w": -1}
reverseDict = {1: "Snake 🐍", 0: "Gun 🔫", -1: "Water 💦"}

while True:  # game loop

    # Score reset each game
    you_Score = 0
    computer_Score = 0
    rounds = 3

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")

        youstr = input(" s->Snake 🐍 \n w->Water 💦 \n g->Gun 🔫 \n Enter your choice: ")

        while youstr not in youDict:
            print("❌ Invalid input!")
            youstr = input(" s->Snake 🐍 \n w->Water 💦  \n g->Gun 🔫 \n Enter your choice: ")

        you = youDict[youstr]
        computer = random.choice([-1, 0, 1])

        print(f" You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]} \n")

        if computer == you:
            print("🤝 It's a Draw!")
        elif (you == -1 and computer == 0) or (you == 0 and computer == 1) or (you == 1 and computer == -1):
            print("🏆 You Win!")
            you_Score += 1
        else:
            print("🤖 Computer Wins!")
            computer_Score += 1

        print(f"Score:\nYou -> {you_Score}\tComputer -> {computer_Score}\n")

    # Final result after 3 rounds
    print("\n--- FINAL RESULT ---")
    if you_Score > computer_Score:
        print(f"You -> {you_Score}\tComputer -> {computer_Score}\n🏆 You Win the Game!")
    elif you_Score < computer_Score:
        print(f"You -> {you_Score}\tComputer -> {computer_Score}\n🤖 Computer Wins the Game!")
    else:
        print(f"You -> {you_Score}\tComputer -> {computer_Score}\n🤝 It's a Draw!")

    # Play again option
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing! Goodbye!")
        break


# 1 -> Snake 🐍  -1 -> Water 💦  0 -> Gun 🔫
