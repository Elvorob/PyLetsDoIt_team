

class BasePage():
    def __init__(self, browser, link):
        self.browser = browser
        self.URL = link

    def open_page(self):
        self.browser.get(self.link)
