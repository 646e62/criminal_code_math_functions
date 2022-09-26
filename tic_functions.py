'''
# TIC ("time in custody") functions


'''

from datetime import date, time, datetime

def tic_calculator_cli():
    # Assumes errorless input
    start = input("Enter arrest date (yyyy-mm-dd):")
    stop = input("Enter sentencing date (yyyy-mm-dd):")
    tic = tic_calculator(start, stop)

    pass


def tic_calculator(start, stop, ratio=1.5, lenity=True):
	'''
	Calculates TIC from a start and stop date
	Returns TIC at 1:1 and at the enhanced ratio (default 1.5:1)
	Can be used in tandem with a function that adds discrete periods of
	custody together
    '''
    
	pass

def default_time_calculator(fine, tic, rate=12.5):
    '''
    Define a function to calculate time in default
    It should default to $100/d (or 12.5/h)
    Advanced feature will accept a provincial code as an argument and calculate the precise amount of default time
    '''
    
    pass
