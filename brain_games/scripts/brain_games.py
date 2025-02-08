from brain_games.cli import welcome_user
from brain_games.scripts.utility import game


def main():
    welcome_user()


def launch_game(game_module, play_count: int):
    user_name = welcome_user()
    game(play_count=play_count,
         player_name=user_name,
         task_and_correct_ans_fun=game_module.get_task_and_answer)


if __name__ == '__main__':
    main()
