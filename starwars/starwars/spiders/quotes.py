import scrapy
import logging


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['starwars.com']

    start_urls = ['https://www.starwars.com/news/40-memorable-star-wars-quotes']
    # start_urls = ['file:///private/var/folders/ny/srt271t92696l16ss1dq493r0000gn/T/tmp8r1_gic9.html']

    def parse(self, response):

        yield {
            "quote": response.xpath('//section[@class="entry-content"]/p[*]/b/text()').extract(),
            "url": response.url       
        }


    def clean_text(self, input_str):
        
        self.logger.info(f"type of input: {type(input_str)}")
        self.logger.info(input_str)
        #flatten the lists
        if type(input_str) is not None:
            if type(input_str) == list:
                self.logger.info("flattening list")
                flat_str = " ".join(input_str)
                self.logger.info(flat_str)
                self.logger.info(f"type after string conversion: {type(flat_str)}")
                cleaned_text = self.replace_new_line(flat_str)
            else:
                cleaned_text = self.replace_new_line(input_str)

        return cleaned_text        

    def replace_new_line(self, input_str):
        if type(input_str) == str :
            self.logger.info("cleaning text, checking for '\n'")
            self.logger.info(input_str.find('\n'))
            if input_str.find("\n") != -1:
                self.logger.info("\n found in input")
                cleaned_str = str.strip(input_str.replace("\n", ""))
                self.logger.info(f"input: {input_str} \n cleaned: {cleaned_str}")
                return cleaned_str
        
        else:
            self.logger.info("No string type found, no cleaning to be done")
            return input_str
