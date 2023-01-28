def roger_ratio(carbon_di_oxide, carbon_monoxide,ethylene,ethane):
    ratio1 = carbon_di_oxide/carbon_monoxide
    ratio2 = ethylene/ethane
    if ratio1 >= 2:
        result = 'Transformer Okay'
    else:
        result = 'Need further analysis'
    return ratio1, ratio2, result
