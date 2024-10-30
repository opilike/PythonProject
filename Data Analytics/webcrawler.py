"""
File: webcrawler.py
Name: Jason
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0'
        }
        response = requests.get(url, headers=header)
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        # ----- Write your code below this line ----- #

        # just find the only one table that class is t-stripe
        table = soup.find('table', {'class': 't-stripe'})
        #  if table exist
        if table:
            male_total, female_total = extract(table)
            print(f"Male Number: {male_total}")
            print(f"Female Number: {female_total}")


#  extract Male Number & Female Number
def extract(table):
    male_total = 0
    female_total = 0
    # # extract all tar exclusive first <tr>
    # trs = table.find_all('tr')[1:]
    # for tr in trs:
    #     tds = tr.find_all('td')
    #     #  make sure have 4 td in tr
    #     if len(tds) == 5:
    #         #  make total and replace , to be null, make 1,000 can  be 1000
    #         male_total += int(tds[2].text.replace(',', ''))
    #         female_total += int(tds[4].text.replace(',', ''))
    # return male_total, female_total

    # text = table.tbody.text.split()
    # # print(text)
    # for i in range(1, len(text)):
    #     if i >= 995:
    #         break
    #     if i % 5 == 2:
    #         male_total += int(text[i].replace(',',''))
    #     elif i % 5 == 4:
    #         female_total += int(text[i].replace(',', ''))
    # return male_total, female_total

    text = table.text.split()
    print(text)
    for i in range(1, len(text), 5):
        if i + 4 < len(text):
            try:
                male_total += int(text[i + 2].replace(',', ''))
                female_total += int(text[i + 4].replace(',', ''))
            except ValueError:
                continue
        if i >= 995:
            break
    return male_total, female_total

if __name__ == '__main__':
    main()
