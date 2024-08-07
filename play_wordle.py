from wordle import Wordle
from colorama import Fore

def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")
    while wordle.can_attempt:
        x = input("Type your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long.")
            continue
        
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")

    if wordle.is_solved:
        print("You've solved the puzzle!")
    else:
        print("You've failed to solve the puzzle!")


if __name__ == "__main__":
   main()