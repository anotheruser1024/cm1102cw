import datetime 
import time
import time

day_endings = {
    1: 'st',
    2: 'nd',
    3: 'rd',
    21: 'st',
    22: 'nd',
    23: 'rd',
    31: 'st'
}


def custom_strftime(format, t):
    #function to return custom date format
    #takes y,m,d,timewithsecons
    return time.strftime(format, t).replace('{TH}', str(t[2]) + day_endings.get(t[2], 'th'))

def Easter(y, form):
    # function to return the date of Easter Sunday
    # Input >>>Easter(2001,True)
    # returns 15/04/2001
    # input >>>Easter(2001,False)
    # returns >>> 15th April 2001
    a=y % 19
    b=y // 100
    c=y % 100
    d=b // 4
    e=b % 4
    g=(8 * b + 13) // 25
    h=(19 * a + b - d - g + 15) % 30
    j=c // 4
    k=c % 4
    m=(a + 11 * h) // 319
    r=(2 * e + 2 * j - k - h + m + 32) % 7
    n=(h - m + r + 90) // 25
    p=(h - m + r + n + 19) % 32

    if form == True:
        return datetime.date(year=y, month=n, day=p)
    else:
        date=(y, n, p, 0, 0, 0, 0, 0, 0)
        return custom_strftime('%B {TH} %Y', date)
