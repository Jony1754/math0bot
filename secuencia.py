# Leer la secuencia como una lista
# seleccionar parejas
# Si la sumaa esta en la secuencia, añadir la sumaa y la pareja.
# Avanzar los iteradores
# Si la nueva sumaa tambien esta en la secuencia pero una de las parejas es menor que el ultimo elemento de la subsecuencia entonces no se añade.


def main(sequence, starting_index=0):
    subsequence = []
    for item in range(starting_index, len(sequence) - 1, 1):
        curr = sequence[item]
        sig = sequence[item + 1]
        suma = curr + sig
        if suma in sequence:
            subsequence.append(curr)
            subsequence.append(sig)
            subsequence.append(suma)
            break

    for subitem in range(0, len(subsequence) - 1, 1):
        curr2 = subsequence[len(subsequence) - 1]
        sig2 = subsequence[len(subsequence) - 2]
        suma2 = curr2 + sig2
        if suma2 in sequence:
            subsequence.append(suma2)

    return subsequence


main([0, 2, 3, 4, 5, 7, 11, 13, 18, 22, 28], 1)
# PARA EL EJEMPLO SE A;ADE ASID
# 0 2 2
# 0 2 2 4 -> 6 NO ESTA Y AQUI SE DETIENE