import GetExcel

if __name__ == '__main__':
    # Enter a date : string
    e = GetExcel.CrawlToDownload(date='2020-04-25')
    e.goto('http://www.tsetmc.com/Loader.aspx?ParTree=15131F')
    e.get_excel()
    