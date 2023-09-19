import pandas as pd

def setIntValue(Value,DefaultValue):
    try:
        if pd.isna(Value):
            raise
        return int(Value)
    except:
        return DefaultValue
    
def setBoolValue(Value,DefaultValue):
    try:
        return bool(Value)
    except:
        return DefaultValue
    
def setFloatValue(Value,DefaultValue):
    try: 
        if pd.isna(Value):
            raise
        return float(Value)
    except:
        return float(DefaultValue)

def setStringValue(Value,DefaultValue):
    try:
        if len(Value) == 0:
            raise
        return Value
    except:
        return DefaultValue