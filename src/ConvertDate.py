from datetime import datetime
import jdatetime


class ConvertDate:
    def __init__(self, date:str=datetime.now().strftime("%Y-%m-%d")):
        self.date = date

    def get_today(self) -> str:
        return str(jdatetime.date.today())
    
    def seprate_date(self) -> list:
        return self.date.split('-')

    def to_solar(self) -> str:
        date = self.seprate_date()
        return str(jdatetime.date.fromgregorian(day=int(date[2]), month=int(date[1]), year=int(date[0])))
    