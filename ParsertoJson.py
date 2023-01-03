from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from  selenium.webdriver.chrome.service import Service
import time
import json

file = open('Database3.txt','a+', encoding='utf8')

s = Service("/Users/eldar/PycharmProjects/pythonParserEldar/chromedriver/chromedriver")
driver = webdriver.Chrome(service=s)

URL = 'https://2gis.kg/bishkek/search/%D1%87%D0%B0%D1%81%D1%82%D0%BD%D1%8B%D0%B5%20%D0%BA%D0%BB%D0%B8%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%B2%20%D0%B1%D0%B8%D1%88%D0%BA%D0%B5%D0%BA%D0%B5'

num = 0;
num2 = 1;
canWrite = True

divs = []

try:
    driver.get(url=URL + "/page/" + str(num2))
    #driver.switch_to.default_content()
    #buttonNext = driver.find_elements(By.CLASS_NAME, '_n5hmn94')
    #print(buttonNext[1])

    #WebDriverWait(driver, 10).until(
        #EC.visibility_of_element_located((By.XPATH, '//div[@class="_n5hmn94"][2]/*[name()="svg"]/*[name()="path"]')))
    #btn = driver.find_element(By.XPATH, '//div[@class="_n5hmn94"][2]/*[name()="svg"]')
    #btn.click()
    #ActionChains(driver).move_to_element(btn).click().perform()

    #time.sleep(10)

    #buttonNext[1].click()
    #buttonNext[1].find_element(By.TAG_NAME, 'svg').click()
    #print(buttonNext[1].find_element(By.TAG_NAME, 'svg'))

    for num in range(30):
        driver.get(url=URL + "/page/" + str(num2))
        print(URL+"/page/"+str(num2))
        time.sleep(5)
        clinics = driver.find_elements(By.CLASS_NAME, '_1hf7139')
        for n in clinics:
            if(canWrite):
                print(n.find_element(By.CLASS_NAME, '_hc69qa').text)
                file.write(n.find_element(By.CLASS_NAME, '_hc69qa').text)
                file.write('\n')
                name = n.find_element(By.CLASS_NAME, '_hc69qa').text

                print(n.find_element(By.CLASS_NAME, '_tluih8').text)
                file.write(n.find_element(By.CLASS_NAME, '_tluih8').text)
                file.write('\n')
                address = n.find_element(By.CLASS_NAME, '_tluih8').text

                link = str(n.find_element(By.CLASS_NAME, '_1rehek').get_attribute('href'))

                try:
                    review = n.find_element(By.CLASS_NAME, '_uzv9b5').text
                except Exception as ex:
                    review = 'no review'

                try:
                    print(n.find_element(By.CLASS_NAME, '_qnf2p99').get_attribute('href'))
                    file.write(n.find_element(By.CLASS_NAME, '_qnf2p99').get_attribute('href'))
                    file.write('\n')
                    phone = str(n.find_element(By.CLASS_NAME, '_qnf2p99').get_attribute('href'))
                except Exception as ex:
                    print("no number")
                    phone = 'no number'

                try:
                    print(n.find_element(By.CLASS_NAME, '_18zamfw').text)
                    file.write(n.find_element(By.CLASS_NAME, '_18zamfw').text)
                    file.write('\n')
                    description = n.find_element(By.CLASS_NAME, '_18zamfw').text

                except Exception as ex:
                    print("no description")
                    description = 'no description'

                print('\n')
                file.write('\n')
                file.write('\n')

                dict_c = {
                    'name' : name,
                    'link' : link,
                    'address' : address,
                    'phone' : phone,
                    'description' : description,
                    'review_count' : review
                }

                divs.append(dict_c)
                print(divs)
        with open('data_clinics6.json', 'w+', encoding= 'utf8') as f:
            json.dump(divs,f,indent=4,ensure_ascii= False, sort_keys=False)

        num2 = num2 + 1

        #a_file = open("data_clinics.json", "a", encoding='utf8')
        #data = a
        #json.dump(divs, a_file,indent=4,ensure_ascii= False, sort_keys=False)
        #a_file.close()


        #if(num2 >= 6):
            #num2 = 1

        #buttonNext[1].click()
        #buttonNext[1].find_element(By.TAG_NAME,'svg').find_element(By.TAG_NAME,'path').click()
        #'//*[@id="root"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]/svg/path'

        #WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="_n5hmn94"][2]/*[name()="svg"]/*[name()="path"]')))
        #btn = driver.find_element(By.XPATH,'//div[@class="_n5hmn94"][2]/*[name()="svg"]')
        #btn.click()
        #ActionChains(driver).move_to_element(btn).click().perform()

except Exception as ex:
    print(ex)