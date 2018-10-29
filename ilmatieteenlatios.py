from lxml import html
import requests

page = requests.get('https://ilmatieteenlaitos.fi/saa/tampere')
tree = html.fromstring(page.content)

lampotila = tree.xpath('//div[@class="daily-meteogram-container day-0 selected"]'\
'/table/tbody/tr[@class="meteogram-temperatures"]/td/div/text()')

paivamaara2 = tree.xpath('//div[@class="daily-meteogram-container day-0 selected"]'\
'/table/thead/tr[@class="meteogram-dates"]/td/div/span/text()')

aika = tree.xpath('//div[@class="daily-meteogram-container day-0 selected"]'\
'/table/thead/tr[@class="meteogram-times"]/td/div/span/text()')

print(paivamaara2[0])
for i in range(len(aika)):
    print(aika[i], ": ",lampotila[i])


for i in range(1,14):
    lampotilat = tree.xpath('//div[@class="daily-meteogram-container day-{}"]'\
    '/table/tbody/tr[@class="meteogram-temperatures"]/td/div/text()'.format(i))

    paivamaara = tree.xpath('//div[@class="daily-meteogram-container day-{}"]'\
    '/table/thead/tr[@class="meteogram-dates"]/td/div/span/text()'.format(i))

    ajat = tree.xpath('//div[@class="daily-meteogram-container day-{}"]'\
    '/table/thead/tr[@class="meteogram-times"]/td/div/span/text()'.format(i))

    if(ajat==[]):
        pass
    else:
        print(paivamaara[0])
        for i in range(len(ajat)):
            print(ajat[i], ": ", lampotilat[i])
