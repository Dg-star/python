from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Лях Никита 107б2

def open_tab(url):
	driver.switch_to.new_window('tab')
	save_get(url)

def save_get(url):
	try:
		windows_before = driver.window_handles
		driver.get(url)
		WebDriverWait(driver, 1).until(EC.new_window_is_opened(windows_before))
	except Exception as ex:
		pass

def save_switch(num):
	try:
		windows_before = driver.window_handles
		driver.switch_to.window(driver.window_handles[num])
		WebDriverWait(driver, 1).until(EC.new_window_is_opened(windows_before))
	except Exception as ex:
		pass


driver = webdriver.Chrome()

URL_VERSES = ("https://www.culture.ru/literature/poems/author-aleksandr-pushkin")
URL_TRANSLATOR = ("https://translate.google.com")

driver.get(URL_TRANSLATOR)
open_tab(URL_VERSES)

verses_urls = driver.find_elements(By.CLASS_NAME, 'ICocV')
verses_urls = verses_urls[:8]
verses_urls = [verse_url.get_attribute('href') for verse_url in verses_urls]


verses_ru = []
verses_en = []

driver.switch_to.new_window('tab')
for verse_url in verses_urls:
	save_get(verse_url)
	verse = driver.find_element(By.CLASS_NAME, 'xZmPc').text
	verses_ru.append(verse)
driver.close()

save_switch(0)

tuple_textarea_ru = [(By.CLASS_NAME, 'n4sEPd'), (By.CLASS_NAME, 'er8xn')]
tuple_textarea_en = [(By.CLASS_NAME, 'lRu31'), (By.CLASS_NAME, 'ryNqvb')]
tuple_btn_clear = (By.CSS_SELECTOR, 'button.VfPpkd-Bz112c-LgbsSe')

textarea_ru = driver.find_element(*tuple_textarea_ru[0]).find_element(*tuple_textarea_ru[1])
btn_clear = driver.find_element(*tuple_textarea_ru[0]).find_element(*tuple_btn_clear)

for verse_ru in verses_ru:
	textarea_ru.send_keys(verse_ru)

	WebDriverWait(driver, 6).until(EC.presence_of_element_located(tuple_textarea_en[0]) and EC.presence_of_element_located(tuple_textarea_en[1]))

	textareaes_en = driver.find_element(*tuple_textarea_en[0]).find_elements(*tuple_textarea_en[1])
	combined = ' '.join([textarea.text for textarea in textareaes_en])
	verses_en.append(combined)
	btn_clear.click()

	WebDriverWait(driver, 6).until(EC.text_to_be_present_in_element(tuple_textarea_ru[0], ""))

driver.quit()



with open('result.txt', 'w', encoding='utf-8') as file:
	for i in range(8):
		file.write(f'{i + 1} Russian: {verses_ru[i]} \n\n')
		file.write(f'{i + 1} English: {verses_en[i]} \n\n')

