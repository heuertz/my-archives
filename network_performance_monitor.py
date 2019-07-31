import csv
from requests import get
from requests.exceptions import RequestException

class network_statistics():

    def blockchain_stats():
        response = requests.get("https://api.blockchain.info/stats")
        response_string = str(response)
        format_response = response_string.replace(";", "/n")

        with open("blockchain-stats", "w") as file:
            file.writelines(format_response)

    def mining_stats():
        response = requests.get("https://blockchain.info/pools?timespan=2days")
        response_string = str(response)
        format_response = response_string.replace(";", "/n")

        with open("pool-stats", "w") as file:
             file.writelines(format_response)

    def network_stats():
        charts = ["my-wallet-n-users", "output-volume", "utxo-count",    "mempool-size", "mempool-growth", "mempool-count", "n-transactions", "n-unique-addresses", "transactions-pers-second", "cost-per-transaction", "transaction-fees", "hash-rate", "difficulty", "miners-revenue", "avg-block-size", "n-transactions-per-block", "median-confirmation-time", "market-price", "market-cap", "trade-volume", "total-bitcoins"]

        for i in charts:
            file = csv.writer(open(charts[i] + ".csv", "w"))
            file.writerow(["Hour Time", "Hour Data", "Day Time", "Day Data", "Week Time", "Week Data", "Month Time", "Month Data", "Year Time", "Year Data"])
            log = csv.writer(open("blockchain-info-errors.log"))
            log.writerow("Errors")
            
            try:
                response_hour_x, response_hour_y = requests.get("https://api.blockchain.info/charts/{0}?timespan=1hour&rollingAverage=1minute&format=csv".format(charts[i]))
            except RequestException as e:
                log.writerow([e])

            try:
                response_day_x, response_day_y = requests.get("https://api.blockchain.info/charts{0}?timespan=1day&rollingAverage=24minutes&format=csv".format(charts[i]))
            except RequestException as e:
                log.writerow([e])

            try:
                response_week_x, response_week_y = requests.get("https://api.blockchain.info/charts{0}?timespan=1week&rollingAverage=3hours&format=csv".format(charts[i]))
            except RequestException as e:
                log.writerow([e])

            try:
                response_month_x, response_month_y = requests.get("https://api.blockchain.info/charts{0}?timespan=1month&rollingAverage=12hours&format=csv".format(charts[i]))
            except RequestException as e:
                log.writerow([e])

            try:
                response_year_x, response_year_y = requests.get("https://api.blockchain.info/charts{0}?timespan=1year&rollingAverage=6days&format=csv".format(charts[i]))
            except RequestException as e:
                log.writerow([e])

            file.writerows([response_hour_x, response_hour_y, None, None, None, None, None, None, None, None])
            file.writerows([None, None, response_day_x, response_day_y, None, None, None, None, None, None])
            file.writerows([None, None, None, None, response_week_x, response_week_y, None, None, None, None])
            file.writerows([None, None, None, None, None, None, response_month_x, response_month_y, None, None])
            file.writerows([None, None, None, None, None, None, None, None, response_year_x, response_year_y])

    def update_network_stats():
    	os.remove("blockchain-stats")
    	blockchain_stats()
    	os.remove("pool-stats")
    	mining_stats()
    	charts = ["my-wallet-n-users", "output-volume", "utxo-count",    "mempool-size", "mempool-growth", "mempool-count", "n-transactions", "n-unique-addresses", "transactions-pers-second", "cost-per-transaction", "transaction-fees", "hash-rate", "difficulty", "miners-revenue", "avg-block-size", "n-transactions-per-block", "median-confirmation-time", "market-price", "market-cap", "trade-volume", "total-bitcoins"]

        for i in charts:
    	    os.remove(charts[i] + ".csv")

    	network_stats()