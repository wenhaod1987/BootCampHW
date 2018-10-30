
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

import time
from splinter import Browser


# In[35]:
def scrape():

	# start scraping first site, NASA Mars News
	nasa_url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=False)
	browser.visit(nasa_url)


	# In[36]:


	nasa_html=browser.html
	soup_nasa = bs(nasa_html, 'html.parser')
	result=soup_nasa.find('div',class_='content_title')
	news_title = result.find('a').text
	news_p=soup_nasa.find('div',class_='article_teaser_body').text

	
	


	# In[34]:


	#scraping 2nd webpage and get the url for feature image
	image_url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
	#executable_path = {'executable_path': 'chromedriver.exe'}
	#browser = Browser('chrome', **executable_path, headless=False)
	browser.visit(image_url)
	nasa_image=browser.html
	soup_image = bs(nasa_image, 'html.parser')
	result=soup_image.find('a',class_='button fancybox')['data-fancybox-href']

	pic_url=f"https://www.jpl.nasa.gov/{result}"


	# In[39]:


	#scraping twitter page to find the weather of Mars
	twitter_url="https://twitter.com/marswxreport?lang=en"
	respond_twitter = requests.get(twitter_url)
	soup_twitter = bs(respond_twitter.text, 'html.parser')
	twitter_result = soup_twitter.find('div',class_='js-tweet-text-container')
	mars_weather=twitter_result.find('p').text


	# In[55]:


	#scraping Mars fact

	fact_url="https://space-facts.com/mars/"
	respond_fact=requests.get(fact_url)
	soup_fact = bs(respond_fact.text,'html.parser')
	table_result = soup_fact.find('table')
	table=pd.read_html(str(table_result))
	table_df = pd.DataFrame({"Description":table[0][0],
	                        "Value":table[0][1]})
	table_html=table_df.to_html()


	# In[57]:


	#scraping required features for Mars Hemispheres
	hemi_url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	browser.visit(hemi_url)
	hemi_html=browser.html
	soup_hemi = bs(hemi_html, 'html.parser')


	# In[63]:


	results = soup_hemi.find_all('div',class_='description')
	hemi_url=[]
	title_ls=[]
	img=[]
	hemisphere_image_urls=[]

	# scraping the main website to get all urls and Hemisphere titles
	for result in results:
	    hemi_url.append(f"https://astrogeology.usgs.gov{result.find('a')['href']}")
	    title_ls.append(result.find('h3').text[:-9])

	# visit each url in the list to get the url for each full-size image     
	for url in hemi_url:
	    browser.visit(url)
	    html = browser.html
	    soup = bs(html,'html.parser')
	    result= soup.find('img',class_='wide-image')['src']
	    img.append(f"https://astrogeology.usgs.gov{result}")

	#combine 2 list into the required list of dictionary
	for x in range(4):
	    hemisphere_image_urls.append({'title':title_ls[x], 'img_url': img[x]})



	    
	    


	# In[64]:


	#create the dictionary to return:
	final_dic = {
	    'news_title': news_title,
	    'news_p': news_p,
	    'featured_image_url': pic_url,
	    'mars_weather':mars_weather,
	    'mars_fact_table':table_html,
	    'hemisphere_image_urls':hemisphere_image_urls
	}

	return final_dic;


# In[65]:




