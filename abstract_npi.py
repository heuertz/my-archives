import time
import network_statistics as net_stats
import exchange_statistics as ex_stats

class npi_abstraction():

    def update_network_monitor(time_monitor):
	    check_time = time.time()
	    if (check_time - time_monitor) >= 22000:
	        try:
	            net_stats.update_network_stats()
	            print("Network Update Successful")

	            return True

	        except:
		        print("Network Update Failed")

		        return False

        return check_time

    def update_exchange_monitor(time_exchange):
    	check_time = time.time()
    	if (check_time - time_exchange) >= 600:
    		try:
    			ex_stats.update_exchange_stats()
    			print("Exchange Update Successful")
    			
    			return True

    	    except:
    	    	print("Exchange Update Failed")
    	    	
    	    	return False

    	return check_time