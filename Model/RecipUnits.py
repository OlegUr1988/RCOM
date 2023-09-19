from BaseEngine import *
from CCEDataContract import *
from Core.PI import *
from Core.UnitsOfMeasure import *
from Core.UnitsOfMeasure.Data import *
from Rcoms2Engine.Data import *

class Rcoms2Engine: #this class replaces the original namespace 'Rcoms2Engine'
    class Models: #this class replaces the original namespace 'Models'
        class RecipUnits:
        ##region Public Properties


        ##endregion

        ##region Construction
            def __init__(self):
                #instance fields found by C# to Python Converter:
                self.Pressure = None
                self.Flow = None
                self.Temperature = None
                self.Power = None
                self.Length = None
                self.Weight = None
                self.Force = None

                self._Initialise()
        ##endregion

        ##region Private Methods
            def _Initialise(self):
                self.Pressure = string.Empty
                self.Flow = string.Empty
                self.Temperature = string.Empty
                self.Power = string.Empty
                self.Length = string.Empty
                self.Weight = string.Empty
                self.Force = string.Empty

        ##endregion

        ##region Public Methods
            def Load(self, hashTable):
                self.Pressure = hashTable.Read(UnitInputKeyName.Pressure, PressureLabel.Psia, ParsingType.STRING)
                self.Flow = hashTable.Read(UnitInputKeyName.Flow, FlowLabel.Mmscfd, ParsingType.STRING)
                self.Temperature = hashTable.Read(UnitInputKeyName.Temperature, TemperatureLabel.R, ParsingType.STRING)
                self.Power = hashTable.Read(UnitInputKeyName.Power, PowerLabel.Hp, ParsingType.STRING)
                self.Length = hashTable.Read(UnitInputKeyName.Length, LengthLabel.In, ParsingType.STRING)
                self.Weight = hashTable.Read(UnitInputKeyName.Weight, MassLabel.Lb, ParsingType.STRING)
                self.Force = hashTable.Read(UnitInputKeyName.Force, ForceLabel.Lbf, ParsingType.STRING)

        ##endregion
