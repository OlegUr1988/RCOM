import Model.CylinderEnd as CylinderEnd 
import Logger
import math 
from Enums import OEM, CylinderMode, CylinderEndType
import DefaultMapper as DM 

        
class Cylinder:  
    def __init__(self): #/ Initialises a new instance of the Cylinder class. 
        self.logger = Logger.logger
    
        self.SerialNumber = None
        self.Number = 0
        self.Name = None
        self.ThrowNumber = 0
        self.StageNumber = 0
        self.MaximumAllowableWorkingPressure = 0
        self.MaximumAllowedDischargeTemperature = 0
        self.HeadEnd =  None
        self.CrankEnd = None
        self.BoreDiameter = 0
        self.CylinderMode = None
        self._GasK = 0
        self._GasN = 0
        self._Velocity = None
        self.InertiaForces = None
        self.GasForces = None
        self.TotalForces = None
        self.InertiaForcesForRodLoad = None
        self.GasForcesForRodLoad = None
        self.TotalForcesForRodLoad = None
        self.DegreesOfPinReversalAndOpposingForcePass = False
        self.AllCylinderWeightsAvailable = False
        self.IsActualTemperatureAvailable = False
        
        self.PreHeatSuctionTemperature = float() 
        self.DischargeTemperatureCalculated =  float() 
        self.EstimatedActualDischargeTemperature = float()    
        self.TensionInertia = float()
        self.TensionInertiaPercentage = float()
        self.CompressionInertia = float()
        self.CompressionInertiaPercentage = float()
        self.DegreesOfPinReversal = float()
        self.OpposingForce = float()
        self.TotalPower = float()
        self.IsentropicEfficiency = float()
        self.DischargeTemperatureAtFlange = float()
        self.DischargeTemperatureCalculatedDelta = float()
        self.Zs = float()
        self.Zd = float()
        
        self.Velocity = []
        self.InertiaForces = []
        self.GasForces = []
        self.TotalForces = []
        self.InertiaForcesForRodLoad = []
        self.GasForcesForRodLoad = []
        self.TotalForcesForRodLoad = []  
        

    def Load(self, DF, cylinderIndex:int):   #/ Loads the Input values for the current Cylinder from DF
        try:
            self.BoreDiameter = DM.setFloatValue(DF['Cylinder_{cylinderno}_BoreDiameter'.format(cylinderno = cylinderIndex)][0], 0) 
            
            # SerialNumber is not used in calc
            self.SerialNumber = DM.setStringValue(DF['Cylinder_{cylinderno}_SN'.format(cylinderno = cylinderIndex)][0], 0)   # DF.Read(RecipModelInputKeys.CylinderSerialNumber, string.Empty, cylinderIndex, ParsingType.STRING)
            self.Name = DM.setStringValue(DF['Cylinder_{cylinderno}_Name'.format(cylinderno = cylinderIndex)][0], 0)  # DF.Read(RecipModelInputKeys.CylinderName, string.Empty, cylinderIndex, ParsingType.STRING)
            self.ThrowNumber = DM.setIntValue(DF['Cylinder_{cylinderno}_ThrowNumber'.format(cylinderno = cylinderIndex)][0], 0)  # DF.Read(RecipModelInputKeys.CylinderThrowNumber, string.Empty, cylinderIndex, ParsingType.INTEGER)
            self.StageNumber = DM.setIntValue(DF['Cylinder_{cylinderno}_StageNumber'.format(cylinderno = cylinderIndex)][0], 0)  # DF.Read(RecipModelInputKeys.CylinderStageNumber, string.Empty, cylinderIndex, ParsingType.INTEGER)
            self.MaximumAllowableWorkingPressure = DM.setFloatValue(DF['Cylinder_{cylinderno}_MaximumAllowableWorkingPressure'.format(cylinderno = cylinderIndex)][0], 0)  # DF.Read(RecipModelInputKeys.CylinderMaximumAllowableWorkingPressure, "0.0", cylinderIndex, ParsingType.DOUBLE)
            self.MaximumAllowedDischargeTemperature = DM.setFloatValue(DF['Cylinder_{cylinderno}_MaximumAllowedDischargeTemperature'.format(cylinderno = cylinderIndex)][0], 0)  # DF.Read(RecipModelInputKeys.CylinderMaximumAllowedDischargeTemperature, "0.0", cylinderIndex, ParsingType.DOUBLE)
    
            self.DischargeTemperatureAtFlange = DM.setStringValue(DF['Cylinder_{cylinderno}_DischargeTemperatureAtFlange'.format(cylinderno = cylinderIndex)][0], 0) # DF.Read(self.DischargeTemperatureAtFlange.KeyName, string.Empty, cylinderIndex, ParsingType.STRING)
    
            # Check and set if the Actual Discharge Temperature At Flange is available/configured (NOT empty) in the model file.
            if self.DischargeTemperatureAtFlange is not math.nan and  self.DischargeTemperatureAtFlange!= 0:
                self.IsActualTemperatureAvailable = self.DischargeTemperatureAtFlange
            self.IsActualTemperatureAvailable = self.DischargeTemperatureAtFlange
    
            # Stores the Cylinder Number/Index across all Stages
            self.Number = cylinderIndex
    
            # Load input data from Model for Cylinder Head End  
            headEnd = CylinderEnd.CylinderEnd(CylinderEndType.HeadEnd) 
            headEnd.Load( DF, cylinderIndex, None ) 
            self.HeadEnd = headEnd 
    
            # Load input data from Model for Cylinder Crank End 
            crankEnd = CylinderEnd.CylinderEnd(CylinderEndType.CrankEnd) 
            crankEnd.Load( DF, cylinderIndex, self.HeadEnd ) 
            self.CrankEnd = crankEnd
             
        
            self.logger.info("INFO_Cylinder_Load done,  Cylinder #" + str(cylinderIndex))  
        except:
            self.logger.error("ERROR_Cylinder_Load")


    def ResetCalculatedValues(self):    #/ Reset all calculated values for Cylinder.
        self._GasK = 0.0
        self._GasN = 0.0
        self._Velocity = []
        self.InertiaForces = []
        self.GasForces = []
        self.TotalForces = []
        self.InertiaForcesForRodLoad = []
        self.GasForcesForRodLoad = []
        self.TotalForcesForRodLoad = []
        self.DegreesOfPinReversalAndOpposingForcePass = False

        self.PreHeatSuctionTemperature.ValueAsDouble = 0.0
        self.DischargeTemperatureCalculated.ValueAsDouble = 0.0
        self.EstimatedActualDischargeTemperature.ValueAsDouble = 0.0
        self.TensionInertia.ValueAsDouble = 0.0
        self.TensionInertiaPercentage.ValueAsDouble = 0.0
        self.CompressionInertia.ValueAsDouble = 0.0
        self.CompressionInertiaPercentage.ValueAsDouble = 0.0
        self.DegreesOfPinReversal.ValueAsDouble = 0.0
        self.OpposingForce.ValueAsDouble = 0.0
        self.TotalPower.ValueAsDouble = 0.0
        self.IsentropicEfficiency.ValueAsDouble = 0.0
        self.DischargeTemperatureCalculatedDelta.ValueAsDouble = 0.0
        self.Zs.ValueAsDouble = 0.0
        self.Zd.ValueAsDouble = 0.0

        # Reset Calculated Values for each Cylinder End
        self.HeadEnd.ResetCalculatedValues()
        self.CrankEnd.ResetCalculatedValues()





#/ Initialise all Model Component objects for Input. 
# def _InitialiseInputItems(self):
#     PreHeatSuctionTemperature = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Cylinder Pre-Heat Suction Temperature") 
#     DischargeTemperatureCalculated =  float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Cylinder Calculated Discharge Temperature") 
#     EstimatedActualDischargeTemperature = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Cylinder Estimated Actual Discharge Temperature") 
#     TensionInertia = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, ForceLabel.Lbf, "Cylinder/Throw Tension Inertia") 
#     TensionInertiaPercentage = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, GeneralLabel.Percentage, "Cylinder/Throw Tension Inertia Percentage") 
#     CompressionInertia = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, ForceLabel.Lbf, "Cylinder/Throw Compression Inertia") 
#     CompressionInertiaPercentage = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, GeneralLabel.Percentage, "Cylinder/Throw Compression Inertia Percentage") 
#     DegreesOfPinReversal = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Cylinder/Throw Degrees of Reversal") 
#     OpposingForce = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, ForceLabel.Lbf, "Cylinder/Throw Opposing Force") 
#     TotalPower = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, PowerLabel.Hp, "Cylinder Total Power") 
#     IsentropicEfficiency = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Cylinder Isentropic Efficiency") 
#     DischargeTemperatureAtFlange = float()
#     # ModelComponent(ModelComponentType.Input, RecipModelInputKeys.CylinderDischargeTemperatureAtFlange, TemperatureLabel.R, "Discharge Temperature At Flange") 
#     DischargeTemperatureCalculatedDelta = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, TemperatureLabel.R, "Discharge Temperature Calculated Delta") 
#     Zs = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Compressibility at Suction") 
#     Zd = float()
#     # ModelComponent(ModelComponentType.Input, string.Empty, string.Empty, "Compressibility at Discharge")


 
    

          # [('Cylinder [{cylinderno}]||Serial Number','float','Cylinder_{cylinderno}_SN'),
          # ('Cylinder [{cylinderno}]||Name','str','Cylinder_{cylinderno}_Name'),
          # ('Cylinder [{cylinderno}]||Throw Number','int','Cylinder_{cylinderno}_ThrowNumber'),
          # ('Cylinder [{cylinderno}]||Stage Number','int','Cylinder_{cylinderno}_StageNumber'),
          # ('Cylinder [{cylinderno}]||Maximum Allowable Working Pressure','float','Cylinder_{cylinderno}_MaximumAllowableWorkingPressure'),
          # ('Cylinder [{cylinderno}]||Maximum Allowed Discharge Temperature','float','Cylinder_{cylinderno}_MaximumAllowedDischargeTemperature'),
          # ('Cylinder [{cylinderno}]||Bore Diameter','float','Cylinder_{cylinderno}_BoreDiameter'),
          # ('Cylinder [{cylinderno}]||Discharge Temperature at Flange','float','Cylinder_{cylinderno}_DischargeTemperatureAtFlange'), 
           
     
    
    #/ Loads the Input values for the current Stage from PI and converts the units from Input to Core Units 
    #     # Read Tag value from PI
    #     piDataWrapper.ReadValue(DischargeTemperatureAtFlange)
    
    
    
    # #/ Loads the data from PI for Performance Tables on the Web. 
    # def LoadPiDataForPerformanceTables(self, DF, piDataWrapper, uom, cylinderNumber):
    #     nlogger.Log(LogLevel.Debug, "Loading Pi data for Cylinder sequence number (across all Stages): '{0:s}'.".format(cylinderNumber))
    
    #     # Initialize Output Items along with Output Units
    #     InitialiseOutputItems(uom)
    
    #     #For Pre-Heat Suction Temperature
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, PreHeatSuctionTemperature, Number)
    
    #     # For Estimated Actual Discharge Temperature
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, EstimatedActualDischargeTemperature, Number)
    
    #     # For Isentropic Efficiency
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, IsentropicEfficiency, Number)
    
    #     # For Discharge Temperature At Flange
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, DischargeTemperatureAtFlange, Number)
    
    #     # For Throw - Each Throw has one Cylinder
    #     # For Tension Inertia
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, TensionInertia, ThrowNumber)
    
    #     # For Tension Inertia Percentage
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, TensionInertiaPercentage, ThrowNumber)
    
    #     # For Compression Inertia
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, CompressionInertia, ThrowNumber)
    
    #     # For Compression Inertia Percentage
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, CompressionInertiaPercentage, ThrowNumber)
    
    #     # For Degrees Of Pin Reversal
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, DegreesOfPinReversal, ThrowNumber)
    
    #     # For Opposing Force
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, OpposingForce, ThrowNumber)
    
    #     # Discharge Temperature Calculated Delta
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, DischargeTemperatureCalculatedDelta, Number)
    
    #     # Get Pi data for Cylider Ends
    #     HeadEnd.LoadPiDataForPerformanceTables(DF, piDataWrapper, uom, cylinderNumber)
    #     CrankEnd.LoadPiDataForPerformanceTables(DF, piDataWrapper, uom, cylinderNumber)
    
        
    
    #/ Loads the data from PI for Cylinder Svg on the Web.
    # def LoadPiDataForCylinderSvg(self, DF, piDataWrapper, uom, cylinderNumber):
    #     nlogger.Log(LogLevel.Debug, "Loading Pi data for Cylinder sequence number (across all Stages): '{0:s}'.".format(cylinderNumber))
    
    #     # Initialize Output Items along with Output Units
    #     InitialiseOutputItems(uom)
    
    #     # For Estimated Actual Discharge Temperature
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, EstimatedActualDischargeTemperature, Number)
    
    #     # For Throw - Each Throw has one Cylinder
    #     # For Tension Inertia
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, TensionInertia, ThrowNumber)
    
    #     # For Compression Inertia
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, CompressionInertia, ThrowNumber)
    
    #     nlogger.Log(LogLevel.Debug, "Loaded data from Pi. Current Cylinder Number = '{0:s}', EstimatedActualDischargeTemperature = '{1:s}', TensionInertia = '{2:s}', CompressionInertia = '{3:s}'".format(Number, EstimatedActualDischargeTemperature.ValueAsDouble, TensionInertia.ValueAsDouble, CompressionInertia.ValueAsDouble))
    
    
    
    #/ Loads the Pi Tags/Expressions from DF for Performance Trends on the Web.
    # def LoadPiTagsForPerformanceTrends(self, DF, piDataWrapper, uom):
    #     # Initialize Output Items along with Output Units
    #     InitialiseOutputItems(uom)
    
    #     # Discharge Temperature Calculated Delta
    #     Rcoms2Helper.LoadPiTagExpressions(DF, piDataWrapper, DischargeTemperatureCalculatedDelta, Number)
    
    #     # Discharge Temperature At Flange
    #     Rcoms2Helper.LoadPiTagExpressions(DF, piDataWrapper, DischargeTemperatureAtFlange, Number)
    
    #     # Estimated Actual Discharge Temperature
    #     Rcoms2Helper.LoadPiTagExpressions(DF, piDataWrapper, EstimatedActualDischargeTemperature, Number)
    
    
    
    #/ Load Historic Data from PI for given Tags & timestamps
    # def LoadHistoricDataFromPi(self, DF, piDataWrapper, uom, timeStamps):
    #     # Initialize Output Items along with Output Units
    #     InitialiseOutputItems(uom)
    
    #     # Load Actual Discharge Temperature
    #     # TO DO - What DischargeTemperatureAtTransmitter for Cylinder?
    #     #Rcoms2Helper.LoadDataFromPi(DF, piInterfaceHelper, DischargeTemperatureAtTransmitter, Number)
    #     #piInterfaceHelper.GetPiExpressionValue(DischargeTemperatureAtTransmitter)
    #     #DischargePressureAtTransmitter.PiTag.DateTime = timeStamps
    
    #     # Load Estimated Actual Discharge Temperature
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, EstimatedActualDischargeTemperature, Number)
    #     EstimatedActualDischargeTemperature.PiTag.DateTime = timeStamps
    
    #     # Load Discharge Temperature Calculated Delta
    #     Rcoms2Helper.LoadDataFromPi(DF, piDataWrapper, DischargeTemperatureCalculatedDelta, Number)
    #     DischargeTemperatureCalculatedDelta.PiTag.DateTime = timeStamps
