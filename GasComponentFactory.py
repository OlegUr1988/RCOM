import Logger
import GasComponentIndex

#PhysicalProperties not required for ccomsv2
class PhysicalProperties:
    def __init__(self, kg=0, m3=0, kmol=None):
        self.Kg = kg
        self.M3 = m3
        self.Kmol = kmol

class GasComponent:
    
    def __init__(self,Id = 0, Name = "", Desc = "", FullName = "", Mw = 0.0, Cp = 0.0, Tcr = 0.0, Pcr = 0.0, MoleFrac = 0.0, SRK_w = 0.0, SRK_CpA = 0.0, SRK_CpB = 0.0, SRK_CpC = 0.0, SRK_CpD = 0.0, SRK_m = 0.0, SRK_alpha = 0.0, SRK_a = 0.0, SRK_b = 0.0, PR_m = 0.0, PR_alpha = 0.0, PR_ac = 0.0, PR_a_i = 0.0, PR_b_i = 0.0, PR_b_x = 0.0, PR_a = 0.0, PR_b = 0.0, PR_c = 0.0, PR_d = 0.0, PR_e = 0.0, PR_f = 0.0, PR_w = 0.0, LHV = None, HHV = None, WobbeIndex = 0, CarbonContent = 0, HydrogenContent = 0, OxygenContent = 0, SulphurContent = 0, WaterContent = 0, Carbon = 0, Hydrogen = 0, Nitrogen = 0, Sulphur = 0, Oxygen = 0):
       
        self.Name = Name 
        self.Mw = Mw  
        self.MoleFrac = MoleFrac  

        #below not used in CCOMsv2
        self.Id = Id   
        self.Desc = Desc  
        self.FullName = FullName  
        self.Cp = Cp  
        self.Tcr = Tcr  
        self.Pcr = Pcr  
        self.SRK_w = SRK_w  
        self.SRK_CpA = SRK_CpA  
        self.SRK_CpB = SRK_CpB  
        self.SRK_CpC = SRK_CpC  
        self.SRK_CpD = SRK_CpD  
        self.SRK_m = SRK_m  
        self.SRK_alpha = SRK_alpha  
        self.SRK_a = SRK_a  
        self.SRK_b = SRK_b  
        self.PR_m = PR_m  
        self.PR_alpha = PR_alpha  
        self.PR_ac = PR_ac  
        self.PR_a_i = PR_a_i  
        self.PR_b_i = PR_b_i  
        self.PR_b_x = PR_b_x  
        self.PR_a = PR_a  
        self.PR_b = PR_b  
        self.PR_c = PR_c  
        self.PR_d = PR_d  
        self.PR_e = PR_e  
        self.PR_f = PR_f  
        self.PR_w = PR_w  
        self.LHV = LHV  
        self.HHV = HHV  
        self.WobbeIndex = WobbeIndex  
        self.CarbonContent = CarbonContent  
        self.HydrogenContent = HydrogenContent  
        self.OxygenContent = OxygenContent  
        self.SulphurContent = SulphurContent  
        self.WaterContent = WaterContent  
        self.Carbon = Carbon  
        self.Hydrogen = Hydrogen  
        self.Nitrogen = Nitrogen  
        self.Sulphur = Sulphur  
        self.Oxygen = Oxygen  

################################################################################################################


def CreateGasComponentsNormal(gasComponents=None):
    
    logger = Logger.logger
    
    if gasComponents is None:
        temporaryComponents = []
    else:
        temporaryComponents = gasComponents

    try:
        temporaryComponents.append(CreateC1())
        temporaryComponents.append(CreateC2())
        temporaryComponents.append(CreateC3())
        temporaryComponents.append(CreateIC4())
        temporaryComponents.append(CreateNC4())
        temporaryComponents.append(CreateIC5())
        temporaryComponents.append(CreateNC5())
        temporaryComponents.append(CreateC6())
        temporaryComponents.append(CreateC7())
        temporaryComponents.append(CreateC8())
        temporaryComponents.append(CreateC9())
        temporaryComponents.append(CreateC10())
        temporaryComponents.append(CreateCO2())
        temporaryComponents.append(CreateN2())
        temporaryComponents.append(CreateH2S())
        temporaryComponents.append(CreateHE())
        temporaryComponents.append(CreateH2O())
        temporaryComponents.append(CreateO2())
        temporaryComponents.append(CreateAR())
        temporaryComponents.append(CreateH2())
        temporaryComponents.append(CreateCO())
        
        if gasComponents is None:
            for component in temporaryComponents:
                component.HHV = PhysicalProperties(kmol = component.HHV.Kg * component.Mw)
                component.LHV = PhysicalProperties(kmol = component.LHV.Kg * component.Mw)

        return temporaryComponents
    
    except Exception as ex:
        logger.error(ex, exc_info=True)
        return []


def CreateGasComponentsExtended():
    logger = Logger.logger    
    try:
        # First create all the Normal gas components.
        components = CreateGasComponentsNormal()

        # Now add the extended collection of components.
        # Add other extended gas components here...
        components.append(CreateSO2())
        components.append(CreateNEO_PENTANE())
        components.append(CreateNEO_HEXANE())
        components.append(CreateISO_OCTANE())
        components.append(CreateETHENE())
        components.append(CreatePROPENE())
        components.append(CreateONE_BUTENE())
        components.append(CreateCIS_2_BUTENE())
        components.append(CreateTRANS_2_BUTENE())
        components.append(CreateISO_BUTENE())
        components.append(CreateONE_PENTENE())
        components.append(CreateACETYLENE())
        components.append(CreateBENZENE())
        components.append(CreateTOLUENE())
        components.append(CreateETHYL_BENZENE())
        components.append(CreateOXYLENE())
        components.append(CreateMXYLENE())
        components.append(CreatePXYLENE())
        components.append(CreateSTYRENE())
        components.append(CreateMETHYL_ALCOHOL())
        components.append(CreateETHYL_ALCOHOL())
        components.append(CreateAMMONIA())

        for component in components:
            component.HHV = PhysicalProperties(kmol = component.HHV.Kg * component.Mw)
            component.LHV = PhysicalProperties(kmol = component.LHV.Kg * component.Mw)

        return components
    
    except Exception as ex:
        logger.error(ex, exc_info=True)
        return []

#################################################################################################################


def CreateAMMONIA():
    Component = GasComponent(
        Id = GasComponentIndex.AMMONIA,
        FullName = "Ammonia",
        Mw = 17.031,
        Name = "Ammonia",
        Pcr = 11350,
        Tcr = 405.5,
        Carbon = 0,
        Hydrogen = 3,
        Nitrogen = 1,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 27.927948, m3 = 20.121),
        LHV = PhysicalProperties(kg = 24.013788, m3 = 17.301)
    )
    return Component


def CreateETHYL_ALCOHOL():

    Component = GasComponent(
        Id = GasComponentIndex.ETHYL_ALCOHOL,
        FullName = "Ethyl Alcohol",
        Mw = 46.069,
        Name = "Ethyl Alcohol",
        Pcr = 6148,
        Tcr = 513.88,
        Carbon = 2,
        Hydrogen = 6,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 1,
        HHV = PhysicalProperties(kg = 29.0979268, m3 = 56.699),
        LHV = PhysicalProperties(kg = 27.7446184, m3 = 54.062)
    )
    return Component

def CreateMETHYL_ALCOHOL():
    Component = GasComponent(
        Id = GasComponentIndex.METHYL_ALCOHOL,
        FullName = "Methyl Alcohol",
        Mw = 32.042,
        Name = "Methyl Alcohol",
        Pcr = 8097,
        Tcr = 512.6,
        Carbon = 1,
        Hydrogen = 4,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 1,
        HHV = PhysicalProperties(kg = 23.878444, m3 = 32.36),
        LHV = PhysicalProperties(kg = 21.1046779, m3 = 28.601)
    )
    return Component

def CreateSTYRENE():
    Component = GasComponent(        
        Id = GasComponentIndex.STYRENE,
        FullName = "Styrene",
        Mw = 104.152,
        Name = "Styrene",
        Pcr = 4050,
        Tcr = 646,
        Carbon = 8,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 42.631962, m3 = 187.806),
        LHV = PhysicalProperties(kg = 42.96883, m3 = 189.29)
    )
    return Component


def CreatePXYLENE():
    Component = GasComponent(
        Id = GasComponentIndex.PXYLENE,
        FullName = "Pxylene",
        Mw = 106.168,
        Name = "Pxylene",
        Pcr = 3511,
        Tcr = 616.19,
        Carbon = 8,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 43.3029015, m3 = 194.445),
        LHV = PhysicalProperties(kg = 41.210635, m3 = 185.05 )
        )
    return Component


def CreateMXYLENE():
    Component = GasComponent(
        Id = GasComponentIndex.MXYLENE,
        FullName = "M-xylene",
        Mw = 106.168,
        Name = "M-xylene",
        Pcr = 3734,
        Tcr = 617.01,
        Carbon = 8,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 43.2962205, m3 = 194.415),
        LHV = PhysicalProperties(kg = 41.203954, m3 = 185.02)
    )
    return Component

def CreateOXYLENE():
    Component = GasComponent(
        Id = GasComponentIndex.OXYLENE,
        FullName = "O-xylene",
        Mw = 106.168,
        Name = "O-xylene",
        Pcr = 3536,
        Tcr = 630.29,
        Carbon = 8,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 43.2962205, m3 = 194.415),
        LHV = PhysicalProperties(kg = 41.2199884, m3 = 185.092)
    )
    return Component

def CreateETHYL_BENZENE():
    Component = GasComponent(
        Id = GasComponentIndex.ETHYL_BENZENE,
        FullName = "Ethyl Benzene",
        Mw = 106.168,
        Name = "Ethyl Benzene",
        Pcr = 3606,
        Tcr = 617.16,
        Carbon = 8,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 43.415365, m3 = 194.95 ),
        LHV = PhysicalProperties(kg = 41.2199884, m3 = 185.092 )
    )
    return Component

def CreateTOLUENE():
    Component = GasComponent(
        Id = GasComponentIndex.TOLUENE,
        FullName = "Toluene",
        Mw = 92.141,
        Name = "Toluene",
        Pcr = 4106,
        Tcr = 591.76,
        Carbon = 7,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 42.86503, m3 = 167.05),
        LHV = PhysicalProperties(kg = 40.9364244, m3 = 159.534)
        )
    return Component

def CreateBENZENE():
    Component = GasComponent(
        Id = GasComponentIndex.BENZENE,
        FullName = "Benzene",
        Mw = 78.114,
        Name = "Benzene",
        Pcr = 4898,
        Tcr = 562.12,
        Carbon = 6,
        Hydrogen = 6,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 42.2847684, m3 = 139.692),
        LHV = PhysicalProperties(kg = 40.5784485, m3 = 134.055)
    )
    return Component

def CreateACETYLENE():
    Component = GasComponent(
        Id = GasComponentIndex.ACETYLENE,
        FullName = "Acetylene",
        Mw = 26.038,
        Name = "Acetylene",
        Pcr = 6139,
        Tcr = 308.31,
        Carbon = 2,
        Hydrogen = 2,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 49.9255218, m3 = 54.978),
        LHV = PhysicalProperties(kg = 48.2182938, m3 = 53.098)
    )
    return Component

def CreateONE_PENTENE():
    Component = GasComponent(
        Id = GasComponentIndex.ONE_PENTENE,
        FullName = "1-Pentene",
        Mw = 70.135,
        Name = "1-Pentene",
        Pcr = 3513,
        Tcr = 464.74,
        Carbon = 5,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.158106, m3 = 142.86),
        LHV = PhysicalProperties(kg = 44.9910515, m3 = 133.465)
    )
    return Component

def CreateISO_BUTENE():
    Component = GasComponent(
        Id = GasComponentIndex.ISO_BUTENE,
        FullName = "Iso-Butene",
        Mw = 56.108,
        Name = "Iso-Butene",
        Pcr = 4000,
        Tcr = 417.86,
        Carbon = 4,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.1537994, m3 = 114.271),
        LHV = PhysicalProperties(kg = 44.986557, m3 = 106.755)
    )
    return Component


def CreateTRANS_2_BUTENE():
    Component = GasComponent(
        Id = GasComponentIndex.TRANS_2_BUTENE,
        FullName = "trans-2-Butene",
        Mw = 56.108,
        Name = "trans-2-Butene",
        Pcr = 3964,
        Tcr = 428.59,
        Carbon = 4,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.2389222, m3 = 114.473 ),
        LHV = PhysicalProperties(kg = 45.0716798, m3 = 106.957 )
        )
    return Component

def CreateCIS_2_BUTENE():
    Component = GasComponent(
        Id = GasComponentIndex.CIS_2_BUTENE,
        FullName = "cis-2-Butene",
        Mw = 56.108,
        Name = "cis-2-Butene",
        Pcr = 4243,
        Tcr = 435.54,
        Carbon = 4,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.3375298, m3 = 114.707),
        LHV = PhysicalProperties(kg = 45.1702874, m3 = 107.191)
    )
    return Component



def CreateONE_BUTENE():
    Component = GasComponent(
        Id = GasComponentIndex.ONE_BUTENE,
        FullName = "1-Butene",
        Mw = 56.108,
        Name = "1-Butene",
        Pcr = 4043,
        Tcr = 419.92,
        Carbon = 4,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.4572074, m3 = 114.991),
        LHV = PhysicalProperties(kg = 45.289965, m3 = 107.475)
    )
    return Component

def CreatePROPENE():
    Component = GasComponent(
        Id = GasComponentIndex.PROPENE,
        FullName = "Propene",
        Mw = 42.081,
        Name = "Propene",
        Pcr = 4665,
        Tcr = 365.55,
        Carbon = 3,
        Hydrogen = 6,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.9521661, m3 = 87.119),
        LHV = PhysicalProperties(kg = 45.7847358, m3 = 81.482)
    )
    return Component

def CreateETHENE():
    Component = GasComponent(
        Id = GasComponentIndex.ETHENE,
        FullName = "Ethene",
        Mw = 28.054,
        Name = "Ethene",
        Pcr = 5040,
        Tcr = 282.34,
        Carbon = 2,
        Hydrogen = 4,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 50.31516, m3 = 59.7),
        LHV = PhysicalProperties(kg = 47.1479176, m3 = 55.942)
    )
    return Component

def CreateISO_OCTANE():
    Component = GasComponent(
        Id = GasComponentIndex.ISO_OCTANE,
        FullName = "Iso-Octane",
        Mw = 114.232,
        Name = "Iso-Octane",
        Pcr = 2570,
        Tcr = 543.86,
        Carbon = 8,
        Hydrogen = 18,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.157308, m3 = 232.644),
        LHV = PhysicalProperties(kg = 44.656524, m3 = 215.732)
    )
    return Component

def CreateNEO_HEXANE():
    Component = GasComponent(
        Id = GasComponentIndex.NEO_HEXANE,
        FullName = "Neo-Hexane",
        Mw = 86.178,
        Name = "Neo-Hexane",
        Pcr = 3080,
        Tcr = 488.66,
        Carbon = 6,
        Hydrogen = 14,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.7213664, m3 = 177.556),
        LHV = PhysicalProperties(kg = 44.9146152, m3 = 163.683)
    )
    return Component

def CreateNEO_PENTANE():
    Component = GasComponent(
        Id = GasComponentIndex.NEO_PENTANE,
        FullName = "Neo-Pentane",
        Mw = 72.151,
        Name = "Neo-Pentane",
        Pcr = 3199,
        Tcr = 433.71,
        Carbon = 5,
        Hydrogen = 12,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.7417703, m3 = 148.739),
        LHV = PhysicalProperties(kg = 45.0472805, m3 = 137.465)
    )
    return Component

def CreateSO2():
    Component = GasComponent(
        Id = GasComponentIndex.SO2,
        # Redlich-Kwong Critical components
        FullName = "Sulphur Dioxide",
        Mw = 64.059,
        Name = "Sulphur Dioxide",
        Pcr = 7884,
        Tcr = 430.8,
        Carbon = 0,
        Hydrogen = 0,
        Nitrogen = 0,
        Sulphur = 1,
        Oxygen = 2,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateCO():
    Component = GasComponent(
        Id = GasComponentIndex.CO,
        FullName = "Carbon Monoxide",
        Mw = 28.0104,
        Name = "CO",
        Pcr = 3494,
        Tcr = 132.86,
        Carbon = 1,
        Hydrogen = 0,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 1,
        HHV = PhysicalProperties(kg = 10.0945919, m3 = 11.959),
        LHV = PhysicalProperties(kg = 10.0945919, m3 = 11.959)
    )
    return Component;

def CreateH2():

    Component = GasComponent(
        Id = GasComponentIndex.H2,
        FullName = "Hydrogen",
        Mw = 2.016,
        Name = "H2",
        Pcr = 1293,
        Tcr = 33,
        SRK_w = -0.2202,
        SRK_CpA = 27.143,
        SRK_CpB = 0.009273,
        SRK_CpC = -1.38E-05,
        SRK_CpD = 7.645E-09,
        PR_a = -49.68,
        PR_b = 13.84,
        PR_c = 0.0003,
        PR_d = 3.46E-07,
        PR_e = -9.71E-11,
        PR_f = 7.73E-15,
        PR_w = -0.1201,
        Carbon = 0,
        Hydrogen = 2,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 141.82743, m3 = 12.091),
        LHV = PhysicalProperties(kg = 121.0536, m3 = 10.32)
    )
    return Component

def CreateAR():

    Component = GasComponent(
        Id = GasComponentIndex.Ar,
        FullName = "Argon",
        Mw = 39.948,
        Name = "A",
        Pcr = 4870,
        Tcr = 150.8,
        Carbon = 0,
        Hydrogen = 0,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateO2():

    Component = GasComponent(
        Id = GasComponentIndex.O2,
        FullName = "Oxygen",
        Mw = 31.9988,
        Name = "O2",
        Pcr = 5043,
        Tcr = 154.59,
        PR_a = -2.283,
        PR_b = 0.952,
        PR_c = -0.000281,
        PR_d = 6.55E-07,
        PR_e = -4.52E-10,
        PR_f = 1.09E-13,
        PR_w = 0.019,
        Carbon = 0,
        Hydrogen = 0,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 2,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateH2O():

    Component = GasComponent(
        Id = GasComponentIndex.H2O,
        FullName = "Water",
        Mw = 18.0154,
        Name = "H2O",
        Pcr = 22064,
        Tcr = 647.1,
        SRK_w = 0.3443,
        SRK_CpA = 32.243,
        SRK_CpB = 0.001923,
        SRK_CpC = 1.055E-05,
        SRK_CpD = -3.596E-09,
        PR_a = -5.73,
        PR_b = 1.915,
        PR_c = -0.000396,
        PR_d = 8.76E-07,
        PR_e = -4.95E-10,
        PR_f = 1.04E-13,
        PR_w = 0.344,
        Carbon = 0,
        Hydrogen = 2,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 1,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateHE():    
    Component = GasComponent(
        Id = GasComponentIndex.HE,
        FullName = "Helium",
        Mw = 4.0026,
        Name = "HE",
        Pcr = 227.5,
        Tcr = 5.2,
        Carbon = 0,
        Hydrogen = 0,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateH2S():    
    Component = GasComponent(
        Id = GasComponentIndex.H2S,
        FullName = "Hydrogen Sulphide",
        Mw = 34.082,
        Name = "H2S",
        Pcr = 8963,
        Tcr = 373.37,
        SRK_w = 0.081,
        SRK_CpA = 31.941,
        SRK_CpB = 0.001436,
        SRK_CpC = 2.432E-05,
        SRK_CpD = -1.176E-08,
        PR_a = -1.435,
        PR_b = 0.9985,
        PR_c = -0.000184,
        PR_d = 5.57E-07,
        PR_e = -3.18E-10,
        PR_f = 6.37E-14,
        PR_w = 0.081,
        Carbon = 1,
        Hydrogen = 2,
        Nitrogen = 0,
        Sulphur = 1,
        Oxygen = 1,
        HHV = PhysicalProperties(kg = 16.5085749, m3 = 23.791),
        LHV = PhysicalProperties(kg = 15.2047368, m3 = 21.912)
    )
    return Component

def CreateN2():    
    Component = GasComponent(
        Id = GasComponentIndex.N2,
        FullName = "Nitrogen",
        Mw = 28.0134,
        Name = "N2",
        Pcr = 3398,
        Tcr = 126.21,
        SRK_w = 0.0372,
        SRK_CpA = 31.15,
        SRK_CpB = -0.01356,
        SRK_CpC = 2.679E-05,
        SRK_CpD = -1.168E-08,
        PR_a = 2.889,
        PR_b = 0.9827,
        PR_c = 9.71E-05,
        PR_d = -4.16E-10,
        PR_e = -3.66E-12,
        PR_f = 4.05E-16,
        PR_w = 0.04,
        Carbon = 0,
        Hydrogen = 0,
        Nitrogen = 2,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateCO2():    
    Component = GasComponent(
        Id = GasComponentIndex.CO2,
        FullName = "Carbon Dioxide",
        Mw = 44.0098,
        Name = "CO2",
        Pcr = 7374,
        Tcr = 304.11,
        SRK_w = 0.2667,
        SRK_CpA = 19.795,
        SRK_CpB = 0.07343,
        SRK_CpC = -5.601E-05,
        SRK_CpD = 1.715E-08,
        PR_a = 0,
        PR_b = 0.6181,
        PR_c = 0.000485,
        PR_d = -1.49E-07,
        PR_e = 2.29E-11,
        PR_f = -1.37E-15,
        PR_w = 0.2389,
        Carbon = 1,
        Hydrogen = 0,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 2,
        HHV = PhysicalProperties(kg = 0, m3 = 0),
        LHV = PhysicalProperties(kg = 0, m3 = 0)
    )
    return Component

def CreateC10():
    Component = GasComponent(
        Id = GasComponentIndex.C10,
        FullName = "Decane",
        Mw = 142.286,
        Name = "C10",
        Pcr = 2100,
        Tcr = 617.7,
        SRK_w = 0.4898,
        SRK_CpA = -7.913,
        SRK_CpB = 0.9608,
        SRK_CpC = 0.0005287,
        SRK_CpD = 1.13E-07,
        PR_a = 0,
        PR_b = -0.0556,
        PR_c = 0.00338,
        PR_d = -1.24E-06,
        PR_e = 1.99E-10,
        PR_f = -3.7E-23,
        PR_w = 0.4885,
        Carbon = 10,
        Hydrogen = 22,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.0427692, m3 = 289.066),
        LHV = PhysicalProperties(kg = 44.6074152, m3 = 268.396)
    )
    return Component


def CreateC9():
    Component = GasComponent(
        Id = GasComponentIndex.C9,
        FullName = "Nonane",
        Mw = 128.259,
        Name = "C9",
        Pcr = 2280,
        Tcr = 594.7,
        SRK_w = 0.4445,
        SRK_CpA = 3.144,
        SRK_CpB = 0.6774,
        SRK_CpC = -0.0001928,
        SRK_CpD = -2.981E-08,
        PR_a = 0,
        PR_b = -0.0653,
        PR_c = 0.0034,
        PR_d = -1.25E-06,
        PR_e = 2.01E-10,
        PR_f = -2.24E-23,
        PR_w = 0.4455,
        Carbon = 9,
        Hydrogen = 20,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.1371327, m3 = 261.189),
        LHV = PhysicalProperties(kg = 44.6739514, m3 = 242.398)
    )
    return Component


def CreateC8():
    Component = GasComponent(
        Id = GasComponentIndex.C8,
        FullName = "Octane",
        Mw = 114.232,
        Name = "C8",
        Pcr = 2490,
        Tcr = 568.4,
        SRK_w = 0.3977,
        SRK_CpA = -6.096,
        SRK_CpB = 0.7712,
        SRK_CpC = -0.0004195,
        SRK_CpD = 8.855E-08,
        PR_a = 126.5,
        PR_b = -0.2701,
        PR_c = 0.004,
        PR_d = -1.97E-06,
        PR_e = 6.23E-10,
        PR_f = -9.38E-14,
        PR_w = 0.4018,
        Carbon = 8,
        Hydrogen = 18,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.290202, m3 = 233.286),
        LHV = PhysicalProperties(kg = 44.789418, m3 = 216.374)
    )
    return Component


def CreateC7():
    Component = GasComponent(
        Id = GasComponentIndex.C7,
        FullName = "Heptane",
        Mw = 100.205,
        Name = "C7",
        Pcr = 2740,
        Tcr = 539.2,
        SRK_w = 0.3494,
        SRK_CpA = -5.146,
        SRK_CpB = 0.6761,
        SRK_CpC = -0.000365,
        SRK_CpD = 7.657E-08,
        PR_a = 71.41,
        PR_b = -0.0969,
        PR_c = 0.00347,
        PR_d = -1.33E-06,
        PR_e = 2.56E-10,
        PR_f = -1.38E-14,
        PR_w = 0.3498,
        Carbon = 7,
        Hydrogen = 16,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.481716, m3 = 205.431),
        LHV = PhysicalProperties(kg = 44.933928, m3 = 190.398)
    )
    return Component


def CreateC6():
    Component = GasComponent(
        Id = GasComponentIndex.C6,
        FullName = "Hexane",
        Mw = 86.178,
        Name = "C6",
        Pcr = 3030,
        Tcr = 506.4,
        SRK_w = 0.2994,
        SRK_CpA = -4.413,
        SRK_CpB = 0.05819,
        SRK_CpC = -0.0003118,
        SRK_CpD = 6.493E-08,
        PR_a = 74.51,
        PR_b = -0.0967,
        PR_c = 0.00348,
        PR_d = -1.32E-06,
        PR_e = 2.52E-10,
        PR_f = -1.35E-14,
        PR_w = 0.3007,
        Carbon = 6,
        Hydrogen = 14,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.7213664, m3 = 177.556),
        LHV = PhysicalProperties(kg = 45.1119088, m3 = 164.402)
    )
    return Component


def CreateNC5():
    Component = GasComponent(
        Id = GasComponentIndex.NC5,
        FullName = "Pentane",
        Mw = 72.151,
        Name = "NC5",
        Pcr = 3365,
        Tcr = 469.65,
        SRK_w = 0.2514,
        SRK_CpA = -3.626,
        SRK_CpB = 0.4873,
        SRK_CpC = -0.000258,
        SRK_CpD = 5.304E-08,
        PR_a = 63.2,
        PR_b = -0.0117,
        PR_c = 0.00332,
        PR_d = -1.17E-06,
        PR_e = 2E-10,
        PR_f = -8.67E-15,
        PR_w = 0.2539,
        Carbon = 5,
        Hydrogen = 12,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 49.0416158, m3 = 149.654),
        LHV = PhysicalProperties(kg = 45.347126, m3 = 138.38)
    )
    return Component

def CreateIC5():
    Component = GasComponent(
        Id = GasComponentIndex.IC5,
        FullName = "Iso Pentane",
        Mw = 72.151,
        Name = "IC5",
        Pcr = 3381,
        Tcr = 460.35,
        SRK_w = 0.228,
        SRK_CpA = -9.525,
        SRK_CpB = 0.5066,
        SRK_CpC = -0.0002729,
        SRK_CpD = 5.723E-08,
        PR_a = 64.25,
        PR_b = -0.1318,
        PR_c = 0.00354,
        PR_d = -1.33E-06,
        PR_e = 2.51E-10,
        PR_f = -1.3E-14,
        PR_w = 0.2222,
        Carbon = 5,
        Hydrogen = 12,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 48.9318363, m3 = 149.319),
        LHV = PhysicalProperties(kg = 45.2370188, m3 = 138.044)
    )
    return Component

def CreateNC4():
    Component = GasComponent(
        Id = GasComponentIndex.NC4,
        FullName = "n Butane",
        Mw = 58.124,
        Name = "NC4",
        Pcr = 3784,
        Tcr = 425.1,
        SRK_w = 0.1995,
        SRK_CpA = 9.487,
        SRK_CpB = 0.3313,
        SRK_CpC = -0.0001108,
        SRK_CpD = -2.821E-09,
        PR_a = 67.72,
        PR_b = 0.0085,
        PR_c = 0.00328,
        PR_d = -1.11E-06,
        PR_e = 1.77E-10,
        PR_f = -6.4E-15,
        PR_w = 0.201,
        Carbon = 4,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 49.5396972, m3 = 121.779),
        LHV = PhysicalProperties(kg = 45.7178112, m3 = 112.384)
    )
    return Component

def CreateIC4():
    Component = GasComponent(
        Id = GasComponentIndex.IC4,
        FullName = "Iso Butane",
        Mw = 58.124,
        Name = "IC4",
        Pcr = 3640,
        Tcr = 407.82,
        SRK_w = 0.1852,
        SRK_CpA = -1.39,
        SRK_CpB = 0.3847,
        SRK_CpC = -0.0001846,
        SRK_CpD = 2.895E-08,
        PR_a = 30.9,
        PR_b = 0.1533,
        PR_c = 0.00264,
        PR_d = 7.27E-08,
        PR_e = -7.28E-10,
        PR_f = 2.37E-13,
        PR_w = 0.1848,
        Carbon = 4,
        Hydrogen = 10,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 49.3960968, m3 = 121.426),
        LHV = PhysicalProperties(kg = 45.5742108, m3 = 112.031)
    )

    return Component

def CreateC3():
    Component = GasComponent(
        Id = GasComponentIndex.C3,
        FullName = "Propane",
        Mw = 44.097,
        Name = "C3",
        Pcr = 4240,
        Tcr = 369.77,
        SRK_w = 0.1522,
        SRK_CpA = -4.224,
        SRK_CpB = 0.3062,
        SRK_CpC = -0.0001586,
        SRK_CpD = 3.214E-08,
        PR_a = 39.49,
        PR_b = 0.395,
        PR_c = 0.00211,
        PR_d = 3.97E-07,
        PR_e = -6.67E-10,
        PR_f = 1.68E-13,
        PR_w = 0.1524,
        Carbon = 3,
        Hydrogen = 8,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 50.3877864, m3 = 93.972),
        LHV = PhysicalProperties(kg = 46.3577072, m3 = 86.456)
    )
    return Component

def CreateC2():
    Component = GasComponent(
        Id = GasComponentIndex.C2,
        FullName = "Ethane",
        Mw = 30.07,
        Name = "C2",
        Pcr = 4880,
        Tcr = 305.41,
        SRK_w = 0.0979,
        SRK_CpA = 5.409,
        SRK_CpB = 0.1781,
        SRK_CpC = -6.937E-05,
        SRK_CpD = 8.712E-09,
        PR_a = -1.768,
        PR_b = 1.143,
        PR_c = -0.000324,
        PR_d = 4.24E-06,
        PR_e = -3.39E-09,
        PR_f = 8.82E-13,
        PR_w = 0.0986,
        Carbon = 2,
        Hydrogen = 6,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        HHV = PhysicalProperties(kg = 51.9209616, m3 = 66.032),
        LHV = PhysicalProperties(kg = 47.4885885, m3 = 60.395)
    )
    return Component


def CreateC1():
    Component = GasComponent(
        Id = GasComponentIndex.C1,
        FullName = "Methane",
        Mw = 16.043,
        Name = "C1",
        Pcr = 4599,
        Tcr = 190.56,
        SRK_w = 0.0104,
        SRK_CpA = 19.251,
        SRK_CpB = 0.05212,
        SRK_CpC = 1.197E-05,
        SRK_CpD = 1.31E-08,
        PR_a = -12.98,
        PR_b = 2.365,
        PR_c = -0.00213,
        PR_d = 5.66E-06,
        PR_e = -3.73E-09,
        PR_f = 8.61E-13,
        PR_w = 0.0115,
        Carbon = 1,
        Hydrogen = 4,
        Nitrogen = 0,
        Sulphur = 0,
        Oxygen = 0,
        # mj/kg mj/m3 at std conditions
        HHV = PhysicalProperties(kg= 55.560956, m3= 37.694),
        LHV = PhysicalProperties(kg= 50.021664, m3= 33.936)
    )
    return Component