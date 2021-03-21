# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars News
# This section scrapes the [NASA Mars News Site](https://mars.nasa.gov/news/) to collect the latest News Title and Paragraph Text. 

def scrape():
    browser = init_browser()
    
    # scrape the site using the URL
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    latest_news_title = soup.body.article.a.h3.text
    
    latest_news_paragraph = soup.body.article.a.div.text

    
    # ### JPL Mars Space Images - Featured Image
    # In this section, splinter is used at JPL Featured Space Image [here](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html) to find the image url for the current Featured Mars Image.

    # Scrape the site using the URL2
    url2 = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url2)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')


    a = soup.body.div.find('a', class_="showimg fancybox-thumbs")
    link = a['href']
    featured_image = print('https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/'+link)


    # ### Mars Facts
    # In this section, the Mars Facts webpage [here](https://space-facts.com/mars/) is scraped with Pandas to get the table containing facts about the planet including Diameter, Mass, etc. Pandas is then used to convert the data to a HTML table string.

    # URL3 is 3rd page to be scraped
    url3 = 'https://space-facts.com/mars/'

    tables = pd.read_html(url3)

    df = tables[0]

    html_table = df.to_html()

    html_table.replace('\n', '')

    #df.to_html('table.html')     Don't think I need the table.html. Just the html table string, named html_table.


    # ### Mars Hemispheres
    # The USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) was visited to obtain high resolution images for each of Mars' hemispheres. Python dictionary was created to store the data using the keys `img_url` and `title`. The dictionary was appended with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.


    # Scrape the site using the URL2
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url4)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    images = soup.find_all('div', class_="item")
    
    hemisphere_image_urls = []

    links = browser.find_by_css('a.product-item img')

    for i in range(len(links)):
        hemisphere = {}
        browser.find_by_css('a.product-item img')[i].click()
        sample = browser.links.find_by_text('Sample').first
        hemisphere['img_url'] = sample['href']
        hemisphere['title'] = browser.find_by_css('h2.title').text
        hemisphere_image_urls.append(hemisphere)
        browser.back()


    # Store all scraped data in Python dictionary. 
    




    browser.quit()




