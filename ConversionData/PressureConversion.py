# Input to Core Conversion Factors

def BarToKpa():
    return 100.0


def PsiToKpa():
    return 6.895


def AtmToKpa():
    return 101.325


def MmHgToKpa():
    return 0.1333


def Kgf_cm2ToKpa():
    return 98.07


def Lbf_ft2ToKpa():
    return 0.04788


def BarToPsi():
    return 14.50377


def KpaToPsi():
    return 0.1450377


def AtmToPsi():
    return 14.69595


def MmHgToPsi():
    return 0.01933677


def Kgf_cm2ToPsi():
    return 14.22334


def Lbf_ft2ToPsi():
    return 0.006944444


# Input to Core Conversion Factors (CCOMS v2)

def PsiToPa():
    return 6894.76


def BarToPa():
    return 100000.0


def KpaToPa():
    return 1000.0

def PaToKPa():
    return 0.001

def AtmToPa():
    return 101325.0


def MmHgToPa():
    return 133.322


def Kgf_cm2ToPa():
    return 98066.5


def Lbf_ft2ToPa():
    return 47.8803

# Tests for Adhoc Unit Conversions

def PsiToKpaAlt(pressureInPsi):
    return pressureInPsi * PsiToKpa()

def KpaToPsiAlt(pressureInKpa):
    return pressureInKpa * KpaToPsi()

def PaToKPaAlt(pressureInPa):
    return pressureInPa * PaToKPa()    