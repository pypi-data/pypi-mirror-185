"""These settings only use for scrapy shell."""

BOT_NAME = r"GetNovel"
ROBOTSTXT_OBEY = True
SPIDER_MODULES = ["getnovel.app.spiders"]
USER_AGENT = r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"
COOKIES_DEBUG = True
