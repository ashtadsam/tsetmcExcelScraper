import GetExcel

if __name__ == '__main__':
    # Enter a date : string
    e = GetExcel.CrawlToDownload("2020-01-01")
    e.get_excel()
    