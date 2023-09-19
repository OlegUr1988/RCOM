import Logger
import math 
from Enums import OEM
import DefaultMapper as DM
        
class Frame: 
    def __init__(self):
        self.logger = Logger.logger
        
        self.Stroke = 0
        self.Friction = 0
        self.AuxillaryLoad = 0
        self.LengthOfConnectingRod = 0
        self.NumberOfThrows = 0
        self.Throws = None
        self.NumberOfCylinders = 0
        self.MechanicalEfficiency = 0
        self.PistonSpeed = 0
        self.Throws = []  

    def Load(self, DF, oem):
        try: 
            self.Stroke = DF["FM_Stroke"][0]
            
            if math.isnan(DF["FM_Friction"][0]): self.Friction = 0
            else: self.Friction = self.Friction = DF["FM_Friction"][0]
            
            if math.isnan(DF["FM_AuxillaryLoad"][0]): self.AuxillaryLoad = 0
            else: self.AuxillaryLoad = DF["FM_AuxillaryLoad"][0]
            
            self.NumberOfThrows = DF["FM_NumberOfThrows"][0]
            self.NumberOfCylinders = DF["FM_NumberOfCylinders"][0]  
            
            defaultME = 0.9 if oem == OEM.Ajax else 0.95 
            self.MechanicalEfficiency = DM.setFloatValue(DF['FM_MechanicalEfficiency'][0], defaultME)
    
            lenOfConRodDefault = self.Stroke * 2.5
            self.LengthOfConnectingRod = DM.setFloatValue(DF['FM_LengthOfConnectingRod'][0], lenOfConRodDefault)  
            
            self.logger.info("INFO_Frame_ Load is done" ) 
        except:
            self.logger.error("ERROR_Frame_ Load")  
            
             