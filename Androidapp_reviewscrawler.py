"""
A crawler to get reviews from specified apps.

I have created a list of top apps in file 'appsid'. This list is created
on a particular day of july month and it contains 3000 apps ids with their
category rank less than 10 on that specific day.

After running the crawler: Two files are created positive.txt and negative.txt
"""

import re
import sys
import requests
from lxml import html


def get_review(url):
    url = 'https://play.google.com/store/apps/details?id='+url+'&hl=en'
    try:
        response = requests.get(url, timeout=1.0)
    except requests.exceptions.Timeout as e:
        print('Connection Timeout')
        return
    except requests.exceptions.ConnectionError as e:
        print('No Internet connection')
        sys.exit(-1)
    #parse the body into tree
    parsed = html.fromstring(response.text)
    
    #data extraction with xpath
    reviews = parsed.xpath('//div[@class="single-review"]//div[@class="review-body"]')
    if not reviews:
        return
    ratings = parsed.xpath('//div[@class="single-review"]//div[@class="tiny-star star-rating-non-editable-container"]/@aria-label')
    #basic processing/stripping the string and taking only 5star and 1,2 star reviews
    for index,rev in enumerate(reviews):
        if '5' in ratings[index]:
            rev = re.sub('[^A-Za-z0-9.,\' ]+', '', rev.text_content().replace('  Full Review  ','').strip())

            if len(rev) > 250:
                continue
            pos.write(rev + '\n')

        if '2' in ratings[index] or '1' in ratings[index]:
            rev = re.sub('[^A-Za-z0-9.,\' ]+', '', rev.text_content().replace('  Full Review  ','').strip())

            if len(rev) > 250:
                continue
            neg.write(rev + '\n')
    return

try:
    with open('appsid', 'r') as aid:
        urls = [i for i in aid.read().split('\n')]

except IOError:
    print('Error while opening App\'s ID file. make sure that\
    you have a file named "appsid" in the irectory of this\
    scrip and you have right permissions to access file. \nExiting...')

if __name__ == '__main__':
    #run it till there are ids in appsid file
    with open('positive.txt', 'w') as pos, open('negative.txt', 'w') as neg:
        length = len(urls)
        while length:
            try:
                for url in urls:
                    get_review(url)
                    print(str(length) + ' apps left')
                    length -= 1
            except IOError as e:
                print('Operation Failed Error...')
                pass

    print('Complete (Y)')
