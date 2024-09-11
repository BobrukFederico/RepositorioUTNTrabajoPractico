#Chat gpt funcion:
#def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones
#= 15):
    #resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
    #resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
    #resultado_final = resultado_nacional + resultado_exportaciones
    #return resultado_final

def resultado_nacional(valor_ventas_nacionales:float, iva:float):
    '''
    Calcula el valor de las ventas nacionales con IVA aplicado

    Parametros:
    valor_ventas_nacionales: el valor total de las ventas nacionales sin iva

    iva: El porcentaje del IVA aplicado a las ventas


    '''
    resultado = valor_ventas_nacionales * (1 / (1 + (iva / 100)))
    return resultado

def resultado_exportaciones(valor_exportaciones:float, retenciones:float = 15):

    '''
        Calcula las ventas de las exportaciones con las retenciones

    '''

    resultado_exportacion = valor_exportaciones * (1 - (retenciones / 100))
    return resultado_exportacion


def resultado_final(resultado_nac, resultado_exp):

    '''
        Suma el resultado_exportaciones con el resultado_nacional
        Para sacar el resultado final

        Parametros:

        resultado_nac = Resultado de la funcion resultado_nacional()
        resultado_exp = Resultado de la funcion resultado_exportaciones()
    '''

    resultado = resultado_nac + resultado_exp
    return resultado