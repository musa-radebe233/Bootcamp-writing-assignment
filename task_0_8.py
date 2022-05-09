def convert_to_min(time):
    hour = int(time //60)
    hours_and_minutes = (time/60)
    minute = (hours_and_minutes - hour) * 60
    return hour, minute
    if time > 120:
        a = "%01d hours, %01d minutes" % convert_to_min(133)
        print (a) 
print("%01d hour, %01d minutes" % convert_to_min(133))





