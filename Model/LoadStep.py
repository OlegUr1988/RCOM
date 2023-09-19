import math 
from Model import LoadStepCylinder
import Logger 
from Enums import OEM
import DefaultMapper as DM
 
class LoadStep: 
    def __init__(self): 
        self.logger = Logger.logger
        self.Number = 0
        self.LoadStepCylinders = []   # list of LoadStepCylinder() class related objects
        self.Power = None   # ModelComponent
        self.Flow = None   # ModelComponent
        self.IsSafe = None   # ModelComponent  
            
        
    def Load(self, DF, loadStepIndex, NoOfCylinders): 
        try:
            self.Number = DM.setFloatValue(DF['LoadStep_{loadstep}_No'.format(loadstep = loadStepIndex)][0], 0)   
            for cylinderIndex in range(1, NoOfCylinders + 1):
                loadStepCylinder = LoadStepCylinder.LoadStepCylinder() 
                loadStepCylinder.Load(DF, loadStepIndex, cylinderIndex)     # Load input values of each LoadStep Cylinder 
                self.LoadStepCylinders.append(loadStepCylinder)     # Add to LoadStep Cylinder list  
            
                self.logger.info("INFO_LoadStep_ Load done, loadStepIndex:" + str(loadStepIndex) + ", cylinderIndex:" +str(cylinderIndex))  
        except:
            self.logger.error("ERROR_LoadStep_ Load")  
        
        
        # self.Power = DM.setFloatValue(DF['OS_BrakePower'][0], 0) 
        
        # self.Power = 
        # ModelComponent(ModelComponentType.INPUT, RecipModelOutputKeys.RecipBrakePower, PowerLabel.Hp, "Unit/Recip Brake Power")
        
        # self.Flow = 
        # ModelComponent(ModelComponentType.INPUT, RecipModelOutputKeys.RecipInletFlow, FlowLabel.Mmscfd, "Unit/Recip Inlet Flow")
        
        # self.IsSafe = 
        # ModelComponent(ModelComponentType.INPUT, string.Empty, string.Empty, "Is Load Step Safe?")        
        
            
        
    # def Load(self, piDataWrapper, uom):     #/ Loads PI Tag input values for Operating Conditions of Recip from PI 
    #     for loadStepCylinder in self.LoadStepCylinders:     # Load input values of each Cylinder for the current LoadStep  
    #         loadStepCylinder.Load(piDataWrapper, uom)       # Load input values of each LoadStep Cylinder
 
    # def LoadPiDataForPerformanceTables(self, DF, piDataWrapper, uom):       #/ Loads the data from PI for Performance Tables on the Web.
    #     self._InitialiseOutputItems(uom) 
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, self.Power, None)        # Power 
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, self.Flow, 1)    # Inlet Flow = Flow at first Stage. Hence Index 1 is used.
 
    # def GetLoadStepCylinder(self, cylinderName):       # / Get the Load Step configuration that matches the Cylinder name
    #     loadStepCylinder = self.LoadStepCylinders.FirstOrDefault(lambda x : x.CylinderName == cylinderName) 
    #     Rcoms2Engine.Models.LoadStep._nlogger.Log(LogLevel.Debug, "cylinderName = '{0:s}', Is Cylinder Found? = '{1:s}'".format(cylinderName, loadStepCylinder is not None)) 
    #     return loadStepCylinder
 
    # def SetLoadStepFlow(self, flow):        #/ Set the Flow value of the Load Step
    #     self.Flow.ValueAsDouble = flow.ValueAsDouble
    #     self.Flow.UnitOfMeasure = flow.UnitOfMeasure 
    #     Rcoms2Engine.Models.LoadStep._nlogger.Log(LogLevel.Debug, "Flow = '{0:s}'".format(self.Flow.ValueAsDouble))
 
    # def SetLoadStepPower(self, power):      #/ Set the Power value of the Load Step
    #     self.Power.ValueAsDouble = power.ValueAsDouble
    #     self.Power.UnitOfMeasure = power.UnitOfMeasure 
    #     Rcoms2Engine.Models.LoadStep._nlogger.Log(LogLevel.Debug, "Power = '{0:s}'".format(self.Power.ValueAsDouble))

    # def SetIsLoadStepSafe(self, isSafe):
    #     self.IsSafe.ValueAsString = str(isSafe) 
    #     Rcoms2Engine.Models.LoadStep._nlogger.Log(LogLevel.Debug, "IsSafe = '{0:s}'".format(self.IsSafe))
  
 

 