import requests
import requests.exception as RequestException
import network_statistics as net_stats
import exchange_statistics as ex_stats
import npi_abstraction as abstract 

class run_npi():

	def start_npi():
		run_time = time.time()
		net_time = run_time
		ex_time = run_time

		net_stats.blockchain_stats()
		net_stats.mining_stats()
		net_stats.network_stats()
        ex_stats.indicator_scraper()

        network_performance_index(net_time, ex_time)

    def network_performance_index(net_time, ex_time):
    	update_net, timer_net = abstract.update_network_monitor(net_time)
    	
    	if update_net == True:
    		net_time = timer_net
    		upload_network_statistics()
    	else:
    		print("No Data Uploaded")

    	update_ex, timer_ex = abstract.update_exchange_monitor(ex_time)

    	if update_ex == True:
    		ex_time = timer_ex
    		upload_exchange_statistics()
        else:
        	print("No Data Uploaded")

    def upload_network_statistics():
        url = http://10.0.0.X:8000
        charts = ["my-wallet-n-users", "output-volume", "utxo-count",    "mempool-size", "mempool-growth", "mempool-count", "n-transactions", "n-unique-addresses", "transactions-pers-second", "cost-per-transaction", "transaction-fees", "hash-rate", "difficulty", "miners-revenue", "avg-block-size", "n-transactions-per-block", "median-confirmation-time", "market-price", "market-cap", "trade-volume", "total-bitcoins"]
        log = csv.writer(open("upload-errors.csv", "w"))
        log.writerow(["Errors"])

        for i in charts:
        	marker = open[i] + "csv"
            files = {"upload_file":marker, "rb"}
            data = {"upload_file":marker, "DB":"Apache", "OUT":"csv"}
            
            try:
                response = 	requests.post(url, files=files, data=data)
            except RequestException as e:
            	log.writerow([e])

    def upload_exchange_statistics():
    	log = csv.writer(open("upload-errors.csv", "w"))
        log.writerow(["Errors"])
        url = http://10.0.0.X:8000

        oscillator_file = {"upload_file":"oscillator-indicators.csv", "rb"}
        oscillator_data = {"upload_file":"oscillator-indicators.csv", "DB":"Apache", "OUT":"csv"}
        
        moving_avgs_file = {"upload_file":"moving-avgs.csv", "rb"}
        moving_avgs_data = {"upload_file":"moving-avgs.csv","DB":"Apache", "OUT":"csv"}

        try:
            oscillator_response = requests.post(url, files=oscillator_file, data=data)
        except RequestException as e:
            log.writerow([e])

        try:
        	moving_avgs_response = requests.post(url, files=moving_avgs_file, data=data)
        except RequestException as e:
        	log.writerow([e])

    if __name__ == __main__:
    	start_npi()