from datetime import date as d
from datetime import timedelta
import doctest

# Comtains function to check if a date is in the past week or a future date

"""
{{{ TO CHANGE }}}
1. Change path to include parent directory and import module
import sys
sys.path.insert(1, '../.')
from get_dates import check_date

2. Convert date as string to date using
    * remove - from format (not needed)
    * .date() converts datetime obj to date obj
new_date = datetime.strptime(old_date, "format").date()

3. Remove unncessary imports
x from datetime import timedelta

4. Add import
from datetime import datetime

"""



def check_date(date):
    """
    
    >>> date = d.today() # Today
    >>> check_date(date)
    True
    
    >>> date = d.today() + timedelta(days=1) # Tomorrow
    >>> check_date(date)
    True
    
    >>> date = d.today() + timedelta(days=365) # Next year
    >>> check_date(date)
    True
    
    >>> date = d.today() - timedelta(days=1) # Yesterday
    >>> check_date(date)
    True
    
    >>> date = d.today() - timedelta(days=3) # Last day of past week
    >>> check_date(date)
    True
    
    >>> date = d.today() - timedelta(days=7) # Last week
    >>> check_date(date)
    False
    
    >>> date = d.today() - timedelta(days=365) # Last year
    >>> check_date(date)
    False
    """
    today = d.today()
    
    past_week = []
    temp_day = d.today()
    
    for i in range(7):
        past_week.append(temp_day)
        temp_day = temp_day-timedelta(1)

    return date in past_week or date > today


if __name__ == "__main__":
    doctest.testmod()
