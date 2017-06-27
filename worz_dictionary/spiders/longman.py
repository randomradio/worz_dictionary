# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from worz_dictionary.custom_parsers import custom_html_parser
from worz_dictionary.items import WorzRawDictionaryItem 
import scrapy
import string


class LongmanSpider(scrapy.Spider):
    """
    This spider crawls longman dictionary
    return resulst as dictionary for process in the next steps
    """

    name = 'longman'
    allowed_domains = ['ldoceonline.com']
    start_url = 'http://ldoceonline.com/'

    def start_requests(self):
        # all information we need in the dictionary is words starting with a to words starting with z
        for letter in string.ascii_lowercase:
            yield scrapy.Request(self._letter_url(letter))

    def parse(self, response):
        # reach the first page, find all lead word of groups
        # scrapy will recognize the result from yield
        # and will continue to scrape 
        # if the returned result is an instance of scrapy.Request

        html = response.body
        soup = BeautifulSoup(html, 'html.parser')
        longman_parser = custom_html_parser.LongmanParser(soup)

        # try to parse both types of links
        group_list_links = longman_parser.get_group_list_links()
        group_result_links = longman_parser.get_group_results_links()
        # check whether the links is properly parsed, if not
        # maybe reached the word page, try to parse words
        if group_list_links:
            for link in group_list_links:
                yield scrapy.Request(link)
        elif group_result_links:
            for link in group_result_links:
                yield scrapy.Request(link)
        else:
            try:
                #{TODO} wrap this part into LongmanParser as well.
                word = soup.find('h1', class_='pagetitle').get_text()
                raw_html = soup.find('div', class_='dictionary').get_text()
                result = WorzRawDictionaryItem(
                    source="longman",
                    word=word,
                    raw_html=raw_html,
                    error='',
                )
                yield result
            except Exception as e:
                # for exception, we keep running the crawler but log the error message in item
                result = WorzRawDictionaryItem(
                    source="longman",
                    word='',
                    raw_html='',
                    error=str(e),
                )
                yield result

    def _letter_url(self, letter):
        return '{0}/browse/english/{1}/'.format(self.start_url, letter)
