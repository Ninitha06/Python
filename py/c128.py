from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
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

headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date","hyperlink","planet_type","discovery_date","mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
planet_data = []
new_planet_data = []

# Else place chromedriver.exe in the path where code is executed..that is CodePython and mention "chromedriver.exe"
# or full path
# browser = webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
def scrape():   
    # Scrape few pages alone to test the program
    for i in range(0, 458):
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
            hyperlink_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_tag.find_all("a", href=True)[0]["href"])
            planet_data.append(temp_list)
        
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        # browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[@class="next"]/a').click()
        # Site causes issues if next arrow is clicked very fast
        time.sleep(2)

  
def scrape_more_data(hyperlink):
    print(hyperlink)
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []
        for tr_tag in soup.find_all("tr", attrs={"class": "fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class": "value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)



scrape()

for index, data in enumerate(planet_data):
    scrape_more_data(data[5])
    print(f"{index+1} page done 2")


final_planet_data = []
for index, data in enumerate(planet_data):
    new_planet_data_element = new_planet_data[index]
    # Each value has \n which has to be removed
    new_planet_data_element = [elem.replace("\n", "") for elem in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]
    final_planet_data.append(data + new_planet_data_element)

with open("final.csv", "w+",newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_planet_data)