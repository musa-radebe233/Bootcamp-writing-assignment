# Task 0.8
def convert_to_hrs(time):
    hour = int(time / 60)
    return hour
print("%d hours" %convert_to_hrs(133),",", end = ' ')

def convert_to_min(time):
    hour = int(time/60)
    hours_and_minutes = float(time/60)
    minute = (hours_and_minutes - hour) * 60
    return minute
print("%d minutes" %convert_to_min(00))


