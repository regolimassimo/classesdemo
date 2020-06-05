from ScrapPages import ScrapPages, Box
import json


class AnsaScrap(ScrapPages):
    def __init__(self, page):
        self._area =  Box(box="div",
                          attrs={"class": "pp-column"},
                          name="area",
                          what="text")
        self._boxes = Box(box="article",
                          attrs={"class": "news"},
                          name="box",
                          what="text")
        self._data = [
            Box(box="h3",  attrs={"class": "news-title"}, name="title",    what="text"),
            Box(box="h3",  attrs={"class": "news-title"}, name="url",      what="a href"),
            Box(box="div", attrs={"class": "news-date"},  name="date",     what="text"),
            Box(box="p",   attrs={"class": "news-abs"},   name="abstract", what="text"),
            Box(box="div", attrs={"class": "news-tags"},  name="tags",     what=self.get_tags),
        ]
        ScrapPages._title = "Ansa"
        ScrapPages.__init__(self, "https://www.ansa.it/sito/notizie/" + page, self._area,
                            self._boxes, self._data, use_selenium=True)

    def next_page_url(self, soup):
        li = soup.find("li", {"class": "pg-next"})
        if li is not None:
            a = li.find("a")
            if a is None:
                return None
            if "href" not in a.attrs:
                return None
            return "https://www.ansa.it" + a.attrs["href"]
        else:
            return None

    def get_tags(self, soup):
        ret = []
        lis = soup.find_all("li")
        for li in lis:
            ret.append(li.text)
        return ret

    def write_data(self, dict_obj):
        print(json.dumps(dict_obj, indent=2))
