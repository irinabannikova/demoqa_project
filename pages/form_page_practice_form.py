from calendar import month_name

from playwright.sync_api import Page, expect


class FormPagePracticeForm:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = ''
        self.mobile = ''
        self.last_name = ''

    def go_to_practice_form(self):
        self.page.goto('https://demoqa.com/automation-practice-form')

    def fill_main_info(
            self,
            first_name,
            last_name,
            email,
            gender,
            mobile,
            date_birth,
            subjects,
            hobbies,
            address,
            state,
            city
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.page.get_by_placeholder('First Name').fill(first_name)
        self.page.get_by_placeholder('Last Name').fill(last_name)
        self.page.get_by_placeholder('name@example.com').fill(email)
        self.page.get_by_placeholder('Mobile Number').fill(mobile)
        self.page.get_by_placeholder('Current Address').fill(address)
        self.page.locator(f'text="{gender}"').check()
        self.page.locator('#dateOfBirthInput').fill(date_birth)
        self.page.locator('#subjectsInput').fill(subjects[:3])
        self.page.get_by_text(subjects, exact=True).click()
        self.page.locator('#state').click()
        self.page.get_by_text(state, exact=True).click()
        self.page.locator('#city').click()
        self.page.get_by_text(city, exact=True).click()
        self.page.locator(f"text={hobbies}").check()

    def click_to_submit(self):
        self.page.locator('#submit').click()

    def review_form_valid_result(self):
        assert self.page.locator('#example-modal-sizes-title-lg').inner_text() == 'Thanks for submitting the form'
        name_student = self.page.locator('table > tbody > tr:nth-child(1) > td:nth-child(2)').inner_text()
        assert name_student == f'{self.first_name} {self.last_name}', f'{name_student} not have {self.first_name} {self.last_name}'
        mobile_number = self.page.locator('table > tbody > tr:nth-child(4) > td:nth-child(2)').inner_text()
        assert mobile_number == f'{self.mobile}', f'{mobile_number} not have {self.mobile}'

    def review_form_required_fields(self):
        assert self.page.locator('#submit').is_visible()


    def add_picture(self):
        input = self.page.locator("#uploadPicture")
        file_path = r"C:\Users\vahla\PycharmProjects\demoqa_progect\hello.jpg"
        input.set_input_files(file_path)


    def select_date_of_birth(self, month, year, date):
        months_dict = {
            '0': 'January',
            '1': 'February',
            '2': 'March',
            '3': 'April',
            '4': 'May',
            '5': 'June',
            '6': 'July',
            '7': 'August',
            '8': 'September',
            '9': 'October',
            '10': 'November',
            '11': 'December'
        }
        name_month = months_dict[month]
        name_month_short = name_month[:3]
        date_dict = {
                '1': 'st',
                '2': 'nd',
                '3': 'rd',
                '4': 'th',
                '5': 'th',
                '6': 'th',
                '7': 'th',
                '8': 'th',
                '9': 'th',
                '10': 'th',
                '11': 'th',
                '12': 'th',
                '13': 'th',
                '14': 'th',
                '15': 'th',
                '16': 'th',
                '17': 'th',
                '18': 'th',
                '19': 'th',
                '20': 'th',
                '21': 'st',
                '22': 'nd',
                '23': 'rd',
                '24': 'th',
                '25': 'th',
                '26': 'th',
                '27': 'th',
                '28': 'th',
                '29': 'th',
                '30': 'th',
                '31': 'st'
            }

        name_ending = date_dict[date]

        self.page.locator('#dateOfBirthInput').click()
        self.page.select_option('.react-datepicker__month-select', value=month)
        self.page.select_option('.react-datepicker__year-select', value=year)
        self.page.locator(f'[aria-label*="{name_month} {date}{name_ending}, {year}"]').click()
        input_date_birth = self.page.get_attribute('#dateOfBirthInput', 'value')
        assert input_date_birth == f'{date} {name_month_short} {year}'




