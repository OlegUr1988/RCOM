def CfmToE3m3_dayCcoms():
    return 0.0407758742743877

def M3_hourToE3m3_day():
    # 24 hours divided by 1000
    return 24.0 / 1000.0

def M3_minToE3m3_day():
    return (60.0 * 24.0) / 1000.0

def M3_secToE3m3_day():
    # Value is 86.4 (60 seconds in 1 minute, 60 minutes in 1 hour, 24 hours divided by 1000). 
    return (60.0 * 60.0 * 24.0) / 1000.0

def MmscfdToE3m3_dayCcoms():
    return 28.31658

def CfmToM3_sec():
    return 0.00047194745

def E3m3_dayToM3_sec():
    #  e3m3/d = 1000 * M3/s
    return 1000.0 * 0.000011574074

def M3_hourToM3_sec():
    return 0.000277778

def M3_minToM3_sec():
    return 0.01666667

def MmscfdToM3_sec():
    return 0.32774

def ScfdToM3_sec():
    return 0.32774 * 1E-6

def ScfmToM3_sec():
    return 0.000472