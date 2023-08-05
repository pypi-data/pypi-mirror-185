"""Get novel on domain ptwxz.

.. _Web site:
   https://www.ptwxz.com

"""

from scrapy import Spider
from scrapy.exceptions import CloseSpider
from scrapy.http import Response

from getnovel.app.itemloaders import InfoLoader, ChapterLoader
from getnovel.app.items import Info, Chapter


class PtwxzSpider(Spider):
    """Define spider for domain: ptwxz.

    Attributes
    ----------
    name : str
        Name of the spider.
    start_urls : list
        List of url to start crawling from.
    sa : int
        The chapter index to start crawling.
    so : int
        The chapter index to stop crawling after that.
    c : str
        Language code of novel.
    """

    name = "ptwxz"

    def __init__(self, u: str, start: int, stop: int, *args, **kwargs):
        """Initialize attributes.

        Parameters
        ----------
        u : str
            Url of the novel information page.
        start: int
            Start crawling from this chapter.
        stop : int
            Stop crawling after this chapter, input -1 to get all chapters.
        """
        super().__init__(*args, **kwargs)
        self.start_urls = [u]
        self.sa = int(start)
        self.so = int(stop)
        self.c = "zh"  # language code

    def parse(self, res: Response, *args, **kwargs):
        """Extract info and send request to the table of content.

        Parameters
        ----------
        res : Response
            The response to parse.

        Yields
        ------
        Info
            Info item.
        Request
            Request to the table of content.
        """
        yield get_info(res)
        yield res.follow(
            url=res.xpath('//*[@id="content"]//a[1]/@href').get(),
            callback=self.parse_toc,
        )

    def parse_toc(self, res: Response):
        """Extract link of the start chapter.

        Parameters
        ----------
        res : Response
            The response to parse.

        Yields
        ------
        Request
            Request to the start chapter.
        """
        yield res.follow(
            url=res.xpath(f'(//div[@class="centent"]//a/@href)[{self.sa}]').get(),
            meta={"id": self.sa},
            callback=self.parse_content,
        )

    def parse_content(self, res: Response):
        """Extract content.

        Parameters
        ----------
        res : Response
            The response to parse.

        Yields
        ------
        Chapter
            Chapter item.

        Request
            Request to the next chapter.
        """
        yield get_content(res)
        neu = res.xpath("//div[3]/a[3]/@href").get()
        if ("i" in neu) or (res.meta["id"] == self.so):
            raise CloseSpider(reason="done")
        yield res.follow(
            url=neu,
            meta={"id": res.meta["id"] + 1},
            callback=self.parse_content,
        )


def get_info(res: Response) -> Info:
    """Get novel information.

    Parameters
    ----------
    res : Response
        The response to parse.

    Returns
    -------
    Info
        Populated Info item.
    """
    ihref = res.xpath('//*[@id="content"]//td[2]//img/@src').get()
    r = InfoLoader(item=Info(), response=res)
    r.add_xpath("title", '//*[@id="content"]//tr[1]//h1/text()')
    r.add_xpath("author", '//*[@id="content"]//tr[2]/td[2]/text()')
    r.add_xpath("types", '//*[@id="content"]//tr[2]/td[1]/text()')
    r.add_xpath("foreword", '//*[@id="content"]//td[2]//text()[4]')
    r.add_value("image_urls", res.urljoin(ihref))
    r.add_value("url", res.request.url)
    return r.load_item()


def get_content(res: Response) -> Chapter:
    """Get chapter content.

    Parameters
    ----------
    res : Response
        The response to parse.

    Returns
    -------
    Chapter
        Populated Chapter item.
    """
    r = ChapterLoader(item=Chapter(), response=res)
    r.add_value("id", str(res.meta["id"]))
    r.add_value("url", res.url)
    r.add_xpath("title", "//h1/text()")
    r.add_xpath("content", "//body/text()")
    return r.load_item()
