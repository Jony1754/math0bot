# Leer la secuencia como una lista
# seleccionar parejas
# Si la suma esta en la secuencia, añadir la suma y la pareja.
# Avanzar los iteradores
# Si la nueva sumaa tambien esta en la secuencia pero una de las parejas es menor que el ultimo elemento de la subsecuencia entonces no se añade.


def get_subsequence(sequence, starting_index=0):
    subsequence = []
    if starting_index > len(sequence) - 1:
        return ValueError

    for item in range(starting_index, len(sequence) - 1, 1):
        curr = sequence[item]
        sig = sequence[item + 1]
        suma = curr + sig
        if suma in sequence:
            subsequence.append(curr)
            subsequence.append(sig)
            subsequence.append(suma)
            break

    for subitem in range(0, len(subsequence), 1):
        curr2 = subsequence[len(subsequence) - 1]
        sig2 = subsequence[len(subsequence) - 2]
        suma2 = curr2 + sig2
        if suma2 in sequence:
            subsequence.append(suma2)

    return subsequence
