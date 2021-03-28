## Mission to Mars
This challenge entails scraping data from three different websites and creating a flask app to display this data in an html file. 
1. I created a Jupyter notebook to complete all web scraping and analysis tasks. I marked down details on each step in the `mission_to_mars.ipynb` included in this repository. Where Splinter was used to navigate the sites when needed and BeautifulSoup was used to help find and parse out the necessary data. 
2. I used MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the various urls. I converted the Jupyter notebook into a Python script call `scrape_mars.py` with a function called `scrape` that will excute all the scraping code and return one Python dictioary containing all of the scraped data. 
3. I created a route called `/scrape` that will import `scrape_mars.py` script and call the `scrape` function.
4. Stored the return value in Mongo as a Python dictionary. 
5. I created a root route `/` that will query the Mongo database and pass the scraped data into and HTML template to display the data. 
6. Finally, I took screenshots of my final application: 
![image](https://user-images.githubusercontent.com/74943070/112769967-21642180-8ff2-11eb-92a0-8e1f5e7c4a21.png)
![image](https://user-images.githubusercontent.com/74943070/112770041-9899b580-8ff2-11eb-815d-398b1ded0494.png)
