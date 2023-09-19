InputMapping = [('CompType||Number of Stages','int','CT_NumberofStages'),
('CompType||Number of Bodies','int','CT_NumberofBodies'),
('Run Status||Run Status Tag','int','RS_RunStatusTag'),

('Unit||Pressure','str','U_Pressure'),
('Unit||Flow','str','U_Flow'),
('Unit||Temperature','str','U_Temperature'),
('Unit||Power','str','U_Power'),
('Unit||Length','str','U_Length'),
('Unit||Volume','str','U_Volume'),
('Unit||Weight','str','U_Weight'),
('Unit||Force','str','U_Force'),

('Driver||Primary Driver ModelId','str','DR_PrimaryDriverModelId'),
('Driver||Primary Driver Model File Name','str','DR_PrimaryDriverModelFileName'),
('Driver||Driver Type','int','DR_DriverType'),
('Driver||Rated Power','float','DR_Rated Power'),
('Driver||Rated Speed','float','DR_Rated Speed'),

('Limits||Speed by Design - Min','float','Limit_SD_Min'),
('Limits||Speed by Design - Max','float','Limit_SD_Max'),
('Limits||Operating Speed - Min','float','Limit_OS_Min'),
('Limits||Operating Speed - Max','float','Limit_OS_Max'),
('Limits||Driver Torque - Min','float','Limit_DT_Min'),
('Limits||Driver Torque - Max','float','Limit_DT_Max'),
('Limits||Suction Volumetric Efficiency - Min','float','Limit_SV_E_Min'),
('Limits||Suction Volumetric Efficiency - Max','float','Limit_SV_E_Max'),
('Limits||First Stage Suction Pressure - Min','float','Limit_FS_SP_Min'),
('Limits||First Stage Suction Pressure - Max','float','Limit_FS_SP_Max'),
('Limits||Last Stage Discharge Pressure - Min','float','Limit_LS_DP_Min'),
('Limits||Last Stage Discharge Pressure - Max','float','Limit_LS_DP_Max'),

('OperatingConditions||OEM','int','OC_OEM'),
('OperatingConditions||Rod Load Calculation Method','int','OC_RodLoadCalculationMethod'),
('OperatingConditions||Number Of Stages','int','OC_NumberOfStages'),
('OperatingConditions||Number Of Load Steps','int','OC_NumberOfLoadSteps'),
('OperatingConditions||Operating Speed','float','OC_OperatingSpeed'),
('OperatingConditions||Operating Load Step','int','OC_OperatingLoadStep'),
('OperatingConditions||Is Dual Service','bool','OC_IsDualService'),

('Other Service||Brake Power','float','OS_BrakePower'),
('Other Service||Torque','float','OS_Torque'),

('General||Atmospheric Pressure','float','GN_ATM_P'),
('General||Pressure at Standard/Normal Condition','float','GN_SP'), 
('General||Temperature at Standard/Normal Condition','float','GN_ATM_T'),  
('General||Flow Tune Factor','float','GN_FlowTuneFactor'),  
('General||Flow Meter Location','int','GN_FlowMeterLocation'),  

('Frame||Stroke','float','FM_Stroke'),
('Frame||Friction','float','FM_Friction'),
('Frame||Auxillary Load','float','FM_AuxillaryLoad'),
('Frame||Length Of Connecting Rod','float','FM_LengthOfConnectingRod'),
('Frame||Number Of Throws','int','FM_NumberOfThrows'),
('Frame||Number Of Cylinders','int','FM_NumberOfCylinders'),
('Frame||Mechanical Efficiency','float','FM_MechanicalEfficiency')]

LimitsStage = [('Limits||Stage [{stageno}] Suction Temperature at Transmitter - Min','float','Limit_Stage_{stageno}_ST_T_Min'),
               ('Limits||Stage [{stageno}] Suction Temperature at Transmitter - Max','float','Limit_Stage_{stageno}_ST_T_Max')]


Throws = [('Throw [{throwno}]||Throw Number','int','Throw_{throwno}_ThrowNumber'),
          ('Throw [{throwno}]||Is Cylinder Omitted','bool','Throw_{throwno}_IsCylinderOmitted'),
          ('Throw [{throwno}]||Rod Load Limit For Compression','int','Throw_{throwno}_RodLoadLimitForCompression'),
          ('Throw [{throwno}]||Rod Load Limit For Tension','int','Throw_{throwno}_RodLoadLimitForTension'),
          ('Throw [{throwno}]||Piston Weight','float','Throw_{throwno}_PistonWeight'),
          ('Throw [{throwno}]||Rod Weight','float','Throw_{throwno}_RodWeight'),
          ('Throw [{throwno}]||Nut Weight','float','Throw_{throwno}_NutWeight'),
          ('Throw [{throwno}]||Cross Head Weight','float','Throw_{throwno}_CrossHeadWeight'),
          ('Throw [{throwno}]||Cross Head Pin Weight','float','Throw_{throwno}_CrossHeadPinWeight'),
          ('Throw [{throwno}]||Cross Head Balance Weight','float','Throw_{throwno}_CrossHeadBalanceWeight')]

Stages = [('Stage [{stageno}]||Suction Fixed Pressure Drop','float','Stage_{stageno}_SuctionFixedPressureDrop'),
          ('Stage [{stageno}]||Suction Pressure Drop Percentage','float','Stage_{stageno}_SuctionPressureDropPercentage'),
          ('Stage [{stageno}]||Discharge Fixed Pressure Drop','float','Stage_{stageno}_DischargeFixedPressureDrop'),
          ('Stage [{stageno}]||Discharge Pressure Drop Percentage','float','Stage_{stageno}_DischargePressureDropPercentage'),
          ('Stage [{stageno}]||Suction Temperature at Transmitter','float','Stage_{stageno}_SuctionTemperatureAtTransmitter'),
          ('Stage [{stageno}]||Suction Pressure at Transmitter','float','Stage_{stageno}_SuctionPressureAtTransmitter'),
          ('Stage [{stageno}]||Discharge Temperature at Transmitter','float','Stage_{stageno}_DischargeTemperatureAtTransmitter'),
          ('Stage [{stageno}]||Discharge Pressure at Transmitter','float','Stage_{stageno}_DischargePressureAtTransmitter')]


GasRecipStage = [('Gas Recip Stage [{stageno}]||Gas Calc Type','int','GasRecip_Stage_{stageno}_GasCalcType'),
('Gas Recip Stage [{stageno}]||C1','float','GasRecip_Stage_{stageno}_C1'),
('Gas Recip Stage [{stageno}]||C2','float','GasRecip_Stage_{stageno}_C2'),
('Gas Recip Stage [{stageno}]||C3','float','GasRecip_Stage_{stageno}_C3'),
('Gas Recip Stage [{stageno}]||IC4','float','GasRecip_Stage_{stageno}_IC4'),
('Gas Recip Stage [{stageno}]||NC4','float','GasRecip_Stage_{stageno}_NC4'),
('Gas Recip Stage [{stageno}]||IC5','float','GasRecip_Stage_{stageno}_IC5'),
('Gas Recip Stage [{stageno}]||NC5','float','GasRecip_Stage_{stageno}_NC5'),
('Gas Recip Stage [{stageno}]||C6','float','GasRecip_Stage_{stageno}_C6'),
('Gas Recip Stage [{stageno}]||C7','float','GasRecip_Stage_{stageno}_C7'),
('Gas Recip Stage [{stageno}]||C8','float','GasRecip_Stage_{stageno}_C8'),
('Gas Recip Stage [{stageno}]||C9','float','GasRecip_Stage_{stageno}_C9'),
('Gas Recip Stage [{stageno}]||C10','float','GasRecip_Stage_{stageno}_C10'),
('Gas Recip Stage [{stageno}]||CO2','float','GasRecip_Stage_{stageno}_CO2'),
('Gas Recip Stage [{stageno}]||N2','float','GasRecip_Stage_{stageno}_N2'),
('Gas Recip Stage [{stageno}]||H2S','float','GasRecip_Stage_{stageno}_H2S'),
('Gas Recip Stage [{stageno}]||HE','float','GasRecip_Stage_{stageno}_HE'),
('Gas Recip Stage [{stageno}]||H2O','float','GasRecip_Stage_{stageno}_H2O'),
('Gas Recip Stage [{stageno}]||O2','float','GasRecip_Stage_{stageno}_O2'),
('Gas Recip Stage [{stageno}]||A','float','GasRecip_Stage_{stageno}_A'),
('Gas Recip Stage [{stageno}]||H2','float','GasRecip_Stage_{stageno}_H2'),
('Gas Recip Stage [{stageno}]||CO','float','GasRecip_Stage_{stageno}_CO'),
('Gas Recip Stage [{stageno}]||Sulphur Dioxide','float','GasRecip_Stage_{stageno}_SulphurDioxide'),
('Gas Recip Stage [{stageno}]||Neo-Pentane','float','GasRecip_Stage_{stageno}_NeoPentane'),
('Gas Recip Stage [{stageno}]||Neo-Hexane','float','GasRecip_Stage_{stageno}_NeoHexane'),
('Gas Recip Stage [{stageno}]||Iso-Octane','float','GasRecip_Stage_{stageno}_IsoOctane'),
('Gas Recip Stage [{stageno}]||Ethene','float','GasRecip_Stage_{stageno}_Ethene'),
('Gas Recip Stage [{stageno}]||Propene','float','GasRecip_Stage_{stageno}_Propene'),
('Gas Recip Stage [{stageno}]||1-Butene','float','GasRecip_Stage_{stageno}_1Butene'),
('Gas Recip Stage [{stageno}]||cis-2-Butene','float','GasRecip_Stage_{stageno}_cis2Butene'),
('Gas Recip Stage [{stageno}]||trans-2-Butene','float','GasRecip_Stage_{stageno}_trans2Butene'),
('Gas Recip Stage [{stageno}]||Iso-Butene','float','GasRecip_Stage_{stageno}_IsoButene'),
('Gas Recip Stage [{stageno}]||1-Pentene','float','GasRecip_Stage_{stageno}_1Pentene'),
('Gas Recip Stage [{stageno}]||Acetylene','float','GasRecip_Stage_{stageno}_Acetylene'),
('Gas Recip Stage [{stageno}]||Benzene','float','GasRecip_Stage_{stageno}_Benzene'),
('Gas Recip Stage [{stageno}]||Toluene','float','GasRecip_Stage_{stageno}_Toluene'),
('Gas Recip Stage [{stageno}]||Ethyl Benzene','float','GasRecip_Stage_{stageno}_EthylBenzene'),
('Gas Recip Stage [{stageno}]||O-xylene','float','GasRecip_Stage_{stageno}_Oxylene'),
('Gas Recip Stage [{stageno}]||M-xylene','float','GasRecip_Stage_{stageno}_Mxylene'),
('Gas Recip Stage [{stageno}]||Pxylene','float','GasRecip_Stage_{stageno}_Pxylene'),
('Gas Recip Stage [{stageno}]||Styrene','float','GasRecip_Stage_{stageno}_Styrene'),
('Gas Recip Stage [{stageno}]||Methyl Alcohol','float','GasRecip_Stage_{stageno}_MethylAlcohol'),
('Gas Recip Stage [{stageno}]||Ethyl Alcohol','float','GasRecip_Stage_{stageno}_EthylAlcohol'),
('Gas Recip Stage [{stageno}]||Ammonia','float','GasRecip_Stage_{stageno}_Ammonia')]


SideStream =[('Stage [{stageno}] Sidestream-In||Flow Meter Type','int','Stage_{stageno}_SS_IN_FlowMeterType'),
          ('Stage [{stageno}] Sidestream-In||Flow Meter','str','Stage_{stageno}_SS_IN_FlowMeter'),
          ('Stage [{stageno}] Sidestream-In||Flow Meter Temperature','float','Stage_{stageno}_SS_IN_FlowMeterTemperature'),
          ('Stage [{stageno}] Sidestream-Out||Flow Meter Type','int','Stage_{stageno}_SS_OUT_FlowMeterType'),
          ('Stage [{stageno}] Sidestream-Out||Flow Meter','str','Stage_{stageno}_SS_Out_FlowMeter')]

LoadStep_Cylinderno =[('LoadStep [{loadstep}]||Number','int','LoadStep_{loadstep}_No'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Name','str','LoadStep_{loadstep}_CL_{cylinderno}_Name'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Head End - Is Active','bool','LoadStep_{loadstep}_CL_{cylinderno}_HE_IsActive'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Head End - Total Active Pocket Clearance','float','LoadStep_{loadstep}_CL_{cylinderno}_HE_TotalActivePocketClearance'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Head End - Pocket Position','float','LoadStep_{loadstep}_CL_{cylinderno}_HE_PocketPosition'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Crank End - Is Active','bool','LoadStep_{loadstep}_CL_{cylinderno}_CE_IsActive'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Crank End - Total Active Pocket Clearance','float','LoadStep_{loadstep}_CL_{cylinderno}_CE_TotalActivePocketClearance'),
                      ('LoadStep [{loadstep}]||Cylinder [{cylinderno}] Crank End - Pocket Position','float','LoadStep_{loadstep}_CL_{cylinderno}_CE_PocketPosition')]

Cylinders = [('Cylinder [{cylinderno}]||Serial Number','float','Cylinder_{cylinderno}_SN'),
          ('Cylinder [{cylinderno}]||Name','str','Cylinder_{cylinderno}_Name'),
          ('Cylinder [{cylinderno}]||Throw Number','int','Cylinder_{cylinderno}_ThrowNumber'),
          ('Cylinder [{cylinderno}]||Stage Number','int','Cylinder_{cylinderno}_StageNumber'),
          ('Cylinder [{cylinderno}]||Maximum Allowable Working Pressure','float','Cylinder_{cylinderno}_MaximumAllowableWorkingPressure'),
          ('Cylinder [{cylinderno}]||Maximum Allowed Discharge Temperature','float','Cylinder_{cylinderno}_MaximumAllowedDischargeTemperature'),
          ('Cylinder [{cylinderno}]||Bore Diameter','float','Cylinder_{cylinderno}_BoreDiameter'),
          ('Cylinder [{cylinderno}]||Discharge Temperature at Flange','float','Cylinder_{cylinderno}_DischargeTemperatureAtFlange'),     
          
          ('Cylinder [{cylinderno}]||Head End - Base Clearance','float','Cylinder_{cylinderno}_HEBaseClearance'),
          ('Cylinder [{cylinderno}]||Head End - % Clearance per inch travel','float','Cylinder_{cylinderno}_HEPerClearancePerInchTravel'),
          ('Cylinder [{cylinderno}]||Head End - Rod Diameter','float','Cylinder_{cylinderno}_HERodDiameter'),
          ('Cylinder [{cylinderno}]||Head End - Resistance Factor At Suction - Active End','float','Cylinder_{cylinderno}_HEResistanceFactorAtSuctionActiveEnd'),
          ('Cylinder [{cylinderno}]||Head End - Resistance Factor At Discharge - Active End','float','Cylinder_{cylinderno}_HEResistanceFactorAtDischargeActiveEnd'),
          ('Cylinder [{cylinderno}]||Head End - Resistance Factor At Suction - Deactivated End','float','Cylinder_{cylinderno}_HEResistanceFactorAtSuctionDeactiveEnd'),
          ('Cylinder [{cylinderno}]||Head End - Number Of Suction Valves','int','Cylinder_{cylinderno}_HENumberOfSuctionValves'),
          ('Cylinder [{cylinderno}]||Head End - Suction Valve - Valve Nose Diameter','float','Cylinder_{cylinderno}_HESuctionValveValveNoseDiameter'),
          ('Cylinder [{cylinderno}]||Head End - Number Of Discharge Valves','int','Cylinder_{cylinderno}_HENumberOfDischargeValves'),
          ('Cylinder [{cylinderno}]||Head End - Discharge Valve - Valve Nose Diameter','float','Cylinder_{cylinderno}_HEDischargeValveValveNoseDiameter'),
          
          ('Cylinder [{cylinderno}]||Crank End - Base Clearance','float','Cylinder_{cylinderno}_CEBaseClearance'),
          ('Cylinder [{cylinderno}]||Crank End - % Clearance per inch travel','float','Cylinder_{cylinderno}_CEPerClearancePerInchTravel'),
          ('Cylinder [{cylinderno}]||Crank End - Rod Diameter','float','Cylinder_{cylinderno}_CERodDiameter'),
          ('Cylinder [{cylinderno}]||Crank End - Resistance Factor At Suction - Active End','float','Cylinder_{cylinderno}_CEResistanceFactorAtSuctionActiveEnd'),
          ('Cylinder [{cylinderno}]||Crank End - Resistance Factor At Discharge - Active End','float','Cylinder_{cylinderno}_CEResistanceFactorAtDischargeActiveEnd'),
          ('Cylinder [{cylinderno}]||Crank End - Resistance Factor At Suction - Deactivated End','float','Cylinder_{cylinderno}_CEResistanceFactorAtSuctionDeactiveEnd'),
          ('Cylinder [{cylinderno}]||Crank End - Number Of Suction Valves','int','Cylinder_{cylinderno}_CENumberOfSuctionValves'),
          ('Cylinder [{cylinderno}]||Crank End - Suction Valve - Valve Nose Diameter','float','Cylinder_{cylinderno}_CESuctionValveValveNoseDiameter'),
          ('Cylinder [{cylinderno}]||Crank End - Number Of Suction Valves','int','Cylinder_{cylinderno}_CENumberOfDischargeValves'),
          ('Cylinder [{cylinderno}]||Crank End - Discharge Valve - Valve Nose Diameter','float','Cylinder_{cylinderno}_CEDischargeValveValveNoseDiameter')]





























