# Webscrapping

I used BeautifulSoup, splinter and pandas to gather information from these 5 websites :
Scraping:

https://mars.nasa.gov/news/ 
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars 
https://twitter.com/marswxreport?lang=en 
https://space-facts.com/mars/ 
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars 

I then deployed a Flask app to run all of the scraping code. All the collected data was stored in a MongoDB database. 

Finally, the entire process can be access from the HTML file called 'index.html'.
