def convert_to_min(time):
    hour = int(time //60)
    hours_and_minutes = (time/60)
    minute = (hours_and_minutes - hour) * 60
    if hour > 1 and minute > 1:
        print("%01d hours, %01d minutes" % (hour, minute))
    elif hour < 1 and minute == 1:
        print("%01d hours, %01d minute" % (hour, minute))
    elif hour == 1 and minute > 1:
        print("%01d hour, %01d minutes" % (hour, minute))
    elif hour > 1 and minute == 1:
        print("%01d hours, %01d minute" % (hour, minute))
    elif hour > 1 and minute < 1:
        print("%01d hours, %01d minutes" % (hour, minute))
    elif hour == 1 and minute < 1:
        print("%01d hour, %01d minutes" % (hour, minute))
convert_to_min(133)
