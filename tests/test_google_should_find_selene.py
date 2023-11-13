from selene.support.shared import browser
from selene import be, have


#первый тест
def test_one(start_settings_google):
    browser.element('[id="L2AGLb"]').click()
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('.FPdoLc input.gNO89b').click()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_empty_results(start_settings_google):
    browser.element('[id="L2AGLb"]').click() #Согласие на куки
    browser.element('[name="q"]').should(be.blank).type('wejrio3roi32or34r3jof32342') #Находим input поле поиска
    browser.element('.FPdoLc input.gNO89b').click() #Нажимаем найти
    browser.element('[id="botstuff"]').should(have.text('По запросу wejrio3roi32or34r3jof32342 ничего не найдено.')) #Проверяем что результатов нету