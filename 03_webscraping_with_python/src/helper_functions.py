# MISC functions for webscraping

def extract_text_from_soup(soup):
    '''
    Function to extract user review text information from the site https://www.beautyheaven.com.au/
    '''
    # fetch the items of interest
    items = soup.find_all('div', {"class": 'field-item even'})
    review_text = ''
    # iterate over the itmes and extract text information
    for i in range(len(items)):
        content = items[i].find_all('p')
        if i > 2: # exclude first entries as they are not user reviews
            if len(content) >= 1: # do not include empty strings
                text = ' '.join([x.get_text().strip() for x in content])
                review_text = review_text + ' ' + text
    return review_text

def generate_urls(url, pages):
    '''
    Function to extend an url with the form "?page=i", where i is is an integer
    : url: string
    : pages: tuple(start, end)
    '''
    r = range(pages[0], pages[1]+1)
    urls = [url]
    for i in r:
        urls.append(f'{url}?page={i}')
    return urls