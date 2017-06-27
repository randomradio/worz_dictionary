# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


class LongmanParser(object):
    """
    this parser is dedicated to parse the html content from
    ldoceonline.com
    in order to get to the word page,
    we have to crawl goups links and group results links
    """

    def __init__(self, soup):
        # check if the soup is tasty
        if isinstance(soup, BeautifulSoup):
            raise TypeError()
        self.soup = soup

    def get_group_list_links(self):
        """
        parse group list links from beautiful soup object
        css selector: ul.browse_groups > li
        """
        group_list = self.soup.find_all('ul', class_='browse_groups')
        if group_list:
            for ul in group_list:
                lis = ul.find_all('li')
                return [li.find('a').get('href') for li in lis]
        else:
            return []

    def get_group_results_links(self):
        """
        parse group list links result, find link to each word
        css selector: ul.browse_results > li
        """
        group_results = self.soup.find_all('ul', class_='browse_results')
        if group_results:
            for ul in group_results:
                lis = ul.find_all('li')
                return [li.find('a').get('href') for li in lis]
        else:
            return [] 
