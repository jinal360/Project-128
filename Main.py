from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    planet_data = []
    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul"):
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
            new_planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

final_planet_data = []

def scrape_more_data(hyperLink):
    page = requests.get(hyperLink)
    soup = BeautifulSoup(page.content, "htmp.parser")
    for tr_tag in soup.find("tr", attrs = {"class":"fact_row"}):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div",attrs = {"class": "value"})[0].contents[0])
            except:
                temp_list.append("")
            new_planet_data.append(temp_list)

scrape()
for data in planet_data:
    scrape_more_data(data[5])

final_planet_data = []

for index, data in enumerate(planet_data):
    final_planet_data.append(data+ final_planet_data[index])

with open("final.csv","w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(final_planet_data)

    
with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)
scrape()