'''
# TIC ("time in custody") functions

A handful of tools for doing some of the basic math the *Criminal Code* requires.

Despite the fact that all the calculations are relatively straightforward, they confuse defendants, lawyers, and judges to no end. These tools should provide everything that's needed on the back-end to make the process perfectly straightforward.
'''


from datetime import date, time, datetime

def tic_calculator_cli():
    '''
    Simple CLI interface to calculate TIC. 
    
    TODO
    * Basic functionality
    * Automatically break down years and months (assumes y=365; mo=30; 12mo = 1y)
    * Error correction
    * Alternate date entry/format recognition
    '''
    
    # Assumes errorless input
    start = input("Enter arrest date (yyyy-mm-dd):")
    stop = input("Enter sentencing date (yyyy-mm-dd):")
    tic = tic_calculator(start, stop)

    pass


def tic_calculator(start, stop, ratio=1.5, lenity=True):
	'''
    # DONE
	* Calculates TIC from a start and stop date
	* Returns TIC at 1:1 and at the enhanced ratio (default 1.5:1)
	* Can be used in tandem with a function that adds discrete periods of custody together
    
    # TODO
    * Adjust enhanced_credit and total_tic for lenity
    '''
	
    tic = (stop - start).days
    total_tic = tic * ratio
    enhanced_credit = tic * ratio - tic
    
    # Rounds up for half-days if the lenity rule applies, down if it doesn't
    if lenity == True:
        
        if int(total_tic) < total_tic:
            total_tic = int(total_tic) + 1
            enhanced_credit = int(enhanced_credit) + 1
            
        else:
            total_tic = int(total_tic)
            enhanced_credit = int(enhanced_credit)
    
    return tic, enhanced_credit, total_tic
    


def default_time_calculator(fine, tic, rate=12.5):
    '''
    TODO
    * Define a function to calculate time in default
    * It should default to $100/d (or 12.5/h)
    * Advanced feature will accept a provincial code as an argument and calculate the precise amount of default time
    '''
    pass
