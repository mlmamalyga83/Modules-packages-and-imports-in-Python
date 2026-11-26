from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == "__main__":
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    calculate_salary()
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    get_employees()