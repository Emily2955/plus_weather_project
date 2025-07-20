import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")
    

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    tempf = float(temp_in_fahrenheit)
    celsius = (tempf-32) * 5/9
    return round(celsius,1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    temp_values=[]
    for item in weather_data:
        temp_values.append(float(item))
    mean_value = sum(temp_values) / len(temp_values)
    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    data=[]
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row!=[]:
                date=row[0]
                mintemp=float(row[1])
                maxtemp=float(row[2])
                data.append([date,mintemp,maxtemp])
    return data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    location_index=0
    minimum_value = float(weather_data[0])
    for index, value in enumerate(weather_data):
        if float(value)<=minimum_value:
            location_index=index
            minimum_value=float(value)
    return (float(minimum_value), location_index)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    
    if not weather_data:
        return ()
    location_index=0
    maximum_value = float(weather_data[0])
    for index, value in enumerate(weather_data):
        if float(value)>=maximum_value:
            location_index=index
            maximum_value=float(value)
    return (float(maximum_value), location_index)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    #Calls previous defined elements and defines helper functions
    low = [convert_f_to_c(day[1]) for day in weather_data]
    high = [convert_f_to_c(day[2]) for day in weather_data]

    min_temp, min_index = find_min(low)
    max_temp, max_index = find_max(high)

    min_day = convert_date(weather_data[min_index][0])
    max_day = convert_date(weather_data[max_index][0])

    average_low = calculate_mean(low)
    average_high = calculate_mean(high)

    #Tell it how to present the summary as a string
    all_summary= (
    f"{len(weather_data)} Day Overview\n"
    f"  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {min_day}.\n"
    f"  The highest temperature will be {format_temperature(max_temp)}, and will occur on {max_day}.\n"
    f"  The average low this week is {format_temperature(round(average_low, 1))}.\n"
    f"  The average high this week is {format_temperature(round(average_high, 1))}.\n"
    )
        
    return "".join(all_summary)


    

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    overall_summary=[]

    for day in weather_data:
        date = convert_date(day[0])
        min_daily = convert_f_to_c(day[1])
        max_daily = convert_f_to_c(day[2])

        daily_summary = (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {format_temperature(min_daily)}\n"
            f"  Maximum Temperature: {format_temperature(max_daily)}\n\n"
        )
        overall_summary.append(daily_summary)

    return "".join(overall_summary)

    
