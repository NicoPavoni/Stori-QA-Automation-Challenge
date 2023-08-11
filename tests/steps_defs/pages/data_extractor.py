import pandas as pd

from selenium.webdriver.common.by import By

from tests.steps_defs.pages.base_page import BasePage


class DataExtractor(BasePage):
    """
            Page Object for the stori Practice Page.

            Contains methods to interact with the tables who contains information that we need to extract.

            Attributes:
                driver (WebDriver): The WebDriver instance used to interact with the web application.

            Methods:
                This class contains methods to search for its elements. These functions use driver decorators
                (find_element_by_id, find_element_by_xpath, find_element_by_css_selector) to centralize the search code,
                avoid writing waiting conditions throughout the test suite, and simplify the implementation.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    COURSES_TABLE = (By.XPATH, '/html/body/div[3]/div[1]/fieldset/table')
    ENGINEERS_TABLE = (By.CSS_SELECTOR, 'div.tableFixHead > table')
    COURSES_IFRAME = (By.ID, 'courses-iframe')
    MENTORSHIP_TEXT = (By.XPATH, "//li[contains(.,'His mentorship program')]")

    def get_courses_table(self):
        return self.driver.find_element(*self.COURSES_TABLE)

    def get_engineers_table(self):
        return self.driver.find_element(*self.ENGINEERS_TABLE)

    def get_courses_iframe(self):
        return self.driver.find_element(*self.COURSES_IFRAME)

    def get_mentorship_program_text(self):
        return self.driver.find_element(*self.MENTORSHIP_TEXT)

    def get_engineers_table_rows(self):
        """
               Get the rows of the engineers table.
        """
        table = self.get_engineers_table()
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
        return rows

    def get_courses_table_rows(self):
        """
                Get the rows of the courses table.
        """
        table = self.get_courses_table()
        rows = table.find_elements(By.TAG_NAME, 'tr')[1:]
        return rows

    def get_courses(self, price):
        """
        Get a list of courses with the given price from the provided rows.
        """
        courses = []
        rows = self.get_courses_table_rows()
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            if columns[2].text == str(price):
                courses.append(columns[1].text)
        return courses

    def save_courses_to_excel(self, price, file_name):
        """
        Save the courses with the given price from the courses table to an Excel file.
        """
        courses = self.get_courses(price)
        data = {'Courses': courses}
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)

    def get_engineers(self, rows, career):
        """
                Get a list of engineers from the given rows.
        """
        self.get_engineers_table()
        engineers = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            if cols[1].text == str(career):
                engineers.append(cols[0].text)
        return engineers

    def save_engineers_to_excel(self, file_name):
        """
        Save the names of the engineers from the engineers table to an Excel file.
        """
        rows = self.get_engineers_table_rows()
        engineers = self.get_engineers(rows, career="Engineer")
        data = {'Engineer Names': engineers}
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)
