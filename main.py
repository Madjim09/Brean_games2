from brain_games.engine import run_game
import games.game_nok as game_nok
import games.game_progression as game_progression

def main():
    print("Choose a game:")
    print("1 - Even Game")
    print("2 - Calc Game")
    choice = input("Enter number: ").strip()

    if choice == '1':
        run_game(game_nok)
    elif choice == '2':
        run_game(game_progression)
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
