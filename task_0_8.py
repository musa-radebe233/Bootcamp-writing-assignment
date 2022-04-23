def convert_to_min(time):
    hour = int(time //60)
    hours_and_minutes = float(time/60)
    minute = (hours_and_minutes - hour) * 60
    return hour, minute
print(convert_to_min(5))





