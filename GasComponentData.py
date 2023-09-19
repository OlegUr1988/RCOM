class GasComponentData:
    def __init__(self, keyName, label, mdfCode, normalCode, value):
        self.KeyName = keyName 
        self.Label = label 
        self.MfdCode = mdfCode  #comment
        self.NormalCode = normalCode  #info
        self.UnitOfMeasureLabel = "mol%"
        self.Value = value