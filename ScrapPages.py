import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import path


class Box:
    def __init__(self, box, attrs, name, what):
        if type(attrs) is not dict:
            raise Exception("attrs must be a dict")
        if type(name) is not str:
            raise Exception("name must be a string")
        if type(box) is not str:
            raise Exception("box must be a string")
        self._box = box
        self._attrs = attrs
        self._name = name
        self._what = what

    def __getitem__(self, item):
        if item == "box":
            return self._box
        elif item == "attrs":
            return self._attrs
        elif item == "name":
            return self._name
        elif item == "what":
            return self._what


class ScrapPages:
    USE_SELENIUM = False

    def __init__(self, home=None, area=None, boxes=None, data=None,
                 use_selenium=USE_SELENIUM):
        self._use_selenium = use_selenium
        self._area = area
        self._home = home
        self._boxes = boxes
        self._data = data
        self._title = None
        self._driver = None
        if use_selenium:
            chrome_options = Options()
            chrome_options.add_argument("user-data-dir=selenium")
            self._driver = webdriver.Chrome(executable_path="assets/webdriver/chromedriver.exe",
                                            options=chrome_options)

    def get_html(self, url):
        if self._use_selenium:
            if path.exists("assets"):
                self._driver.get(url)
                self.selenium_interaction(self._driver)
                html = self._driver.page_source
                return html
            else:
                raise Exception("Directory assets does not exists")
        else:
            conn = requests.get(url)
            html = conn.content
            return html

    def get_area(self, soup):
        area = soup.find(self._area["box"], self._area["attrs"])
        return self.get_boxes(area)

    def get_boxes(self, soup):
        ret = []
        boxes = soup.find_all(self._boxes["box"], self._boxes["attrs"])
        for b in boxes:
            if callable(self._boxes["what"]) and not self._boxes["what"](b):
                continue
            ret.append(self.get_data(b))
        return ret

    def get_data(self, soup):
        info = {}
        for d in self._data:
            data = soup.find(d["box"], d["attrs"])
            info[d["name"]] = self.extract_info(soup, d, data)
        return info

    def write_data(self, dict_obj):
        pass

    def next_page_url(self, soup):
        pass

    def selenium_interaction(self, driver):
        pass

    def go(self):
        url = self._home
        info = []
        while url is not None:
            html = self.get_html(url)
            soup = BeautifulSoup(html, "html.parser")
            url = self.next_page_url(soup)
            info = info + self.get_area(soup)
        self.write_data(info)
        if self._driver:
            self._driver.close()
            self._driver.quit()

    @staticmethod
    def extract_info(soup, d, data):
        if callable(d["what"]):
            return d["what"](data)
        if d["what"] == "text":
            return data.text
        if d["what"] == "a href":
            a = soup.find("a")
            return a.attrs["href"]
        else:
            return data.attrs[d["what"]]
