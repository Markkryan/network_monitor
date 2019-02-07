import psutil

def main():
    ntwrk_rsc = _retrv_rsc()
    #print(network_res)
    print(_retrv_et_rsc(ntwrk_rsc))
    print(_retrv_wifi_rsc(ntwrk_rsc))

def _retrv_rsc():
    return psutil.net_io_counters(pernic=True)

def _retrv_et_rsc(rsc):
    return rsc["Ethernet"]

def _retrv_wifi_rsc(rsc):
    return rsc["Wi-Fi"]

if __name__ == "__main__":
    main()