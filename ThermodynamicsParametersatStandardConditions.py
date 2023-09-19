import MathematicalConstant
import DefaultMapper as DM

class ThermodynamicsParametersatStandardConditions:
    
    def __init__(self):
        
        self.PSTD_Defaultvalue = 101.325
        self.PSTD = 101.325        
        self.TSTD_DefaultValue = 288.15
        self.TSTD = 288.15

    #checked
    def Load(self, DF):
        self.TSTD =         DM.setStringValue(DF['GN_ATM_T'][0], 0)    
        self.PSTD =         DM.setStringValue(DF['GN_SP'][0], 0)    
        


 



    # #checked
    # def ConvertPressure(self, pressUIn, atmosphericPressure_KiloPascal):
    #     if self.PSTD < 50:
    #         self.PSTD = (self.PSTD * pressUIn) + atmosphericPressure_KiloPascal
        
            
    # #checked
    # def ConvertTemperature(self, tempAddUIn, tempUIn):
    #     if self.TSTD < 150:
    #         self.TSTD = (self.TSTD + tempAddUIn) * tempUIn
    #         self.TSTD = self.TSTD + MathematicalConstant.Kelvin