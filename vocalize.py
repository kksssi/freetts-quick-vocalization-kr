from selenium import webdriver
import time
from urllib import request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

filename = 'vocab.txt'
with open(filename, encoding="utf8") as file:
    vocab = [line.rstrip() for line in file]

print(vocab)

options = Options()
options.headless = True

# To prevent download dialog
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)  # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/mp3')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver.get("https://freetts.com/")


for text in vocab:
    # select language
    voice_selection = Select(driver.find_element(By.ID, 'Language'))
    voice_selection.select_by_value('ko-KR')

    # select voice
    voice_selection = Select(driver.find_element(By.ID, 'Voice'))
    voice_selection.select_by_value('Seoyeon_Female')

    # type text into the form
    text_input = driver.find_element(By.ID, 'TextMessage')
    driver.execute_script("arguments[0].scrollIntoView();", text_input)
    text_input.clear()
    text_input.send_keys(text)

    # download audio to file
    audio_btn = driver.find_element(By.ID, 'btnAudio')
    driver.execute_script("arguments[0].scrollIntoView();", audio_btn)
    audio_btn.click()
    time.sleep(3)
    driver.find_element(By.ID, 'DivDownloadLink').click()
    driver.switch_to.window(driver.window_handles[-1])
    driver.switch_to.default_content()
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    request.install_opener(opener)
    request.urlretrieve(driver.current_url, "mp3/" + text + ".mp3")
    driver.close()
    # driver.switch_to.default_content()
    driver.switch_to.window(driver.window_handles[0])

driver.close()

