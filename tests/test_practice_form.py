from selene.support.shared import browser
from selene import have, be, command
import os


def test_registration_form_demo_qa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type("Andrew")
    browser.element('#lastName').type("Jones")
    browser.element('#userEmail').type('andrew_jones@test.com')
    browser.all('[for^=gender-radio]').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').type('7111222333')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select [value="1999"]').click()
    browser.element('.react-datepicker__day--015').click()
    browser.element('#subjectsInput').should(be.blank).type('arts').press_enter()
    browser.all('[for^=hobbies-checkbox-3]').element_by(have.exact_text('Music')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img/new_year.jpeg'))
    browser.element('#currentAddress').type('Russia, Moscow, 109012')
    browser.element('.css-yk16xz-control').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').perform(command.js.click)

    browser.element('.table').all('td').even.should(have.exact_texts(
        'Andrew Jones',
        'andrew_jones@test.com',
        'Male',
        '7111222333',
        '15 September,1999',
        'Arts',
        'Music',
        'new_year.jpeg',
        'Russia, Moscow, 109012',
        'NCR Noida'))
