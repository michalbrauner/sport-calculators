import math


def convert_seconds_to_tempo(seconds):
    data = dict(minutes=0, seconds=0)

    data["minutes"] = math.floor(seconds / 60)
    data["seconds"] = round(seconds) - data["minutes"] * 60

    return data


def convert_seconds_to_time(seconds):
    data = dict(hours=0, minutes=0, seconds=0)

    data["hours"] = math.floor(seconds / (60 * 60))
    data["minutes"] = math.floor((seconds - (data["hours"] * 60 * 60)) / 60)
    data["seconds"] = round(seconds) - (data["hours"] * 60 * 60) - (data["minutes"] * 60)

    return data
