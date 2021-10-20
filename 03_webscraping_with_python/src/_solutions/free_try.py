import time
import random
from bs4 import BeautifulSoup
import requests

# Set the URL
url = "https://www.makeupalley.com/product/showreview.asp/ItemId=148506/Visage-Q10-Plus-Anti-Wrinkle-Night-Cream/NIVEA/Moisturizers"
# Number of pages
max_pagination = 9
urls = hf.generate_urls(url=url, pages=(1, max_pagination))
# Retrieve the data
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;     x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}
reviews = ""
for url in urls:
    print(f"Processing url {url}")
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    text = hf.extract_text_from_soup(soup)
    reviews = reviews + " " + text
    print(f"There are {len(text.split())} words extracted.\n")
    time.sleep(random.randint(0, 1) + random.random())

# Create and generate a word cloud image:
wordcloud = WordCloud(
    background_color="white",
    max_words=60,
    mode="RGB",
    relative_scaling=0.5,
    random_state=42,
).generate(reviews)

# Display the generated image:
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
