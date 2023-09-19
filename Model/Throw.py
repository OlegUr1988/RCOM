import Logger
import math  
import DefaultMapper as DM
        
class Throw:   
    def __init__(self, throwNumber): 
        self.logger = Logger.logger
        
        self.ThrowNumber = throwNumber
        self.IsCylinderOmitted = False
        self.RodLoadLimitForCompression = 0
        self.RodLoadLimitForTension = 0
        self.PistonWeight = 0
        self.RodWeight = 0
        self.NutWeight = 0
        self.CrossHeadWeight = 0
        self.CrossHeadPinWeight = 0
        self.CrossHeadBalanceWeight = 0 
        
    def Load(self, DF):  
        try:
            self.IsCylinderOmitted = DM.setBoolValue(DF['Throw_{throwno}_IsCylinderOmitted'.format(throwno = self.ThrowNumber)][0], "False")
            self.RodLoadLimitForCompression = DM.setFloatValue(DF['Throw_{throwno}_RodLoadLimitForCompression'.format(throwno = self.ThrowNumber)][0], math.nan) 
            self.RodLoadLimitForTension = DM.setFloatValue(DF['Throw_{throwno}_RodLoadLimitForTension'.format(throwno = self.ThrowNumber)][0], math.nan)  
            self.PistonWeight = DM.setFloatValue(DF['Throw_{throwno}_PistonWeight'.format(throwno = self.ThrowNumber)][0], 0)  
            self.RodWeight = DM.setFloatValue(DF['Throw_{throwno}_RodWeight'.format(throwno = self.ThrowNumber)][0], 0) 
            self.NutWeight = DM.setFloatValue(DF['Throw_{throwno}_NutWeight'.format(throwno = self.ThrowNumber)][0], 0) 
            self.CrossHeadWeight = DM.setFloatValue(DF['Throw_{throwno}_CrossHeadWeight'.format(throwno = self.ThrowNumber)][0], 0) 
            self.CrossHeadPinWeight = DM.setFloatValue(DF['Throw_{throwno}_CrossHeadPinWeight'.format(throwno = self.ThrowNumber)][0], 0)
            self.CrossHeadBalanceWeight = DM.setFloatValue(DF['Throw_{throwno}_CrossHeadBalanceWeight'.format(throwno = self.ThrowNumber)][0], 0)
    
            self.logger.info("INFO_Throw_ Throw Number:" + str(self.ThrowNumber) + " Data Load Completed" )  
        except:
            self.logger.error("ERROR_Throw_ Load")  



    # def ConvertValuesFromInputUnitToCoreUnit(self, uom):
    #     Rcoms2Engine.Models.Throw._nlogger.Log(LogLevel.Debug, "Before converting Input to Core Unit - Input Units: RodLoadLimitForCompression = '{0:s}', RodLoadLimitForTension = '{1:s}', PistonWeight = '{2:s}'" + ", RodWeight = '{3:s}', CrossHeadWeight = '{4:s}', CrossHeadPinWeight = '{5:s}', CrossHeadBalanceWeight = '{6:s}'; " + "Input Values: RodLoadLimitForCompression = '{7:s}', RodLoadLimitForTension = '{8:s}', PistonWeight = '{9:s}', RodWeight = '{10:s}', NutWeight = '{11:s}', CrossHeadWeight = '{12:s}', " + "CrossHeadPinWeight = '{13:s}', CrossHeadBalanceWeight = '{14:s}'".format(uom.Force.Input.Label, uom.Force.Input.Label, uom.Mass.Input.Label, uom.Mass.Input.Label, uom.Mass.Input.Label, uom.Mass.Input.Label, uom.Mass.Input.Label, uom.Mass.Input.Label, self.RodLoadLimitForCompression, self.RodLoadLimitForTension, self.PistonWeight, self.RodWeight, self.NutWeight, self.CrossHeadWeight, self.CrossHeadPinWeight, self.CrossHeadBalanceWeight))


    #     self.RodLoadLimitForCompression = Rcoms2Helper.ConvertUnit(self.RodLoadLimitForCompression, uom.Force)
    #     self.RodLoadLimitForTension = Rcoms2Helper.ConvertUnit(self.RodLoadLimitForTension, uom.Force)

    #     self.PistonWeight = Rcoms2Helper.ConvertUnit(self.PistonWeight, uom.Mass)
    #     self.RodWeight = Rcoms2Helper.ConvertUnit(self.RodWeight, uom.Mass)
    #     self.NutWeight = Rcoms2Helper.ConvertUnit(self.NutWeight, uom.Mass)

    #     self.CrossHeadWeight = Rcoms2Helper.ConvertUnit(self.CrossHeadWeight, uom.Mass)
    #     self.CrossHeadPinWeight = Rcoms2Helper.ConvertUnit(self.CrossHeadPinWeight, uom.Mass)
    #     self.CrossHeadBalanceWeight = Rcoms2Helper.ConvertUnit(self.CrossHeadBalanceWeight, uom.Mass)

    #     Rcoms2Engine.Models.Throw._nlogger.Log(LogLevel.Debug, "After converting values to Core Unit - RodLoadLimitForCompression = '{0:s}', RodLoadLimitForTension = '{1:s}', PistonWeight = '{2:s}'" + ", RodWeight = '{3:s}', CrossHeadWeight = '{4:s}', CrossHeadPinWeight = '{5:s}', CrossHeadBalanceWeight = '{6:s}'; ".format(self.RodLoadLimitForCompression, self.RodLoadLimitForTension, self.PistonWeight, self.RodWeight, self.NutWeight, self.CrossHeadWeight, self.CrossHeadPinWeight, self.CrossHeadBalanceWeight))

    # def CheckIfAllCylinderWeightsAreAvailable(self):
    #     if (self.PistonWeight + self.RodWeight + self.NutWeight > 0.0) and (self.CrossHeadWeight + self.CrossHeadPinWeight + self.CrossHeadBalanceWeight > 0.0):
    #         return True

    #     return False
    