#Converts 12h time format <-> 24h time format
def time_converter(start):
    hours = start[:start.find(':')]
    ampm = start[-2:]
    #Converts 12h format to 24h format
    if ampm == 'AM' or ampm == 'PM':
        minutes = start[start.find(':') + 1 : start.find(' ')]
        #1:00 PM - 11:59 PM -> 13:00 - 23:59
        if ampm == 'PM' and hours != '12':
            hours = int(hours) + 12
        #12:00 AM - 12:59 AM -> 0:00 - 0:59
        elif ampm == 'AM' and hours == '12':
            hours = 0
        return str(hours) + ':' + minutes
    #Converts 24h format to 12h format
    else:
        minutes = start[start.find(':') + 1:]
        #12:00 - 12:59 -> 12:00 PM - 12:59 PM
        if hours == '12':
            return hours + ':' + minutes + ' PM'
        #00:00 - 00:59 -> 12:00 AM - 12:59 AM
        if hours == '0':
            return '12:' + minutes + ' AM'
        #13:00 - 23:59 -> 1:00 PM - 11:59 PM
        elif int(hours) > 12:
            hours = int(hours) - 12
            return str(hours) + ':' + minutes + ' PM'
        #1:00 - 11:59 -> 1:00 AM - 11:59 AM
        elif int(hours) >= 1 and int(hours) <= 11:
            return start + ' AM'

def add_time(start, duration, day = None):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    #Converts start time (12h) to military time (24h)
    start_mt = time_converter(start)

    minutes_start_mt = start_mt[start_mt.find(':') + 1:]
    minutes_duration = duration[duration.find(':') + 1:]
    minutes_new_time = str((int(minutes_start_mt) + int(minutes_duration)) % 60)
    
    #Formats the minutes of new_time so that the value is always double digit
    if len(minutes_new_time) == 1:
        minutes_new_time = '0' + minutes_new_time
    
    #Checks if minutes of start time + minutes duration > 60
    add_hour = (int(minutes_start_mt) + int(minutes_duration)) // 60
    
    hours_start_mt = start_mt[:start_mt.find(':')]
    hours_duration = duration[:duration.find(':')]
    hours_new_time = (int(hours_start_mt) + int(hours_duration) + add_hour) % 24

    days_later = (int(hours_start_mt) + int(hours_duration) + add_hour) // 24
    
    new_time = str(hours_new_time) + ':' + minutes_new_time
    new_time = str(time_converter(new_time))
    
    if day != None:
        #Starting day isn't case sensitive
        day = day[0].upper() + day[1:].lower()
        day_index = days.index(day)
        new_day_index = (day_index + days_later) % 7
        new_day = days[new_day_index]
        new_time += ', ' + new_day
    
    if days_later == 1:
        new_time += ' (next day)'
    elif days_later > 1:
        new_time += ' ('+ str(days_later) + ' days later)'
    
    return new_time

add_time('8:16 PM', '466:02', 'tuesday')