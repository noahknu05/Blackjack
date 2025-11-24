from colors import Color
# ui.py

def clear_lines(n):
    for _ in range(n):
        # Move cursor up one line and clear it
        print("\033[F\033[K", end="")



def input_player_action(allowed_act):
    i = 1
    for action in allowed_act:
        print(f"{allowed_act[action]}: ({action}) |", end=" ")
    print("")

    
    #print("Hit (h), Stand (s), Double Down (dd), Split (sp), Surrender (sur): ")
    while True:
        action = input("Command: ").strip().lower()
        if action in allowed_act:
            return action
        else:
            clear_lines(i)
            print("Not a valid command.")
            i = 2

def input_player_bet(chips):
    i  = 1
    while True:
        try:
            bet = int(input("Bet ammount: "))
            if  0 < bet <= chips:
                return bet
            
            elif bet <= 0:
                    clear_lines(i)
                    print("Bet must be positive")

            else:
                clear_lines(i)
                print(Color.yellow + "Not enough chips" + Color.reset)

            i = 2
            
            
             
        except ValueError:
            clear_lines(i)
            print("Please enter a number.")

                

if __name__ == "__main__":
    action = input_player_action()
    