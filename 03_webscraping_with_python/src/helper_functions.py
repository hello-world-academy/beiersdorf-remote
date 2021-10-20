# MISC functions for webscraping


def extract_text_from_soup(soup):
    """
    Function to extract user review text information from the site https://www.makeupalley.com/
    """
    # fetch the items of interest
    items = soup.find_all("div", {"class": "__ReviewTextReadMoreV2__"})
    # iterate over the itmes and extract text information
    review_text = " ".join([x["data-text"] for x in items])
    return review_text


def generate_urls(url, pages):
    """
    Function to extend an url with the form "?page=i#reviews", where i is is an integer
    : url: string
    : pages: tuple(start, end)
    """
    r = range(pages[0], pages[1] + 1)
    urls = []
    for i in r:
        urls.append(f"{url}?page={i}#reviews")
    return urls
