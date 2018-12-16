class Cifrar:
    def cifrado(texto, desplazamiento, alfabetoMay, alfabetoMin):
        aux1 = alfabetoMin.alfabeto()
        aux2 = alfabetoMay.alfabeto()
        aux3 = list(texto)
        cifrado = ""
        for c in texto:
            if (not(c not in aux1) or not(c not in aux2)):
                cifrado += aux1[((aux1.index(aux3[aux3.index(c)]))+int(desplazamiento))%len(aux1)] if not(c not in aux1) else aux2[((aux2.index(aux3[aux3.index(c)]))+int(desplazamiento))%len(aux2)]
            else:
                cifrado += c
        return cifrado
