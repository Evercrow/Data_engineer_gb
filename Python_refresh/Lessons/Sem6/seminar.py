
import sys
from all_tasks import *

LOWER_LIMIT = 0
UPPER_LIMIT = 10
GUESS_LIMIT = 3
print(guess_game(LOWER_LIMIT, UPPER_LIMIT, GUESS_LIMIT))
if len(sys.argv) > 1:
    print(guess_game_mk2(*sys.argv))
RIDDLE_TXT = "Зимой и летом одним цветом"
answers = ["ель", "елка", "асфальт", "елочка"]
print(f"Попытка номер {custom_guess(RIDDLE_TXT, answers)}")
print(f"Попытка номер {custom_guess(RIDDLE_TXT, answers)}")
for row in print_log():
    print(row)
print(f"{check_date('20.11.2000')=}")
