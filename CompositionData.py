from Enums import EOSModelType
import GasComponentFactory
import GasComponentLabel
from GasComponentData import GasComponentData

class CompositionData:
    
    def __init__(self):
        
        self.AbsoluteMoleSum = 0.0
        self.EnthalpyOffset = 0.0
        self.EntropyOffset = 0.0
        
        self.VapourDensity = 0.0 
        self.VapourViscosity = 0.0

        self.Components = []
        self.InitialiseGasComposition()
        self.GasComponentCollection = GasComponentFactory.CreateGasComponentsExtended()
        
        self.EquationofStateModel = EOSModelType.NoModel

        self.Mw = 0.0
        self.K = 0.0
        self.Z = 0.0
        
    def CalculateAbsoluteMoleSum(self):
        self.AbsoluteMoleSum = 0.0
        for item in self.Components:
            self.AbsoluteMoleSum += item.Value

    def InitialiseGasComposition(self):

        H2 = GasComponentData("H2", GasComponentLabel.H2, "H2", "H2", 0)
        He = GasComponentData("HE", GasComponentLabel.He, "HE", "HE", 0)
        N2 = GasComponentData("N2", GasComponentLabel.N2, "N2", "N2", 0)
        Co2 = GasComponentData("CO2", GasComponentLabel.CO2, "CO2", "CO2", 0)
        H2s = GasComponentData("H2S", GasComponentLabel.H2S, "H2S", "H2S", 0)
        C1 = GasComponentData("C1", GasComponentLabel.C1, "1P", "C1", 0)
        C2 = GasComponentData("C2", GasComponentLabel.C2, "2P", "C2", 0)
        C3 = GasComponentData("C3", GasComponentLabel.C3, "3P", "C3", 0)
        IC4 = GasComponentData("IC4", GasComponentLabel.IC4, "4P1", "IC4", 0)
        Nc4 = GasComponentData("NC4", GasComponentLabel.Nc4, "4P", "NC4", 0)
        IC5 = GasComponentData("IC5", GasComponentLabel.IC5, "5P1", "IC5", 0)
        Nc5 = GasComponentData("NC5", GasComponentLabel.Nc5, "5P", "NC5", 0)
        C6 = GasComponentData("C6", GasComponentLabel.C6, "6P", "C6", 0)
        C7 = GasComponentData("C7", GasComponentLabel.C7, "7P", "C7", 0)
        C8 = GasComponentData("C8", GasComponentLabel.C8, "8P", "C8", 0)
        C9 = GasComponentData("C9", GasComponentLabel.C9, "9P", "C9", 0)
        C10 = GasComponentData("C10", GasComponentLabel.C10, "10P", "C10", 0)
        H2o = GasComponentData("H2O", GasComponentLabel.H2O, "H2O", "H2O", 0)
        O2 = GasComponentData("O2", GasComponentLabel.O2, "O2", "O2", 0)
        A = GasComponentData("A", GasComponentLabel.Ar, "AR", "AR", 0)
        Co = GasComponentData("CO", GasComponentLabel.CO, "CO", "CO", 0)
        SulphurDioxide = GasComponentData("SulphurDioxide", GasComponentLabel.SulphurDioxide, "SO2", "Sulphur Dioxide", 0)
        NeoPentane = GasComponentData("NeoPentane", GasComponentLabel.NeoPentane, "5P2", "Neo-Pentane", 0)
        NeoHexane = GasComponentData("NeoHexane", GasComponentLabel.NeoHexane, "6P3", "Neo-Hexane", 0)
        IsoOctane = GasComponentData("IsoOctane", GasComponentLabel.IsoOctane, "8PE", "Iso-Octane", 0)
        Ethene = GasComponentData("Ethene", GasComponentLabel.Ethene, "2O", "Ethene", 0)
        Propene = GasComponentData("Propene", GasComponentLabel.Propene, "3O", "Propene", 0)
        OneButene = GasComponentData("1Butene", GasComponentLabel.OneButene, "4O", "1-Butene", 0)
        Cis2Butene = GasComponentData("cis2Butene", GasComponentLabel.Cis2Butene, "4O1", "cis-2-Butene", 0)
        Trans2Butene = GasComponentData("trans2Butene", GasComponentLabel.Trans2Butene, "4O2", "trans-2-Butene", 0)
        IsoButene = GasComponentData("IsoButene", GasComponentLabel.IsoButene, "4O3", "Iso-Butene", 0)
        OnePentene = GasComponentData("1Pentene", GasComponentLabel.OnePentene, "5O", "1-Pentene", 0)
        Acetylene = GasComponentData("Acetylene", GasComponentLabel.Acetylene, "2T", "Acetylene", 0)
        Benzene = GasComponentData("Benzene", GasComponentLabel.Benzene, "6A", "Benzene", 0)
        Toluene = GasComponentData("Toluene", GasComponentLabel.Toluene, "7A", "Toluene", 0)
        EthylBenzene = GasComponentData("EthylBenzene", GasComponentLabel.EthylBenzene, "8A", "Ethyl Benzene", 0)
        Oxylene = GasComponentData("Oxylene", GasComponentLabel.Oxylene, "8A1", "O-xylene", 0)
        Mxylene = GasComponentData("Mxylene", GasComponentLabel.Mxylene, "8A2", "M-xylene", 0)
        Pxylene = GasComponentData("Pxylene", GasComponentLabel.Pxylene, "8A3", "Pxylene", 0)
        Styrene = GasComponentData("Styrene", GasComponentLabel.Styrene, "8S", "Styrene", 0)
        MethylAlcohol = GasComponentData("MethylAlcohol", GasComponentLabel.MethylAlcohol, "MEOH", "Methyl Alcohol", 0)
        EthylAlcohol = GasComponentData("EthylAlcohol", GasComponentLabel.EthylAlcohol, "ETOH", "Ethyl Alcohol", 0)
        Ammonia = GasComponentData("Ammonia", GasComponentLabel.Ammonia, "NH3", "Ammonia", 0)

        self.Components.append(H2)
        self.Components.append(He)
        self.Components.append(N2)
        self.Components.append(Co2)
        self.Components.append(H2s)
        self.Components.append(C1)
        self.Components.append(C2)
        self.Components.append(C3)
        self.Components.append(IC4)
        self.Components.append(Nc4)
        self.Components.append(IC5)
        self.Components.append(Nc5)
        self.Components.append(C6)
        self.Components.append(C7)
        self.Components.append(C8)
        self.Components.append(C9)
        self.Components.append(C10)
        self.Components.append(H2o)
        self.Components.append(O2)
        self.Components.append(A)
        self.Components.append(Co)
        self.Components.append(SulphurDioxide)
        self.Components.append(NeoPentane)
        self.Components.append(NeoHexane)
        self.Components.append(IsoOctane)
        self.Components.append(Ethene)
        self.Components.append(Propene)
        self.Components.append(OneButene)
        self.Components.append(Cis2Butene)
        self.Components.append(Trans2Butene)
        self.Components.append(IsoButene)
        self.Components.append(OnePentene)
        self.Components.append(Acetylene)
        self.Components.append(Benzene)
        self.Components.append(Toluene)
        self.Components.append(EthylBenzene)
        self.Components.append(Oxylene)
        self.Components.append(Mxylene)
        self.Components.append(Pxylene)
        self.Components.append(Styrene)
        self.Components.append(MethylAlcohol)
        self.Components.append(EthylAlcohol)
        self.Components.append(Ammonia)