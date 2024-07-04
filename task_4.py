from datetime import datetime, timedelta


def get_upcoming_birthdays(user_list: list) -> list:
    """
    Get a list of user`s birthdays and return upcoming birthdays. If B-Day falls on weekend, it will be moved to Monday

    :param user_list: list with dicts, where keys are 'name' and 'birthday'
    :return: list with dicts, where keys are 'name' and 'congratulation_date'
    """
    result = []
    today = datetime.today().date()

    try:
        for user in user_list:
            date_obj = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

            if timedelta(days=0) <= date_obj - today <= timedelta(days=7):
                if date_obj.weekday() == 5:
                    date_obj += timedelta(days=2)
                elif date_obj.weekday() == 6:
                    date_obj += timedelta(days=1)

                new_dict = {
                    "name": user["name"],
                    "congratulation_date": datetime.strftime(date_obj, "%Y.%m.%d"),
                }

                result.append(new_dict)
    except Exception:
        raise Exception("Here should be some error message")
    else:
        return result
