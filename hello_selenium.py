from selenium import webdriver
import pandas as pd
import time

driver_location = '/usr/bin/chromedriver'
binary_location = '/usr/bin/google-chrome'

options = webdriver.ChromeOptions()
options.binary_location = binary_location

driver = webdriver.Chrome(executable_path=driver_location,options=options)

search_string = "Japan"
search_url = f"https://www.google.com/search?q={search_string}"

print(f"search_url: {search_url}")

driver.get(search_url)
time.sleep(5)

titles = driver.find_elements_by_xpath("//div[@class='yuRUbf']//h3[@class='LC20lb MBeuO DKV0Md']")

top_5_titles = []
count = 0
for title in titles:
    if title.text:
        top_5_titles.append(title.text)
        count += 1
        if count >= 5:
            break
for title in top_5_titles:
    print("Title: ", title)

links = driver.find_elements_by_xpath("//div[@class='yuRUbf']//div[@class='TbwUpd NJjxre']")

top_5_links = []
count = 0
for link in links:
    if link.text:
        top_5_links.append(link.text)
        count += 1
        if count >= 5:
            break

for t in top_5_links:
    print("Link: ", t)

descriptions = driver.find_elements_by_xpath("//div[@class='VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc']")

top_5_descriptions = []
count = 0
for link in descriptions:
    if link.text:
        top_5_descriptions.append(link.text)
        count += 1
        if count >= 5:
            break

for t in top_5_descriptions:
    print("Description: ", t)

df = pd.DataFrame({
    "Title": top_5_titles,
    "Links": top_5_links,
    "Descriptions": top_5_descriptions
})

print(df.head(10))

df.to_csv(f"top_5_results_for_{search_string}.csv", index=False)

time.sleep(100)
driver.quit()