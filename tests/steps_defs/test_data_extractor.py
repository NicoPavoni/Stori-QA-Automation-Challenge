from tests.steps_defs.pages.data_extractor import DataExtractor


def test_save_courses_to_excel(driver):
    page = DataExtractor(driver)
    page.save_courses_to_excel(price=25, file_name='courses_names.xlsx')


def test_save_engineers_to_excel(driver):
    page = DataExtractor(driver)
    page.save_engineers_to_excel('engineer_names.xlsx')


def test_find_text_and_print_it(driver):
    page = DataExtractor(driver)
    iframe = page.get_courses_iframe()
    driver.switch_to.frame(iframe)
    text_element = page.get_mentorship_program_text()
    print(text_element.text)
    expected_text = 'His mentorship program is most after in the software testing community with long waiting period.'
    assert expected_text == text_element.text
