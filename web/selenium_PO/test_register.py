from web.selenium_PO.index import Index


class Test_register():

    def setup(self):
        self.index = Index()

    def test_register(self):

        # self.index.goto_lonin().goto_register().register()

        self.index.goto_register().register()

        # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome
