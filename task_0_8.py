def convert_to_min(time):
    hour = (time //60)
    hours_and_minutes = (time/60)
    minute = round((hours_and_minutes - hour) * 60)
    if hour == 1:
        hours = ""
    else:
        hours = "s"
    if minute ==1:
        minutes = ""
    else:
        minutes = "s" 
    print(f"{hour} hour{hours} , {minute} minute{minutes}")       
convert_to_min(121)
