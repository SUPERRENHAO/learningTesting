from selenium.webdriver.common.by import By

from web.selenium_TCLAD.page.base_page import Base_Page
from web.selenium_TCLAD.page.resource_managment import Resource_managment


class Launcher(Base_Page):


    def goto_resource_management(self):



        self.find(By.ID,'nav_resources_a').click()


        return  Resource_managment(self._driver)

    def goto_system_managment(self):
        pass


