class Separar:
    def dividir(texto, div):
        dividido = ""
        aux = list(texto)
        for idx, val in enumerate(texto):
            dividido += val + " " if (idx+1) % int(div) == 0 else val
        return dividido
