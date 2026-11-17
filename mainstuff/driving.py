
def drivingTime():

    def getValidInput(prompt):
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                else:
                    print('Please enter a positive number.')
            except ValueError:
                print('Please enter a valid whole number.')

    sessions = getValidInput('How many driving sessions have you completed? ')

    totalMinutes = 0

    for i in range(sessions):
        print('Session', i + 1)

        hours = getValidInput('How many hours did you drive? ')
        minutes = getValidInput('How many minutes did you drive? ')

        totalMinutes += (hours * 60) + minutes

    totalHours = totalMinutes // 60
    remainingMinutes = totalMinutes % 60

    print('Total driving time:')
    print(totalHours, 'hours and', remainingMinutes, 'minutes')


drivingTime()
