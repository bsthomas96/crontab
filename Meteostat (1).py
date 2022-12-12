# Import Meteostat library and dependencies
from datetime import datetime
from datetime import date
from meteostat import Point, Daily

# Set time period
start = datetime(2022, 1, 1)
end = datetime(date.today())

# Create Point for Vancouver, BC
location = Point(49.2497, -123.1193, 70)

# Get daily data for 2022
data = Daily(location, start, end)
data = data.fetch()