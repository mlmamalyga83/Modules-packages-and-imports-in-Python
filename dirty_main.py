from datetime import datetime
from application.salary import *
from application.db.people import *


if __name__ == "__main__":
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    calculate_salary()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    get_employees()