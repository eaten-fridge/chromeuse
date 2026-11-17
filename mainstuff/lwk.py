import sys
import valid as v
import driving as d
def main():
    #this is a menu interface for stuff that i make, like a Driver's Ed assistant
    #as shown in 'PG1'
    PG1 = 'Driving Time Calculator'
    PG2 = 'Chess'

    print('Please choose a option from below.')
    #now its time to display the options
    print('#1:\t', PG1)
    #so far we only have 1 option, which is okay
    #time for the choice part of all of this
    choice = v.tg('|>')
    #v.tg is a number validator in a different place of the folder, therefore the import at the top (valid)
    if choice == 1:
        print("Launching ", PG1, '...' sep = '')
        pg1()
    elif choice > 1 or choice < 1:
        print('Please enter a valid number.')
        #literally just more validation just in case


def pg1():
    d.drivingTime() #this is a function in a different file, refer to driving.py
    print() #this is just a blank spacer
    main() #restarts
