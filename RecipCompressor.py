from Model.Range import *
from Model import Throw, Frame, Limits, OperatingConditions, Cylinder, Stage, LoadStep
import ThermodynamicsStl
import Logger
import math 

class RecipCompressor:

    # Equation 2-40
    def get_variable_auxiliary_load(self):
        return self.Frame.Friction * (self.OperatingConditions.OperatingSpeed.ValueAsDouble / self._RatedSpeed)
    def set_variable_auxiliary_load(self, value):
        pass


    def __init__(self):
        self.Limits = Limits.Limits()
        self.OperatingConditions = OperatingConditions.OperatingConditions()
        self.Frame = Frame.Frame()
         
        self.Stages = []
        self.LoadSteps = []
        self.Thermodynamics = ThermodynamicsStl.ThermodynamicsStl()
        self.RatedPower = 0
        self._RatedSpeed = 0
        self._PressureRatioFactor = 0
        self._IsentropicHorsePower = 0
        self._IsLoadStepSafe = False
        self._IsWebCallForLoadStepTable = False
        self.IsModelBuilderCalculation = False
        self.SweptVolume = None
        self.BrakePower = None
        self.Torque = None
        self.DriversMaximumAllowedPowerAtCurrentSpeed = None
        self.DriverPercentOfRatedLoad = None
        self.InletFlow = None
        self.OutletFlow = None
        self.IsentropicEfficiency = None
        self.OverallCompressionRatio = None
        self.RunStatus = None
        self.FlowReferenceCurveForSuctionPressure = None
        self.PowerReferenceCurveForSuctionPressure = None
        self.FlowReferenceCurveForDischargePressure = None
        self.PowerReferenceCurveForDischargePressure = None
        self.TemperatureReferenceCurveForSuctionPressure = None
        self.IsFlowBalanceCalculationSuccessful = False

    
    def _LoadLoadStepInputData(self, DF):   # Load Input data from Model for each LoadStep 
        loadStepIndex = 1
        while loadStepIndex <= self.OperatingConditions.NoOfLoadSteps:   # Load input data from Model for LoadStep
            loadStep = LoadStep.LoadStep()
            loadStep.Load(DF, loadStepIndex, self.Frame.NumberOfCylinders)   # Add LoadStep input data of each LoadStep into LoadSteps list
            self.LoadSteps.append(loadStep)
            loadStepIndex += 1 
    
    def _LoadThrowInputData(self, DF):   # Load Input data from Model for each Throw configured in Frame section 
        throwNumber = 1
        while throwNumber <= self.Frame.NumberOfThrows:   # Load input data from Model for Throw 
            throwInput = Throw.Throw(throwNumber)
            throwInput.Load(DF)   # Add throw input data of each throw into Throws list
            self.Frame.Throws.append(throwInput)
            throwNumber += 1

    def LoadStageInputData(self, DF):
        
        cylinders = self._LoadCylinderInputData(DF)    # Load Input data from Model for each Stage configured in Stage(s) sections # Actual index/number in model file starts with "1" but it starts with index "0" in list
        
        stageIndex = 1  
        while stageIndex <= self.OperatingConditions.NoOfStages: # Get all Cylinders for current Stage    
            stageCylinders = list( filter ( lambda x: (x.Number == stageIndex), cylinders) ) 
            print('Stage=' + str(stageIndex) + '  Cylinders=' + str(stageCylinders)) 
            stage = Stage.Stage(stageIndex) # Load input data from Model for Stage 
            
            stage.Load( DF, self.Thermodynamics, stageCylinders, self.OperatingConditions.NoOfStages )  
            self.Stages.append(stage) # Add Stage input data of each Stage into Stages list 
            stageIndex += 1

    def _LoadCylinderInputData(self, DF):
        cylinders = []   # Actual index in model file starts with 1
        cylinderIdx = 1
        while cylinderIdx <= self.Frame.NumberOfCylinders:   # Load input data from Model for Cylinder
            cylinder = Cylinder.Cylinder()
            cylinder.Load(DF, cylinderIdx)   # Add Cylinder input data of each Cylinder into Cylinder list
            cylinders.append(cylinder)
            cylinderIdx += 1 
        return cylinders
    
    def FrameLoad(self, DF):
        self.Frame.Load(DF, self.OperatingConditions.OEM) 
        

    def Load(self, DF): 
        self.Limits.Load(DF)   # Load Limits STATIC data input settings from model file 
        
        self.OperatingConditions.Load(DF)   # Load Operating Conditions STATIC data input settings from model file 
        
        self.FrameLoad(DF)   # Load Frame data input settings from model file 
        
        self._LoadThrowInputData(DF)   # Load Throw data input settings from model file 
        
        self._LoadLoadStepInputData(DF)   # Load Loadstep data input settings from model file 
        
        self.LoadStageInputData(DF)   # Load Stage STATIC data input settings from model file

        # Load the Unit level Operating Conditions data input settings from model file
        #LoadUnitInputData(DF)





            
            
            

    # def Load(self, piDataWrapper, UOM):
    #     # Load/Read Stage PI input data from PI
    #     self._LoadAndConvertInputDataFromPi(piDataWrapper, UOM)

    #     # Apply Unit Conversion for Constant values from Input to Core
    #     self.ConvertValuesFromInputUnitToCoreUnit(UOM)

    #     # Set Cylinder configuration from Load Step configuration
    #     # These values can only be set after reading Load Step information from Pi
    #     # This is initial Load and is primarily for Web calls.
    #     self._SetCylinderValuesFromLoadStep()







