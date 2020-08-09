
from value import Value
from value import SectorValue
from value import StockValue

class ScrapFactory:
    def __init__(self, scrap_type):
        print("__init__")
        self.scrap_type = scrap_type
    
    def create_scrap(self):
        print("create_scrap")

    def scrap_value(self):
        print("scrap_value")


class SectorScrapFactory(ScrapFactory):
    def __init__(self, scrap_type):
        print("__init__")
        super().__init__(scrap_type)
        print("scrap_type: {}".format(self.scrap_type))

    def create_scrap(self):
        print("create_scrap")
        self.sectors = SectorValue(self.scrap_type)
        self.scrap_value()
        return self.sectors.get_value()

    def scrap_value(self):
        print("scrap_value")
        self.request_value()
        a = [1, 2, 3]
        self.sectors.set_value(a)

    def request_value(self):
        print("request_value")


class StockScrapFactory(ScrapFactory):
    def __init__(self, scrap_type):
        print("__init__")
        super().__init__(scrap_type)
        print("scrap_type: {}".format(self.scrap_type))

    def create_scrap(self):
        print("create_scrap")
        self.stocks = StockValue(self.scrap_type)
        self.scrap_value()
        return self.stocks.get_value()

    def scrap_value(self):
        print("scrap_value")
        self.request_value()
        a = [1, 2, 3]
        self.stocks.set_value(a)
    
    def request_value(self):
        print("request_value")


if __name__ == "__main__":
    scrap_type = 1
    scrap = ScrapFactory(scrap_type)
    scrap.create_scrap()

    scrap_type = 2
    stocks = StockScrapFactory(scrap_type)
    stocks.create_scrap()

    scrap_type = 3
    sectors = SectorScrapFactory(scrap_type)
    sectors.create_scrap()
