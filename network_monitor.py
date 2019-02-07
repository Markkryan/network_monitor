import psutil


def main():
    network_res = _retrive_resources()
    #print(network_res)
    print(_retrieve_et_resource(network_res))
    print(_retrieve_wifi_resource(network_res))

def _retrive_resources():
    network_res = psutil.net_io_counters(pernic=True)
    return network_res

def _retrieve_et_resource(resource):
    return resource["Ethernet"]

def _retrieve_wifi_resource(resource):
    return resource["Wi-Fi"]

if __name__ == "__main__":
    main()