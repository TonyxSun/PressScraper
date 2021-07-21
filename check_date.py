from datetime import date as d
from datetime import timedelta
import doctest

# Comtains function to check if a date is in the past week or a future date

"""
{{{ TO CHANGE }}}

1. Remove imports
from datetime import timedelta
from datetime import date as d

2. Add import
from datetime import datetime

3. Change path to include parent directory and import module
import sys
sys.path.insert(1, '../.')
from check_date import check_date

4. Convert date as string to date, and adjust functions accordingly
    * remove - from format (not needed)
    * .date() converts datetime obj to date obj
# Obtain date as object
date_obj = datetime.strptime(date, "format").date()

5. Remove function
get_past_days()

6. Change d to datetime when creating csv

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
