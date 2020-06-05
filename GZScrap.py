from ScrapPages import ScrapPages, Box


class GZScrap(ScrapPages):
    def __init__(self, page):
        ScrapPages.__init__(self, "https://www.giallozafferano.it/ricette-cat/" + page)
        self._area = Box(box="div", attrs={"class": "gz-content"}, name="area", what="text")
        self._boxes = Box(box="article", attrs={"class": "gz-card"}, name="box", what="text")
        self._data = [Box(box="h2", attrs={"class": "gz-title"}, name="title", what="text"),
                      Box(box="div", attrs={"class": "gz-description"}, name="description", what="text"),
                      Box(box="h2", attrs={"class": "gz-title"}, name="recipe_url", what="a href"),
                    ]
        self._title = "Giallo Zafferano"

    def next_page_url(self, soup):
        arrow = soup.find("a", {"class": "gz-arrow next"})
        if arrow is not None:
            if "href" not in arrow.attrs:
                return None
            return arrow.attrs["href"]
        else:
            return None

    def write_data(self, dict_obj):
        print(dict_obj)
