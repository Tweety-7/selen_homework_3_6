"""
Реализуйте в файле conftest.py логику запуска браузера с указанным
 языком пользователя. Браузер должен объявляться в фикстуре browser
  и передаваться в тест как параметр.
В файл test_items.py напишите тест, который проверяет, что 
страница товара на сайте содержит кнопку добавления в корзину. 
Например, можно проверять товар, доступный по 
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
Тест должен запускаться с параметром language следующей командой:

pytest --language=es test_items.py
"""
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_btn_have(browser):
	browser.get(link)
	# time.sleep(30)
	#поиск кнопки дообавить в корзину
	btn = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")	
	btn.click() #тык на кнтпку для появления алертов(или не совсем алертов - 
	# переключиться на них невозможно)
	alerts = browser.find_elements_by_class_name("alertinner")
	assert "Coders at Work" in alerts[0].text
	