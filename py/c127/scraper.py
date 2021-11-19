from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
#To install Chrome Driver on runtime.
from webdriver_manager.chrome import ChromeDriverManager
START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

# chrome_options = webdriver.ChromeOptions()

#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

# browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
browser = webdriver.Chrome(ChromeDriverManager().install())


# Else place chromedriver.exe in the path where code is executed..that is CodePython and mention "chromedriver.exe"
# or full path
# browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
    planet_data = []
    for i in range(0, 457):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        # Under Elements of Inspect, first icon to highlight which tag each element in page represents
        for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        #browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[@class="next"]/a').click()
        # Site causes issues if next arrow is clicked very fast
        time.sleep(2)
        # w+ creates the file if it does not exists
    with open("scrapper_2.csv", "w+") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()