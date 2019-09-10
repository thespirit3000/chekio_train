#!/usr/local/bin/checkio --domain=py run time-converter-24h-to-12h

# You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
# - the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
# - if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
# Here you can find some useful information about the12-hour format.
# 
# 
# 
# Input:Time in a 24-hour format (as a string).
# 
# Output:Time in a 12-hour format (as a string).
# 
# Precondition:
# '00:00'<= time<= '23:59'
# 
# 
# END_DESC

def time_converter(time):
    hh = time.split(':')
    if int(hh[0]) >= 13:
        time = str(int(hh[0]) - 12) +':'+str(hh[1])+' p.m.'
    elif int(hh[0]) == 12:
        time = time+' p.m.'
    elif int(hh[0]) == 0:
        time = str(12)+':'+str(hh[1])+' a.m.'
    else:
        time = time[1:5]+' a.m.'
    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")