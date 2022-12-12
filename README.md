Meteostat Python Package

The Meteostat Python Package is a simple API for accessing open weather and climate data. Historical and statistical observations of the weather patterns are collected by the Meteostat package from accessible public interfaces, most of which are mostly governmental.

#Accessing the Weather API data

First, installation of the Meteostat Python package is done using the code:
pip install meteostat

Then, the point and daily attributes are called from the library. The point attribute will be used to
specify the location to which the data is collected from. The daily attribute is used to define the
frequency or periods to which the data can be accessed.

#Scheduling/Cronjob

After writing the python script to access the meteostat data, writing and implementing of a
cronjob script to run the API access script is done.

Installation of crontab is done first. Then there is need to call the crontab and pandas for writing
the accessed data to csv. 
The cronjobs implemented will pull the data at 12.01am daily, 10.00pm every Sunday night and at the end of every quarter. The data is written to a csv file available locally on the machine where the cronjob is running.