from datetime import timedelta


def add_gigasecond(birthday):
    delta = timedelta(seconds=10**9)
    return birthday + delta