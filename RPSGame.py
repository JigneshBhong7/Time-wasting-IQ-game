import random
import keyboard
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)\n'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)\n'''

Scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
while True:

    print("Let's play Rock, Paper, Scissor against the computer.")
    options = [Rock, Paper, Scissor]
    option_for_user = input("Choose :\n"
                   "1. Rock\n"
                   "2. Paper\n"
                   "3. Scissor\n")

    option_For_computer = print(f"Computer\n"
                                f"{random.choice(options)}")

    print("You\n")
    if option_for_user == "1":
        print(Rock)
    elif option_for_user == "2":
        print(Paper)
    elif option_for_user == "3":
        print(Scissor)
    else:
        print("Enter valid Input")
    if option_For_computer == option_for_user:
        print("Gues It's a Draw")
    elif ((option_For_computer == "rock" and option_for_user == "2") or
          (option_For_computer == "paper" and option_for_user == "3") or
          (option_For_computer == "scissor" and option_for_user == "1")):
        print("You Win!")
    else:
        print("You Lose!")
    print("Press Enter to play or any other key to exit.")
    key = keyboard.read_key()
    if key == "enter":
        print("Alright")
    else:
        break
    # choice = input("\nPress Enter to exit, or type '/' to run again: ")
    # if choice.strip().lower() != '/':
    #     print("Thanks for playing! Goodbye.")
    #     break