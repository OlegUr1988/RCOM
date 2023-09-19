# Input to Core Conversion Factors
def FToC():
    return 5.0 / 9.0

def KToC():
    return 1.0

def RToC():
    return 5.0 / 9.0

def CToR():
    return 9.0 / 5.0

def FToR():
    return 1.0

def KToR():
    return 9.0 / 5.0

def RToK():
    return 5.0 / 9.0

def RToF():
    return 1.0

def KToF():
    return 9.0 / 5.0

def FToK():
    return 5.0 / 9.0

def CToK():
    return 1.0

# Input to Core Offset Factors

def FToCOffset():
    return -32.0

def KToCOffset():
    return -273.15

def RToCOffset():
    return -491.67

def CToROffset():
    return 491.67

def FToROffset():
    return 459.67

def KToROffset():
    return 0.0

def RToKOffset():
    return 0.0

def RToFOffset():
    return -459.67

def KToFOffset():
    return -273.15

def FToKOffset():
    return 273.15

def CToKOffset():
    return 273.15

# Adhoc Unit Conversions

def CToF():
    return 9.0 / 5.0

def CToFOffset():
    return 32.0

def CToFConverter( temperatureInC):
    return (temperatureInC * CToF()) + CToFOffset()

def RToKAlt( temperatureInR):
    return temperatureInR * RToK() + RToKOffset()

def KToRAlt( temperatureInK):
    return temperatureInK * KToR() + KToROffset()

def FToRAlt( temperatureInF): 
    return temperatureInF * FToR() + FToROffset()

def RToFAlt( temperatureInR):
    return temperatureInR * RToF() + RToFOffset()

def KToFAlt( temperatureInK):
    return (temperatureInK + KToFOffset()) * KToF() + 32

def FToKAlt( temperatureInF):
    return (temperatureInF - 32) * FToK() + FToKOffset()