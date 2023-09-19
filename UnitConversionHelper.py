from Enums import PhysicalQuantity
import Labels.TemperatureLabel as TemperatureLabel
import ConversionData.TemperatureConversion as TemperatureConversion

class UnitConversionHelper:
    @staticmethod
    def CalculateActualFlowUnitConversionValue(Za, Zb, actual_pressure, actual_temperature, base_pressure, base_temperature):
        conversion_value = (base_temperature / actual_temperature) * (actual_pressure / base_pressure) * (Zb / Za)
        return conversion_value

    @staticmethod
    def ConvertActualFlowToStandardFlow(flow, calculated_flow_conversion):
        return flow * calculated_flow_conversion

    @staticmethod
    def ConvertStandardFlowToActualFlow(flow, calculated_flow_conversion):
        return flow / calculated_flow_conversion

    @staticmethod
    def ConvertUnit(actual_value, unit_selection, core_unit=None):
        if unit_selection is None:
            return actual_value
        
        converted_value = actual_value * unit_selection.Input.Conversion.Factor

        if unit_selection.PhysicalQuantity == PhysicalQuantity.Temperature:
            if unit_selection.Input.Label == TemperatureLabel.F and core_unit == TemperatureLabel.K:
                converted_value = TemperatureConversion.FToK(actual_value)
            else:
                converted_value += unit_selection.Input.Conversion.Offset

        return converted_value
