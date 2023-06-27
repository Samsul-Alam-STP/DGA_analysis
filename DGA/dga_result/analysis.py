<<<<<<< HEAD


def roger_ratio(ethylene,ethane,methane, acetylene,hydrogen):
    ratio_c2h2_c2h4 = acetylene/ethylene
    ratio_ch4_h2 = methane/hydrogen
    ratio_c2h4_c2h6 = ethylene/ethane
    result = ""
    if (ratio_c2h2_c2h4 <= 0.1 and (ratio_ch4_h2>=0.1 and ratio_ch4_h2<=1) and ratio_c2h4_c2h6<=1):
        result = "Case: 0 -> Unit normal."
    elif (ratio_c2h2_c2h4 <= 0.1 and ratio_ch4_h2<=.1 and ratio_c2h4_c2h6<=1):
        result = "Case: 1 -> Low-energy density arcing - PD"
    elif ((ratio_c2h2_c2h4 > 0.1 and ratio_c2h2_c2h4 <= 3) and (ratio_ch4_h2>=0.1 and ratio_ch4_h2<=1) and ratio_c2h4_c2h6>3):
        result = "Case: 2 -> Arcing - High energy discharge."
    elif (ratio_c2h2_c2h4 <= 0.1 and (ratio_ch4_h2>=0.1 and ratio_ch4_h2<=1) and (ratio_c2h4_c2h6>1 and ratio_c2h4_c2h6<=3)):
        result = "Case: 3 -> Low temperature thermal."
    elif (ratio_c2h2_c2h4 <= 0.1 and ratio_ch4_h2>1 and (ratio_c2h4_c2h6>1 and ratio_c2h4_c2h6<=3)):
        result = "Case: 4 -> Thermal < 700°C."
    elif (ratio_c2h2_c2h4 <= 0.1 and ratio_ch4_h2>1 and ratio_c2h4_c2h6>3):
        result = "Case: 5 -> Thermal > 700°C."
    else:
        result = "Rogers ratio is not applicable for this particular report."
    return ratio_c2h2_c2h4, ratio_ch4_h2, ratio_c2h4_c2h6, result


def co2_c0_ratio(carbon_di_oxide, carbon_monoxide):
    ratio_co2_co = carbon_di_oxide/carbon_monoxide
    return ratio_co2_co
    


=======
def roger_ratio(carbon_di_oxide, carbon_monoxide,ethylene,ethane):
    ratio1 = carbon_di_oxide/carbon_monoxide
    ratio2 = ethylene/ethane
    if ratio1 >= 2:
        result = 'Transformer Okay'
    else:
        result = 'Need further analysis'
    return ratio1, ratio2, result
>>>>>>> 9722bbbd343f5da9d344ea25d059419e6706a359
