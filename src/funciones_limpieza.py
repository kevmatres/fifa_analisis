def limpiar_valor(val):
    if isinstance(val,str):
        if val.endswith("M"):
            return float(val.replace("M","")) * 1000000
        elif val.endswith("K"):
            return float(val.replace("K","")) * 1000
        else:
            return float(val)
    
    return None



def limpiar_altura_peso(val:str):
    if  isinstance(val[-2:],str):
        return int(val[:-2])
    else:
        return int(val)