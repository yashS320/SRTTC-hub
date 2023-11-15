import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest.")
    time.sleep(1)

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def forest_path():
    print("You come across a fork in the path.")
    time.sleep(1)
    choices = ["Take the left path.", "Take the right path."]
    choice = make_choice(choices)

    if choice == 1:
        print("You encounter a friendly squirrel. It leads you to a hidden treasure!")
    else:
        print("You find a dark cave. Inside, you discover a sleeping dragon!")

def mountain_path():
    print("You start climbing a steep mountain.")
    time.sleep(1)
    choices = ["Continue climbing.", "Descend and explore the caves below."]
    choice = make_choice(choices)

    if choice == 1:
        print("You reach the summit and enjoy a breathtaking view.")
    else:
        print("You enter the caves and find a chest with valuable gems.")

def main():
    introduction()
    
    choices = ["Explore the forest.", "Ascend the mountain."]
    choice = make_choice(choices)

    if choice == 1:
        forest_path()
    else:
        mountain_path()

if __name__ == "__main__":
    main()
