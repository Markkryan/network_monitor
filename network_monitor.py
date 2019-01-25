import psutil
import logger

def main():
    network_res = _retrive_resources()
    print(network_res)

def _retrive_resources():
    network_res = psutil.net_io_counters(pernic=true)
    return network_res

if __name__ == "__main__":
    main()