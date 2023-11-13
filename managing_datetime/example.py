from datetime import datetime, date, time, timedelta

# Current date and time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Current date
current_date = date.today()
print("Current Date:", current_date)

# Current time
current_time = datetime.now().time()
print("Current Time:", current_time)

# Creating a specific datetime
custom_datetime = datetime(2022, 11, 13, 15, 30)
print("Custom Datetime:", custom_datetime)

# Creating a specific date
custom_date = date(2022, 11, 13)
print("Custom Date:", custom_date)

# Creating a specific time
custom_time = time(15, 30)
print("Custom Time:", custom_time)

# Formatting datetime as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Datetime:", formatted_datetime)

# Parsing a string into a datetime object
date_str = "2022-11-13 15:30:00"
parsed_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_datetime)

# Calculate the difference between two dates or times
time_difference = custom_datetime - current_datetime
print("Time Difference:", time_difference)

# Add or subtract time from a datetime
new_datetime = custom_datetime + timedelta(days=5, hours=3)
print("New Datetime:", new_datetime)