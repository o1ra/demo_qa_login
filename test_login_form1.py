from selene import browser, have, be


def test_registratoin():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://demoqa.com/text-box')
    browser.element('.main-header').should(have.text('Text Box'))

    browser.element('#userName').type('Irina K')
    browser.element('#userEmail').type("irinatest@gmail.com")
    browser.element('#currentAddress').type('Almaty, street Al-Farabi, 666')
    browser.element('#permanentAddress').type('Almaty, street Batyra, 777')

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    browser.element('#submit').click()

    browser.element('#output').should(be.visible)
    browser.element('#name').should(have.text('Irina K'))
    browser.element('#email').should(have.text('irinatest@gmail.com'))
    browser.element('#output #currentAddress').should(have.text('Almaty, street Al-Farabi, 666'))
    browser.element('#output #permanentAddress').should(have.text('Almaty, street Batyra, 777'))
