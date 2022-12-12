from crontab import CronTab
import pandas as pd
file_cron = CronTab(tabfile='meteostat.tab')

mem_cron = CronTab(tab="""
  1 0 * * * command
""")

mem_cron = CronTab(tab="""
  0 22 * * 0 command
""")

mem_cron = CronTab(tab="""
  0 0 * */3 * command
""")

pd.to_csv('meteostat.csv')