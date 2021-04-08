


### trying out Scrapy - web scraping framework


#### One Time Setup for the scrapy project
```
scrapy startproject starwars
```


#### Test out the selectors  in Scrapy using scrapy shell
```
scrapy shell
fetch('your url')
view (response)
#test out the xpath selector
response.xpath(".//span[@id='priceblock_ourprice']/text()").extract_first()
```


#### Try out the spider

To save the output to a json file.
The new output is appended to the file.
```
cd starwars
scrapy crawl quotes -o starwars40.jl
```

To crawl and overwrite the file.
```
cd v1
scrapy crawl quotes -O starwars40.json

```


#### Setup your env
```
pyenv virtualenv 3.9.4 webscraper
pip install -r requirements.txt
```

