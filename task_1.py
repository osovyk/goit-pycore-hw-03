from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculate the difference between the entered date and the current date and return it in days

    :param date: str
    :return: delta: int
    """
    try:
        datetime_obj = datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        raise Exception("Here should be some error message")
    else:
        current_date = datetime.today()
        delta = (datetime_obj - current_date).days
        return delta
