

# Importing the datetime module for date and time objects
from datetime import datetime

def time_delta(t1, t2):
    # The format of the time string
    d_format = "%a %d %b %Y %H:%M:%S %z"

    time_stamp1 = datetime.strptime(t1, d_format) #Converts to the given format
    time_stamp2 = datetime.strptime(t2, d_format)

    # Calculate the time difference between the two times
    time_dif = time_stamp2 - time_stamp1

    time_delta_in_seconds = abs(time_dif.total_seconds()) #Time value in seconds

    return str(int(time_delta_in_seconds))  # Return the time difference in seconds as a string
