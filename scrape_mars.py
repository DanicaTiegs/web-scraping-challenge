from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit Mars News Data
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    # Why do we do this?
    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the average temps
    news_title = soup.find("div", target="_self").get_text()
    #print(news_title)

    news_p = soup.find("div", class_="article_teaser_body").get_text()
    #print(news_p)

    mars_news = {
    "Title": news_title,
    "Teaser": news_p
    }

    print(mars_news)

    # Visit JPL Mars Space Images 

    # URL of page to be scraped
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url)

    timer.sleep(1)

    browser.links.find_by_partial_text("FULL IMAGE").click()

    timer.sleep(1)

    browser.links.find_by_partial_text("more info").click()

    timer.sleep(1)

    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    featured_image_url = soup.find("figure", class_="lede")
    print(featured_image_url["src"])
    featured_image_url = featured_image_url["src"]

    # Visit Mars Facts 

    # URL of page to be scraped
    url = "https://space-facts.com/mars/"

    print(browser.visit(url))

    html = browser.html

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    mars_facts = pd.read_html(url)
    #print(mars_facts[0])
    mars_facts = mars_facts[0]
    #turns df back into html
    mars_facts = mars_facts.to_html()

    # Visit Hemispheres

    # URL of page to be scraped
url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

browser.visit(url)

timer.sleep(1)

browser.links.find_by_partial_text("Hemisphere Enhanced")[0].click()

timer.sleep(1)

hemisphere = {}

hemisphere["img_url"] = img_url

hemisphere["title"] = title

hempisphere_image_urls.append(hemisphere)

browser.back()

browser.links.find_by_partial_text("Hemisphere Enhanced")[1].click()

timer.sleep(1)

hemisphere = {}

hemisphere["img_url"] = img_url

hemisphere["title"] = title

hempisphere_image_urls.append(hemisphere)

browser.back()

browser.links.find_by_partial_text("Hemisphere Enhanced")[2].click()

timer.sleep(1)

hemisphere = {}

hemisphere["img_url"] = img_url

hemisphere["title"] = title

hempisphere_image_urls.append(hemisphere)

browser.back()

browser.links.find_by_partial_text("Hemisphere Enhanced")[3].click()

timer.sleep(1)

hemisphere = {}

hemisphere["img_url"] = img_url

hemisphere["title"] = title

hempisphere_image_urls.append(hemisphere)

browser.back()

timer.sleep(1)

html = browser.html

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(html, 'html.parser')

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]



# Quite the browser after scraping
browser.quit()

mars_data = {
    "news_p": news_p,
    "news_title": news_title,
    "mars_facts" mars_facts, 
    "featured_image": featured_image_url,
    "hemisphere_image": hemisphere_image_urls
}

# Return results
return mars_data

   