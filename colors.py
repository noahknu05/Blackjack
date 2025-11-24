import time
class Color:
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    reset = "\033[0m"

class Helper:
    def read_command_ranged(menu, x1, x2):
        x2 += 1
        while True:
            command = (input(f"{menu}\nEnter command ({x1}-{x2-1}): "))
            try:
                if int(command) not in range(x1, x2):
                    raise ValueError
                else:
                    return command
                
            
            except ValueError:
                print(Color.red + "\nInvalid command.\n" + Color.reset)
                time.sleep(1)

    if __name__ == "__main__":
        menu1 = "1 - 3"
        command = read_command_ranged(menu1, 1, 3)
        print(command)