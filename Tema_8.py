# Tema 8 - SELECTORS
#


#####//input[@id= "job-title"]
# Exerciții Recomandate - grad de dificultate: Ușor
# 1. Revizualizează întâlnirea 7 și ia notițe în caz că ți-a scăpat ceva.
# Te rog să scrii pe canalul de comunicare scrisă unde întâmpini dificultăți și te
# ajut.
# Dacă stai blocat > 30 min, cere indiciu.


# Exerciții obligatorii - grad de dificultate: Usor spre Mediu
# Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos
# - https://www.phptravels.net/
# - http://automationpractice.com/index.php
# - https://formy-project.herokuapp.com/
# - https://the-internet.herokuapp.com/
# - https://www.techlistic.com/p/selenium-practice-form.html
# - jules.app

# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
# ● Link text
# ● Parțial link text
# ● Name
# ● Tag*
# ● Class name*
# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
#
# observație:
# - Probabil nu vei găsi un singur website care să cuprindă toate variantele  de mai sus,
# astfel că îți recomandăm să folosești mai multe site-uri
# - Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
# Interactionează cu un element la alegere din listă.
from time import sleep
# import org.openqa.selenium.support.ui.Select

from selenium.webdriver import chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)

# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?id_product=4&controller=product')

# # ● Id
# Quantity = chrome.find_element(By.ID, "quantity_wanted")
# '''Quantity.send_keys('2') # pune in casuta 12, i-a 1 default si puna alaturi 2 ?!?!'''
# Quantity.clear()
# sleep(3)
# Quantity.send_keys('2')
# sleep(3)
#
# chrome.find_element(By.LINK_TEXT, "Add to wishlist").click()
# sleep(3)
# chrome.find_element(By.LINK_TEXT, "Facebook").click()
# sleep(3)

# chrome.quit()
#
#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.phptravels.net/')
# Color = chrome.find_element(By.ID, "checkin")
# Color.click()
# sleep(3)
# chrome.quit()
#
#
#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# Address = chrome.find_element(By.ID, "autocomplete").send_keys("Brasov")
# sleep(3)
# chrome.quit()



# ● Link text
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
# sleep(2)
# chrome.find_element(By.LINK_TEXT,"Autocomplete").click()
# sleep(2)
# chrome.quit()
#
#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/frames')
# sleep(2)
# chrome.find_element(By.LINK_TEXT,"Nested Frames").click()
# sleep(3)
# chrome.quit()
#
#
#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php?id_product=4&controller=product#/size-s/color-beige')
# chrome.find_element(By.LINK_TEXT, "Add to wishlist").click()
# sleep(3)
# chrome.quit()


# ● Parțial link text
'''
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/')
# sleep(2)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Entr").click()
# sleep(3)
# chrome.quit()
'''

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
# sleep(2)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Log").click()
# sleep(3)
# chrome.quit()

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
# sleep(2)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()
# sleep(3)
# chrome.quit()

#
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://jules.app/sign-in')
# sleep(2)
# chrome.find_element(By.PARTIAL_LINK_TEXT,"Sig").click()
# sleep(3)
# chrome.quit()




# ● Name
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://the-internet.herokuapp.com/forgot_password')
# sleep(2)
# chrome.find_element(By.NAME,"email").send_keys("andreea@an.a")
# sleep(3)
# chrome.quit()
# #
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(2)
# chrome.find_element(By.NAME,"lastname").send_keys("andreea")
# sleep(3)
# chrome.quit()
# #
# #
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(2)
# chrome.find_element(By.NAME,"continents").send_keys("North America")
# sleep(3)
# chrome.quit()





# ● Tag*
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
# tag = chrome.find_elements(By.TAG_NAME, 'input')
# tag[1].send_keys('Tag1')
# sleep(2)
# tag[2].send_keys('Tag2')
# sleep(2)
# tag[3].click()
# sleep(3)
# chrome.quit()



# ● Class name*
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
# clasa=chrome.find_elements(By.CLASS_NAME, 'form-control')
# clasa[1].send_keys("a")
# sleep(2)
# clasa[3].click()
# sleep(3)
# clasa[4].click()

'''
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
# Select drp'''





# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')
#
# chrome.find_element(By.CSS_SELECTOR, 'input#last-name').send_keys('LastName')
# sleep(2)
# chrome.find_element(By.CSS_SELECTOR, 'input#last-name').clear()
# sleep(3)
#
# chrome.find_element(By.CSS_SELECTOR, 'input.form-control'). send_keys('clasa')
# sleep(3)
#
# chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="Enter your job title"]').send_keys('Job')
# sleep(3)





# Pentru xpath identifică elemente după criteriile de mai jos:
# ● 3 după atribut valoare
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')

# chrome.find_element(By.XPATH, '//input[@id="first-name"]').send_keys("Andre")
# sleep(3)
# chrome.find_element(By.XPATH, '//input[@id="last-name"]').send_keys("Lech")
# sleep(3)
# chrome.find_element(By.XPATH, '//input[@id="job-title"]').send_keys("job new")
# sleep(3)





# ● 3 după textul de pe element
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/form')

# buttons = chrome.find_element(By.XPATH, '//a[contains(text(), "Buttons")]').text
# assert buttons == 'Contextual'
# sleep(3)


# buttons = chrome.find_element(By.XPATH, '//a[contains(text(), "Buttons")]').text
# assert buttons == 'Buttons'
# sleep(3)
#
# form = chrome.find_element(By.XPATH, '//a[contains(text(), "Complete Web Form")]').text
# assert form == 'Complete Web Form'

# sleep(3)


# ● 1 după parțial text

# chrome.find_elements(By.PARTIAL_LINK_TEXT,'Male' )
# sleep(2)

# ● 1 cu SAU, folosind pipe |
# # ● 1 cu *
# so=chrome.find_element(By.XPATH,'//*[@id="first-name"] | //*[@id="job-title"]')
# sleep(2)
# so.send_keys('test')

# ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci cu (xpath)[1]
# chrome.find_element(By.XPATH,'//*[@id="select-menu"]/option[2]').click()
# sleep(2)

# ● 1 în care să folosești parent::

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php')

# chrome.find_element(By.XPATH, '//a[@class="product-name"]/parent::h5')
# sleep(3)

# ● 1 în care să folosești fratele anterior sau de după (la alegere)

# chrome.find_elements(By.XPATH, '//*[@id="thumbnail_11"]/parent::ul/li/following-sibling::li[1]')
#
# sleep(3)
# ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu ce element vreau să interacționez.




# Exerciții extra - Opțional
# https://www.automatetheplanet.com/most-exhaustive-xpath-locators-cheat-sheet/