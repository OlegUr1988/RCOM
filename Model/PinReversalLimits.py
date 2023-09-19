from Rcoms2Engine.Settings import *

class Rcoms2Engine: #this class replaces the original namespace 'Rcoms2Engine'
    class Models: #this class replaces the original namespace 'Models'
        #/ Class that defines all properties & functionality of a Pin Reversal Limits. These are basically used for Engineer's reference.
        class PinReversalLimits:
            _PinReversalLimitsReferences = None

        ##region Construction

            #/ Instantiate the Limits on creation of the Class
            @staticmethod
            def _static_initializer():
                temp_var = PinReversalLimit()
                temp_var.OEMOrRule = str(OEM.ARIEL)
                temp_var.MinimumDegrees = 30
                temp_var.MinimumOppositeForce = 25
                temp_var2 = PinReversalLimit()
                temp_var2.OEMOrRule = str(OEM.DRESSERRAND)
                temp_var2.MinimumDegrees = 40
                temp_var2.MinimumOppositeForce = 20
                temp_var3 = PinReversalLimit()
                temp_var3.OEMOrRule = str(OEM.GEMINI)
                temp_var3.MinimumDegrees = 60
                temp_var3.MinimumOppositeForce = 15
                temp_var4 = PinReversalLimit()
                temp_var4.OEMOrRule = str(OEM.SUPERIOR)
                temp_var4.MinimumDegrees = 30
                temp_var4.MinimumOppositeForce = 15
                temp_var5 = PinReversalLimit()
                temp_var5.OEMOrRule = "General High-Speed"
                temp_var5.MinimumDegrees = 45
                temp_var5.MinimumOppositeForce = 15
                temp_var6 = PinReversalLimit()
                temp_var6.OEMOrRule = "General Slow-Speed"
                temp_var6.MinimumDegrees = 15
                temp_var6.MinimumOppositeForce = 15
                Rcoms2Engine.Models.PinReversalLimits._PinReversalLimitsReferences = [temp_var, temp_var2, temp_var3, temp_var4, temp_var5, temp_var6]

            _static_initializer()

        ##endregion

        ##region Public Methods

            #/ Get the Pin Reversal Limits for Non Pre-configured limits.
            #/ Note: If no pre-configured limit is found, use the Rated Speed
            @staticmethod
            def GetPinReversalLimit(oem, ratedSpeed):
                pinReversalLimit = Rcoms2Engine.Models.PinReversalLimits._PinReversalLimitsReferences.FirstOrDefault(lambda x : x.OEMOrRule == str(oem))

                if pinReversalLimit is None:
                    OEMOrRule = "General Slow-Speed"

                    if ratedSpeed <= 440.0:
                        # Slow Speed Recip
                        OEMOrRule = "General Slow-Speed"
                    elif ratedSpeed > 440.0:
                        # High Speed Recip
                        OEMOrRule = "General High-Speed"

                    return Rcoms2Engine.Models.PinReversalLimits._PinReversalLimitsReferences.FirstOrDefault(lambda x : x.OEMOrRule == OEMOrRule)

                return pinReversalLimit
