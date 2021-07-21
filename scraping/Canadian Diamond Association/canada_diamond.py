import csv
from requests_html import HTMLSession



def dataExtractor(url):
    keys = ['Membership Level', 'Organization','First Name','Last Name', 'Address', 'City', 'Province', 'Country', 'Phone', 'Website', 'Type Of Service', 'Postal Code', 'Description','Data_url', 'Email']
    dictionary = dict.fromkeys(keys)
    session = HTMLSession()

    source = session.get(url)
    source.html.render(sleep = 1, timeout=20)
    div_block = source.html.xpath('//*[@class="fieldContainer simpleTextContainer"]')

    #elements = data_block.html.xpath('//*[@class="fieldSubContainer labeledTextContainer"]')

    for div in div_block:
        split_data = div.text.splitlines()
        label = split_data[0].title()
        data = ' '.join([str(elem) for elem in split_data[1:]]) 

        #print('LABEl:{}'.format(label))
        #print('DATA:{}'.format(data))

        dictionary[label] = data

    dictionary['Data_url'] = url

    session.close()

    return dictionary
