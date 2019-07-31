import csv
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

class exchange_statistics():
    
    def indicator_scraper():
    	oscillators_file = csv.writer(open("oscillator-indicators.csv", "w"))
    	moving_avg_file = csv.writer(open("moving-avgs.csv", "w"))
    	oscillators_file.writerow(["Name", "Value"])
    	moving_avg_file.writerow(["Name", "Value"])

    	response = requests.get("https://www.tradingview.com/symbols/BTCUSD/technicals/")
    	soup = BeautifulSoup(response.text, "html.parser")

    	oscillators_html = soup.find("div", class_="container-2w8ThMcC- tableWithAction- 20CRQQ8y-")
    	oscillators_values = oscillators_html.select("tr [class='row-3rEbNObt-']")

    	for indicator in oscillators_values:
    		indicator_name = indicator.get("a")
    		indicator_value = indicator.get("td [class='cell-5XzWwbDG]")
    		oscillators_file.writerow([indicator_name, indicator_value])

        moving_avg_html = soup.find("div", class_="container-2w8ThMcC- maTable- 27Z4Dq6y- tableWithAction-20CRQQ8y")
        moving_avgs_values = moving_avg_html.select("tr [class='row-3rEbNOt-']")

        for average in moving_avgs_values:
        	moving_avg_name = average.get("a")
        	moving_avg_value = average.get("td [class='cell-5XzWwbDG']")
        	moving_avg_file.writerow([moving_avg_name, moving_avg_value])

    def update_exchange_stats():
    	indicator_scraper()