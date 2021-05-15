


### trying out Scrapy - web scraping framework


#### Setup your env
```
# using pyenv
pyenv virtualenv 3.9.4 webscraper
pip install -r requirements.txt

# or with Conda
conda create -n webscraper  python=3.9.4
conda install --file requirements.txt

```


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
cd starwars
scrapy crawl quotes -O starwars40.json

```


