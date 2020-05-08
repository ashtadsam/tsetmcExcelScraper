import GetExcel
import datetime
from dateutil import utils as date_utils


DAYS = 14

if __name__ == '__main__':
    # Enter a date : string
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(DAYS)]
    for date in date_list:
        if date_utils.datetime.isoweekday(date) == 4:
            date_list.remove(date)
            continue
        if date_utils.datetime.isoweekday(date) == 5:
            date_list.remove(date)
            continue

    for date in date_list:
        e = GetExcel.CrawlToDownload(date=date.strftime("%Y-%m-%d"))
        e.goto('http://www.tsetmc.com/Loader.aspx?ParTree=15131F')
        e.get_excel()
    