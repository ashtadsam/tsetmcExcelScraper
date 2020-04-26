from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from ConvertDate import ConvertDate

from environs import Env
env = Env()
env.read_env()


class CrawlToDownload:
    def __init__(self, date):
        self.date:str = ConvertDate(date).to_solar()

        options = Options()
        options.headless = True

        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList", 2)
        fp.set_preference("browser.download.dir", env.str('DIR'))
        fp.set_preference("browser.download.manager.showWhenStarting", False)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk",
                          "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        
        self.browser = webdriver.Firefox(options=options, firefox_profile=fp)

    def goto(self, url:str):
        self.browser.get(url)
        print('%s\t:OK!'% url)

    def get_excel(self):
        self.browser.find_element_by_class_name('MwExcel').click()
        print('Openned History Window!')
        self.browser.find_element_by_id('exceldate').send_keys(self.date)
        self.browser.find_element_by_xpath(
            "//div[@onclick='mw.ExportClick(\"dateexcel\")']").click()
        print("File Downloaded! \t%s" % self.date)
        self.browser.close()
