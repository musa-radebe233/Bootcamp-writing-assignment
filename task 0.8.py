# Task 0.8
def convert_to_hrs(time):
    hours = int(time / 60)
    return hours
print("hours:", convert_to_hrs(133))

def convert_to_min(time):
    hours = int(time/60)
    hours_and_minutes = float(time/60)
    minutes = (hours_and_minutes - hours) * 60
    return minutes
print("minutes", convert_to_min(133))


