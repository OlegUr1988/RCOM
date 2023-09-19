from Enums import PhaseState

class PhaseOfMatter:
    
    def __init__(self):
        
        self.StlStreamPhaseArrayIndex = -1
        self.PhaseSTL = None
        self.State = PhaseState.Unknown
        self.Fraction = 0.0
        self.SpecificHeatRatio = 0.0
        self.Compressibility = 0.0
        self.MolecularWeight = 0.0
        self.Density = 0.0
        self.IsobaricSpecificHeatCp = 0.0
        self.IsochoricHeatCapacityCv = 0.0
        self.SpecificEnthalpy = 0.0
        self.SpecificEntropy = 0.0
        self.Viscosity = 0.0
        self.SurfaceTension = 0.0
    
    @property
    def K(self):
          return self.SpecificHeatRatio
    
    @property
    def Z(self):
          return self.Compressibility

    def IsStateKnown(self):
        return self.State != PhaseState.Unknown
    
        
