from ScrapPages import ScrapPages, Box


class TAScrap(ScrapPages):
    def __init__(self, page):
        self._area = Box(box="div", attrs={"class": "restaurants-list-List__wrapper--3PzDL"},
                         name="area", what="text")
        self._boxes = Box(box="div", attrs={"class": "_1llCuDZj"},
                          name="box", what=self.no_sponsor)
        self._data = [
            Box(box="a", attrs={"class": "_15_ydu6b"}, name="url", what="href"),
        ]
        ScrapPages._title = "Trip Advisor"
        ScrapPages.__init__(self, "https://www.tripadvisor.it/" + page, self._area, self._boxes, self._data)

    @staticmethod
    def no_sponsor(soup):
        sponsor = soup.find("div", {"class": "_376lhJeB fXv-kKaf"})
        if sponsor is None:
            return True
        return False

    def next_page_url(self, soup):
        return None

    def write_data(self, dict_obj):
        print(dict_obj)
