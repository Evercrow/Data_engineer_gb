from all_tasks import checktime
import sys

if len(sys.argv) > 1:
    print(checktime.check_date(*sys.argv))
else:
    print("you didn't give any date console arguments")