from brain_games.games import brain_even
from brain_games.scripts.brain_games import launch_game


def main():
    launch_game(brain_even, play_count=3)


if __name__ == '__main__':
    main()
