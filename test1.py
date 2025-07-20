def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_days = len(weather_data)

    # Extract low and high temperatures for calculation
    lows = [convert_f_to_c(day[1]) for day in weather_data]
    highs = [convert_f_to_c(day[2]) for day in weather_data]

    # Find min and max using your helper functions
    min_temp, min_index = find_min(lows)
    max_temp, max_index = find_max(highs)

    min_day = convert_date(weather_data[min_index][0])
    max_day = convert_date(weather_data[max_index][0])

    # Calculate averages
    avg_low = calculate_mean(lows)
    avg_high = calculate_mean(highs)

    # Format final summary string
    summary = (
        f"{num_days} Day Overview\n"
        f"The lowest temperature will be {format_temperature(min_temp)}, and will occur on {min_day}.\n"
        f"The highest temperature will be {format_temperature(max_temp)}, and will occur on {max_day}.\n"
        f"The average low this week is {format_temperature(round(avg_low, 1))}.\n"
        f"The average high this week is {format_temperature(round(avg_high, 1))}.\n"
    )

    return summary
