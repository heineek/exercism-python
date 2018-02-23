from datetime import date
from leap import is_leap_year


def days_in_month(month, is_leap_year=False):
    months_with_30_days = {4, 6, 9, 11}

    if month == 2:
        if is_leap_year:
            num_of_days = 29
        else:
            num_of_days = 28
    elif month in months_with_30_days:
        num_of_days = 30
    else:
        num_of_days = 31

    return num_of_days


def meetup_day(year, month, weekday_str, day_order):

    class MeetupDayException(Exception):
        pass

    days_of_week = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3,
                    'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    days_descriptions = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5,
                        'last': 'last',
                        'teenth': (13, 14, 15, 16, 17, 18, 19)}

    #days_in_month = 0

    weekday = days_of_week[weekday_str]

    # calculate all dates in month
    number_of_days = days_in_month(month, is_leap_year(year))
    month_dates = [date(year, month, day) for day in range(1, number_of_days + 1)]

    # all weekdays in month
    month_weekdays = [(day, day.weekday()) for day in month_dates]

    required_day = days_descriptions[day_order]

    # collect all dates with required weekday
    all_dates_with_required_weekday = []
    for item in month_weekdays:
        if weekday in item:
            all_dates_with_required_weekday.append(item[0])

    # select required date using description
    if required_day == 'last':
        result = all_dates_with_required_weekday[-1]
    elif type(required_day) is int:
        if len(all_dates_with_required_weekday) >= required_day:
            result = all_dates_with_required_weekday[required_day - 1]
        else:
            raise MeetupDayException()
    elif type(required_day) is tuple:
        for item in all_dates_with_required_weekday:
            if item.day in required_day:
                return item
        raise MeetupDayException()      # no such day
    else:
        raise MeetupDayException()      # date not found

    return result