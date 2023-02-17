from selenium import webdriver

def webSearch(query):
    search_string = query
    search_string = search_string.replace(' ', '+')
    browser = webdriver.Chrome('chromedriver')
    for i in range(1):
    	matched_elements = browser.get("https://www.google.com/search?q=" +
    									search_string + "&start=" + str(i))


webSearch("youtube")