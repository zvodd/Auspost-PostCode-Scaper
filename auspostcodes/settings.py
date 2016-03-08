# -*- coding: utf-8 -*-

# Scrapy settings for auspostcodes project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'auspostcodes'

SPIDER_MODULES = ['auspostcodes.spiders']
NEWSPIDER_MODULE = 'auspostcodes.spiders'

DOWNLOAD_DELAY = 0.25

POSTCODE_PAGES_JSON = 'postcode_pages.json'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'auspostcodes (+http://www.yourdomain.com)'
