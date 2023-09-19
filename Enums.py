from enum import Enum

class ModelComponentType(Enum):
    Input = 0
    Output = 1

class OEM(Enum):
    Ariel = 1
    CooperBessemer = 2
    Worthington = 3
    Clark = 4
    Ajax = 5
    Superior = 6
    DresserRand = 7    #    Dresser-Rand = 7
    Gemini = 8
    NeumanEsser = 9    #   Neuman&Esser = 9
    Others = 10

class RodLoadCalculationMethod(Enum):
    NA = 0                  # N/A
    PinLoadapproach = 1     #     Pin Load approach 
    GasRodLoadapproach = 2  #  Gas Rod Load approach    
    NetRodLoadapproach = 3  #     Net Rod Load approach 
    Auto = 4

class FlowMeterLocation(Enum):
    BeforeCompressor = 1    #1. Before Compressor
    AfterCompressor = 2     #2. After Compressor

class GasCalcType(Enum):
    SMIRK = 7
    CPA_SMIRK = 9   # CPA SMIRK
    CPA_SMIRK_LKP =  10     # CPA SMIRK LKP
    
class ErrorCodeClass(Enum):
    CCEError = -1
    NoError = 0
    PiTagError = 1 << 0
    IoKeynameError = 1 << 1
    IoFileError = 1 << 4
    CalculationError = 1 << 5
    Level1StateIsStop = 1 << 8
    
    
    
class CylinderEndType(Enum):
    HeadEnd = 0
    CrankEnd = 1
            
class CylinderMode(Enum): 
    NA = 0  # Not Applicable 
    DA = 1  # Double/Dual Acting 
    SAHE = 2    #Single Acting Head End 
    SACE = 3    # Single Acting - Crank End 
    Unloaded = 4    # Unloaded
        
class ValveType(Enum):
    Suction = 0
    Discharge = 1 
    
class FlowMeterType(Enum): 
    
    NoOption = -3,  #this is a change since none is a keyword in python
    Disabled = -2, 
    Previous = -1, 
    FlowPiTagAtStandardConditions = 0, 
    Orifice = 1, 
    Venturi = 2, 
    Valve = 3, 
    
    VesselsLiquidFlowPiTag = 4, 
    FlowPiTagActualFlow = 5, 
    RestrictionOrifice = 6, 
    PIDflow = 7, 
    Sidestream = 8

class FlowStatus(Enum): 
    
    Known = 0,   
    Unknown = 1,  

class FlowMeterLocationType(Enum):
    Suction = "SUCTION"
    Discharge = "DISCHARGE"

class EOSModelType(Enum):
    NoModel	= -1
    NoCalculation = 0
    AGA8 = 1
    RedlichKwongCritical = 2
    RedlichKwongExpanded = 3
    DranchukPurvisRobinson = 4
    SoaveRedlichKwong = 5
    PengRobinson = 6
    SMIRK = 7
    CPA = 8
    CPA_SMIRK = 9
    CPA_SMIRK_LKP = 10
    CPA_LKP = 11
    PR78 = 12
    PSRK_NRTL = 13
    PSRK_UNIFAC = 14
    STEAM = 15
    STL_HydrateFormationCalculations = 16 #ask if to be removed
    
class PhaseState(Enum):
    Unknown = -1
    Vapour = 0
    Liquid = 1
    Solid = 2
    
class Models(Enum):
    SMIRK = "Smirk"
    CPA = "CPA"
    CPA_SMIRK = "CPA/SMIRK"
    CPA_SMIRK_LKP = "CPA/SMIRK/LKP"
    CPA_LKP = "CPA/LKP"
    PR78 = "PR78"
    PSRK_NRTL = "PSRK"
    PSRK_UNIFAC = "PSRK-UNIFAC"
    STEAM = "Steam"
    
class Phases(Enum):
    VLL = "VLL"
    VLLL = "VLLL"
    Hydrates = "hydrates" 

class SideStreamType(Enum): 
    NotSet = 0  #/ The type has not been set.  
    Extraction = 1  #/ The side stream is an extraction type.  
    Admission = 2   #/ The side stream is an admission type.  
    Both = 3    #/ The side stream is both an extraction and admission type. 
    
    Default = 8   # it is not clear/ check it
    NoPresent = -2   # it is not clear/ check it
 

class SideStreamControllerType(Enum): 
    NotSet = 0  #/ The type has not been set. 
    Pressure = 1 #/ The controller uses pressure readings. 
    Flow = 2    #/ The controller uses flow readings.

class PhysicalQuantity(Enum): 
    NotSet = 1
    Density = 2
    DifferentialPressure = 3 
    DynamicViscosity = 4
    Force = 4
    Head = 5
    InletFlow = 6 
    StandardFlow = 7 
    Length = 8
    Mass = 9
    MassFlow = 10
    Momentum = 11
    PolytropicHead = 12 
    Power = 13
    Pressure = 14 
    Speed = 15
    SurfaceTension = 16 
    Temperature = 17
    VolumeFlow = 18
    Area = 19
    Volume = 20

# print(GasRecipStage_GasCalcType(9))
# print(Phases.Hydrates.value)
# print(Models("Smirk"))
# print(type(Models("Smirk")))
# print(Models.CPA_SMIRK.name)
#print(type(OEM(2)))
#print(type(FlowMeterLocationType.Suction))


    
'''   CCOM structure
class EOSModelType(Enum):
    NoModel	= -1
    NoCalculation = 0
    AGA8 = 1
    RedlichKwongCritical = 2
    RedlichKwongExpanded = 3
    DranchukPurvisRobinson = 4
    SoaveRedlichKwong = 5
    PengRobinson = 6
    SMIRK = 7
    CPA = 8
    CPA_SMIRK = 9
    CPA_SMIRK_LKP = 10
    CPA_LKP = 11
    PR78 = 12
    PSRK_NRTL = 13
    PSRK_UNIFAC = 14
    STEAM = 15
    STL_HydrateFormationCalculations = 16 #ask if to be removed
    
class CompressorMapCategory(Enum):
    SingleCurve = 1
    MultiSpeedCurve = 2
    IgvCurve = 3
    
class CurveName(Enum):
    InletFlowAndPolytropicHead = 1
    InletFlowAndPolytropicEfficiency = 2
    InletFlowAndPressureRatio = 3   
    InletFlowAndShaftPower = 4
        
class CurveType(Enum):
    PolytropicHeadAndEfficiencyCurve = 1
    PressureRatioAndShaftPowerCurve = 2
    
class FlowMeterType(Enum):
    NoOption = -3          #this is a change since none is a keyword in python
    Disabled = -2
    Previous = -1
    FlowPiTagAtStandardConditions = 0
    Orifice = 1
    Venturi = 2
    
class FluidType(Enum):
    ProcessGas = 7
    ProcessGasSideStream = 9
    
class VenturiType(Enum):
    AsCast = 0
    Machined = 1
    Rough = 2
    Other = 3
    
class FlowMeterLocationType(Enum):
    Suction = "SUCTION"
    Discharge = "DISCHARGE"
    
class PhysicalQuantity(Enum): 
    NotSet = 1
    Density = 2
    DifferentialPressure = 3 
    DynamicViscosity = 4
    Force = 4
    Head = 5
    InletFlow = 6 
    StandardFlow = 7 
    Length = 8
    Mass = 9
    MassFlow = 10
    Momentum = 11
    PolytropicHead = 12 
    Power = 13
    Pressure = 14 
    Speed = 15
    SurfaceTension = 16 
    Temperature = 17
    VolumeFlow = 18
    Area = 19
    Volume = 20

class ErrorCodeClass(Enum):
    CCEError = -1
    NoError = 0
    PiTagError = 1 << 0
    IoKeynameError = 1 << 1
    IoFileError = 1 << 4
    CalculationError = 1 << 5
    Level1StateIsStop = 1 << 8

class PhaseState(Enum):
    Unknown = -1
    Vapour = 0
    Liquid = 1
    Solid = 2
        
class Models(Enum):
    SMIRK = "Smirk"
    CPA = "CPA"
    CPA_SMIRK = "CPA/SMIRK"
    CPA_SMIRK_LKP = "CPA/SMIRK/LKP"
    CPA_LKP = "CPA/LKP"
    PR78 = "PR78"
    PSRK_NRTL = "PSRK"
    PSRK_UNIFAC = "PSRK-UNIFAC"
    STEAM = "Steam"
        
class Phases(Enum):
    VLL = "VLL"
    VLLL = "VLLL"
    Hydrates = "hydrates"

class EOSModelType(Enum):
    NoModel	= -1
    NoCalculation = 0
    AGA8 = 1
    RedlichKwongCritical = 2
    RedlichKwongExpanded = 3
    DranchukPurvisRobinson = 4
    SoaveRedlichKwong = 5
    PengRobinson = 6
    SMIRK = 7
    CPA = 8
    CPA_SMIRK = 9
    CPA_SMIRK_LKP = 10
    CPA_LKP = 11
    PR78 = 12
    PSRK_NRTL = 13
    PSRK_UNIFAC = 14
    STEAM = 15
    STL_HydrateFormationCalculations = 16 #ask if to be removed

class OEM(Enum):
    NoOEM = 0
    NuvoPignone = 1
    Siemens = 2
    GE = 3
    Elliot = 4
    ManesmannDeMag = 5
    BakerHughes = 6
    Mitsibushi = 7
    DresserRand = 8
    IngersollRand = 9
    KOBELCO = 10
    Others = 11
    InValid = 12 #check
''' 
