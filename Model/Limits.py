import sys
sys.path.append('..') 
import Logger 
from Model.Range import Range  
        
class Limits:  
    def __init__(self):
        self.logger = Logger.logger 
        
        #self.logger.basicConfig(level=Logger.ERROR)
        self.OperatingSpeedLimit = None
        self.SpeedLimitByDesign = None
        self.DriverTorqueLimit = None
        self.SuctionVolumetricEfficiency = None
        self.FirstStageSuctionPressure = None
        self.LastStageDischargePressure = None
        self.SuctionTemperatureAtTransmitter = None 
 
    def Load(self, DF):
        try: 
            self.SpeedLimitByDesign = Range(DF['Limit_SD_Min'][0] ,DF['Limit_SD_Max'][0])
            self.OperatingSpeedLimit = Range(DF['Limit_OS_Min'][0] ,DF['Limit_OS_Max'][0])
            self.DriverTorqueLimit = Range(DF['Limit_DT_Min'][0] ,DF['Limit_DT_Max'][0])
            self.SuctionVolumetricEfficiency = Range(DF['Limit_SV_E_Min'][0] ,DF['Limit_SV_E_Max'][0])
            self.FirstStageSuctionPressure = Range(DF['Limit_FS_SP_Min'][0] ,DF['Limit_FS_SP_Max'][0])
            self.LastStageDischargePressure = Range(DF['Limit_LS_DP_Min'][0] ,DF['Limit_LS_DP_Max'][0]) 
            #Rcoms2Engine.Models.Limits._nlogger.Log(LogLevel.Debug, "OperatingSpeedLimit.Min = '{0:s}', OperatingSpeedLimit.Max = '{1:s}', SpeedLimitByDesign.Min = '{2:s}', , SpeedLimitByDesign.Max = '{3:s}'," + " DriverTorqueLimit.Min = '{4:s}', DriverTorqueLimit.Max = '{5:s}', SuctionVolumetricEfficiency.Min = '{6:s}', SuctionVolumetricEfficiency.Max = '{7:s}', FirstStageSuctionPressure.Min = '{8:s}', FirstStageSuctionPressure.Max = '{9:s}', " + "LastStageDischargePressure.Min = '{10:s}', LastStageDischargePressure.Max = '{11:s}', SuctionVolumetricEfficiency.Min = '{12:s}, SuctionVolumetricEfficiency.Max = '{13:s}'".format(self.OperatingSpeedLimit.Min, self.OperatingSpeedLimit.Max, self.SpeedLimitByDesign.Min, self.SpeedLimitByDesign.Max, self.DriverTorqueLimit.Min, self.DriverTorqueLimit.Max, self.SuctionVolumetricEfficiency.Min, self.SuctionVolumetricEfficiency.Max, self.FirstStageSuctionPressure.Min, self.FirstStageSuctionPressure.Max, self.LastStageDischargePressure.Min, self.LastStageDischargePressure.Max, self.SuctionVolumetricEfficiency.Min, self.SuctionVolumetricEfficiency.Max))
            
            self.logger.info("INFO_Limit_ Load is done" ) 
        except:
            self.logger.error("ERROR_Limit_ Load") 
                    
