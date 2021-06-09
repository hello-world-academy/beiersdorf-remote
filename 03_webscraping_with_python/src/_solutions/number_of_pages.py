characters_per_page = 3000
pages = round(len(reviews)/characters_per_page, 1)
print(f'We have retrieved approximately {pages} pages of information')
