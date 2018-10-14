from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd
import time

def init_browser():
    executable_path = {"executable_path":"/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    browser = init_browser()
    mars = {}

    #nasa website
    nasa_url ="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response_nasa = requests.get(nasa_url)
    nasa_soup = BeautifulSoup(response_nasa.text, 'html.parser')

    mars['news_title'] = nasa_soup.find("div", class_="content_title").text
    mars['news_p'] = nasa_soup.find("div", class_="rollover_description_inner").text

    #Use splinter to go to the chosen webpage
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url ="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    jpl_soup = BeautifulSoup(html, "html.parser")

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')


    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    img_url = soup.find("img", class_="main_image")["src"]

    mars['featured_image_url'] = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars" + img_url

    #weather
    weather_url = "https://twitter.com/marswxreport?lang=en"
    response_weather = requests.get(weather_url)
    weather_soup = BeautifulSoup(response_weather.text, 'html.parser')

    weather_tweet = weather_soup.find_all('div', class_="js-tweet-text-container")

    for i in range(10):
        tweets = weather_tweet[i].text
        if "Sol " in tweets:
            mars['mars_weather'] = tweets
            break

    #facts
    mars_fact = "https://space-facts.com/mars/"
    tables = pd.read_html(mars_fact)
    df = tables[0]
    df.set_index([0], inplace=True)
    #df.columns = ['Property','Number']
    mars_fact_html = df.to_html()
    mars_fact_html = mars_fact_html.replace("\n", "")
    mars["mars_fact_html"] = mars_fact_html


    #Mars Hemispheres Cerberus
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    html = browser.html
    hemispheres_soup = BeautifulSoup(html, "html.parser")

    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    img_url = soup.find("img", class_="thumb")["src"]

    Cerberus_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" + img_url

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    html = browser.html
    hemispheres_soup = BeautifulSoup(html, "html.parser")

    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    img_url = soup.find("img", class_="thumb")["src"]

    Schiaparelli_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" + img_url

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    html = browser.html
    hemispheres_soup = BeautifulSoup(html, "html.parser")

    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    img_url = soup.find("img", class_="thumb")["src"]

    Syrtis_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" + img_url

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    html = browser.html
    hemispheres_soup = BeautifulSoup(html, "html.parser")

    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    html_image = browser.html
    soup = BeautifulSoup(html_image, "html.parser")

    img_url = soup.find("img", class_="thumb")["src"]

    Valles_image_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars" + img_url

    mars['hemisphere_image_urls'] = [
    {"title": "Valles Marineris Hemisphere", "img_url": Valles_image_url},
    {"title": "Cerberus Hemisphere", "img_url": Cerberus_image_url},
    {"title": "Schiaparelli Hemisphere", "img_url": Schiaparelli_image_url},
    {"title": "Syrtis Major Hemisphere", "img_url": Syrtis_image_url},
    ]
    hemisphere = mars[0].hemisphere_image_urls
    return mars