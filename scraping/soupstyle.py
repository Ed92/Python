import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.txt, 'html.parser')
    elems = soup.select('#newOfferAccordionRow > div > div.a-accordion-row-a11y > a > h5 > div > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip()
    
price = getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/ref=sr_1_1?ie=UTF8&qid=1534529194&sr=8-1&keywords=automate+the+boring+stuff+with+python')

print('The price is ' + price)
