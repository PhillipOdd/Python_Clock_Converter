def time_converter(hours, minutes,seconds,period):
    if 1 <= hours <= 12 and 0 <= minutes < 60 and 0 <= seconds < 60 and period in {'AM', 'PM'}:
        if period == 'PM':
            hours = (hours + 12) % 24
            formatted_time = f"{hours:02d}:{minutes:02d}:{seconds}"
            return formatted_time
        else:
            return "Please put in the correct format"
        
hours = int(input("Enter time in hours:"))
minutes = int(input("Enter time in minutes:"))
seconds = int(input("Enter time in seconds:"))
period = input("Enter AM or PM:")

formatted_time = time_converter(hours,minutes,seconds,period)
print ("Whats the time?", formatted_time)

