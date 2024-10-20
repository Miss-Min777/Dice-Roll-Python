# p1=1
# p2=1
#
#
# print("*"
#                          "\n\t\t\t\t\tSCORE BOARD"
#       "\n*"
#                 f"\n\t\t\tPlayer-1                  {p1} "
#                 f"\n\t\t\tPlayer-2                  {p2}"
#       "\n*")




import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 3.0)
engine.setProperty('voice', voices[1].id)

# Dice representations
rolls = ['''
┌───────────┐ 
│           │
│     ●     │
│           │
└───────────┘
   ''', '''
┌───────────┐ 
│        ●  │
│           │
│  ●        │
└───────────┘
  ''', '''
┌───────────┐ 
│        ●  │
│     ●     │
│  ●        │
└───────────┘
  ''', '''
┌───────────┐ 
│ ●       ● │
│           │
│ ●       ● │
└───────────┘
  ''', '''
┌───────────┐ 
│ ●       ● │
│     ●     │
│ ●       ● │
└───────────┘
  ''', '''
┌───────────┐ 
│ ●       ● │
│ ●       ● │
│ ●       ● │
└───────────┘
''']

def roll_dice():

    try:
        num_players = int(input("\nEnter the number of players: "))
        if num_players < 2:
            print("Sorry,The game requires at least 2 players.")
            engine.say("Sorry,The game requires at least 2 players.")
            engine.runAndWait()
            print("---------------------------------------------------------------------------------------------------")
            replay = input("\n\nDo you want to play again? press 'Y' or 'y' to retry..else press another key to exit: ")
            if replay == 'y' or replay == 'Y':
                roll_dice()
            else:
                exit()

        n = int(input(f"How many round you want to play with {num_players} players? "))
        if n<=0:
            print("Error!! Invalid number of rounds")
            print("---------------------------------------------------------------------------------------------------")
            replay = input("\nDo you want to play again? press 'Y' or 'y' to retry..else press another key to exit: ")
            if replay == 'y' or replay == 'Y':
                roll_dice()
            else:
                exit()

        print(f"\nStarting the game with {num_players} players.")
        print(f"You have {n} chances to win the game...\n")

    except ValueError:
        print("Invalid input. Please enter a number.")
        engine.say("Invalid input. Please enter a number.")
        engine.runAndWait()
        print("---------------------------------------------------------------------------------------------------")
        replay = input("\nDo you want to play again? press 'Y' or 'y' to retry..else press another key to exit: ")
        if replay == 'y' or replay == 'Y':
            roll_dice()
        else:
            exit()


    scores = [0] * num_players
    for round_num in range(n+1):
        if round_num < n:
            print("---------------------------------------------------------------------------------------------------")
            print(f"\n\t\t\t● ROUND {round_num + 1} ●")

            # Collecting rolls for each player
            dice_rolls = []
            for player in range(num_players):
                cont = input(f"Player-{player + 1}, press 'Y' or 'y' to roll the dice: ")
                if cont == 'y' or cont == 'Y':
                    die_roll = random.randint(0, 5)
                    dice_rolls.append(die_roll)
                    print(f"Player-{player + 1} rolled: {rolls[die_roll]}")
                    engine.say(f"Player-{player + 1} rolled: {die_roll+1} {rolls[die_roll]}")
                    engine.runAndWait()
                else:
                    print("Invalid input. You missed your chance to roll.")
                    engine.say("Invalid input. You missed your chance to roll.")
                    engine.runAndWait()
                    dice_rolls.append(-1)  # Representing a missed roll

            # Determine the highest roll
            max_roll = max(dice_rolls)
            round_winners=[]
            for i in range(len(dice_rolls)):
                if dice_rolls[i] == max_roll:
                    round_winners.append(i)


            if len(round_winners) == 1:
                winner = round_winners[0]
                print(f"---- Player-{winner +1} wins this round ----")
                engine.say(f"---- Player-{winner + 1} wins this round. ----")
                engine.runAndWait()
                scores[winner] += 1
            else:
                print("---- It't a tie this round ----")
                engine.say(f"---- It't a tie this round. ----")
                engine.runAndWait()

            print("\nScores so far:")
            for player in range(num_players):
                print(f"Player-{player + 1}: {scores[player]}")

        if round_num == n:
            print("---------------------------------------------------------------------------------------------------")
            print("\n────────────────────────── ")
            print("\t---FINAL SCORES:---")
            engine.say("Final Scores")
            engine.runAndWait()
            for player in range(num_players):
                print(f"    Player-{player + 1}:     {scores[player]}")
            print("────────────────────────── ")

            winner_score = max(scores)
            game_winners = []
            for i in range(len(scores)):
                if scores[i] == winner_score:
                    game_winners.append(i)

            if len(game_winners) == 1:
                print(f"\nCongratulation Player-{game_winners[0] + 1} wins the game!")
                engine.say("Congratulation Player-{game_winners[0] + 1} wins the game!")
                engine.runAndWait()
            else:
                print("\nIt't a tie between:")
                engine.say("It't a tie between.")
                engine.runAndWait()
                for winner in game_winners:
                    print(f"Player-{winner + 1}")

            print("GAME IS OVER...better luck next time..!!")
            engine.say("GAME IS OVER...better luck next time..!!")
            engine.runAndWait()

    print("\n●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●-●")
    replay = input("\nDo you want to play again? press 'Y' or 'y' to retry..else press another key to exit: ")
    if replay == 'y' or replay == 'Y':
        roll_dice()
    else:
        print("Thank you for playing!")
        engine.say("Thank you for playing!")
        engine.runAndWait()

# Start the game
roll_dice()