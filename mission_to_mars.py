
    #scrape latest news stories from NASA mars site
    # So dependant
    from bs4 import BeautifulSoup
    import requests
    import pymongo

    # EDIT: skipping Mongo til later.
    #conn = 'mongodb://localhost:27017'
    #client = pymongo.MongoClient(conn)

    # Mongo is but collection in database of life....
    #db = client.Mars_db
    #collection = db.mars_news

    #let's start with our nasa news
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    mars_news_raw = requests.get(url)
    soup = BeautifulSoup(mars_news_raw.text, 'html.parser')
    print(soup.prettify())

    #Let's go grab those articles out of lists, then we roll
    nasa_articles = soup.find_all("div", class_="slide")
    mars_news = []
    for article in nasa_articles:
        article_title = article.find("div", class_="content_title").text
        article_content = article.find("div", class_="rollover_description_inner").text
        mars_news_dict = {
            "title" : article_title,
            "content" : article_content
        }
        print("----------------")
        print(article_title)
        print(article_content)
        mars_news.append(mars_news_dict)
        #collection.insert_one(mars_news_dict)
        #print("added to db")
    print(mars_news)   
    #Stick it all into Mongo
    #Collect it all up
    #collection.insert_one(mars_news)


    #Ok, let's use splinter.
    #Get current featured image url from here:
    #https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars


    #import splinter, etc
    from splinter import Browser
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    #go to the URL
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)

    #Navigate to the full image
    browser.click_link_by_partial_text('FULL IMAGE')

    #soup it up
    image_html = browser.html
    image_soup = BeautifulSoup(image_html, 'html.parser')

    #grab that image
    image_ext = image_soup.find('img', {'class': 'fancybox-image'})['src']

    featured_image_url = "https://www.jpl.nasa.gov" + image_ext
    #image_link = image_soup.find("div", class_="fancybox-inner")
    print(featured_image_url)
    image_dict = {"featured_image" : featured_image_url}

    #get it in mongo
    #collection = db.mars_images
    #collection.insert_one(image_dict)

    #Ok! On to Twitter!
    #Could scrape like the others, but we learned tweepy. Let's refresh.
    import tweepy

    from config import api_twitter
    from config import api_twitter_secret
    from config import api_access_token
    from config import api_access_token_secret
    # Your Twitter API Keys
    consumer_key = api_twitter
    consumer_secret = api_twitter_secret
    access_token = api_access_token
    access_token_secret = api_access_token_secret

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    tweets = api.user_timeline("@MarsWxReport", count = 1)
    print(tweets[0]["text"])
    mars_weather_dict = {"mars_weather" : tweets[0]["text"]}


    #Scrape mars facts as a table https://space-facts.com/mars/

    #Wow, I think this is the furthest I've ever gotten into a script without importing Pandas.
    import pandas as pd

    table_url = "https://space-facts.com/mars/"
    mars_facts = pd.read_html(table_url)
    mars_facts = mars_facts[0]

    #damn. That one is so nice and easy.

    #Ok, finally, images and hemispheres
    #USGS site here: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    #I think we go back to splinter, so we can do a nice move between the pages.

    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    hemispheres = ["Cerberus", "Schiaparelli", "Syrtis", "Valles"]
    hemisphere_image_urls = []

    for hemisphere in hemispheres:
        browser.visit(hemisphere_url)
        browser.click_link_by_partial_text(hemisphere)
        hem_html = browser.html
        hem_soup = BeautifulSoup(hem_html, 'html.parser')
        hem_title = hem_soup.find('h2', class_="title").text
        hem_downloads = hem_soup.find('div', class_="downloads")
        hem_url = hem_downloads.find('a')["href"]
        hem_dict = {
            "title":hem_title,
            "image":hem_url
        }
        hemisphere_image_urls.append(hem_dict)
        print("{} added successfully.".format(hem_title))
        


# In[25]:


hemisphere_image_urls

