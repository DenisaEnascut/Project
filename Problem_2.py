def numar_in_cuvinte(numar):
    # Dicționar cu cuvintele asociate cifrelor
    cifre = {
        0: 'zero', 1: 'unu', 2: 'doi', 3: 'trei', 4: 'patru',
        5: 'cinci', 6: 'șase', 7: 'șapte', 8: 'opt', 9: 'nouă'
    }

    # Dicționar cu cuvintele asociate grupurilor de cifre
    grupuri = {
        0: '', 1: 'mi', 2: 'milion', 3: 'miliard', 4: 'bilion',
        5: 'biliard', 6: 'trilion', 7: 'triliard', 8: 'cvadrilion',
        9: 'cvadriliard', 10: 'quintilion', 11: 'quintiliard', 12: 'dodecilion',
        13: 'dodeciliard', 14: 'tridecilion', 15: 'trideciliard', 16: 'cvadridecilion',
        17: 'cvadrideciliard', 18: 'quintadecilion', 19: 'quintadeciliard',
        20: 'sedecilion', 21: 'sedeciliard', 22: 'vindecilion', 23: 'vindeciliard',
        24: 'trivigintilion', 25: 'trivigintiliard', 26: 'cvadrivigintilion', 27: 'cvadrivigintiliard',
        28: 'quintavigintilion', 29: 'quintavigintiliard', 30: 'sedecavigintilion', 31: 'sedecavigintiliard',
        32: 'trigintilion', 33: 'trigintiliard', 34: 'cvadratrigintilion', 35: 'cvadratrigintiliard', 36: 'quintatrigintilion',
        37: 'quintatrigintiliard', 38: 'sedecatrigintilion', 39: 'sedecatrigintiliard', 40: 'quadragintilion', 41: 'quadragintiliard',
        42: 'quinquagintilion', 43: 'quinquagintiliard', 44: 'sexagintilion', 45: 'sexagintiliard',
        46: 'septuagintilion', 47: 'septuagintiliard', 48: 'octogintilion', 49: 'nonagintilion',
        50: 'nonagintiliard', 51: 'centilion', 52: 'centiliard', 53: 'ducentilion', 54: 'ducentiliard'
    }

    def converteste_mii(numar, grup_index):
        rezultat = ''
        sute = numar // 100
        zeci = (numar // 10) % 10
        unitati = numar % 10

        # Verificarea cazurilor speciale pentru unele numere
        if grup_index == 1 and numar == 1:
            return 'o'
        if grup_index == 2 and numar == 1:
            return 'un'
        if grup_index == 2 and numar == 2:
            return 'doua'
        if grup_index == 3 and numar == 2:
            return 'doua'
        if grup_index == 4 and numar == 2:
            return 'doua'

        # Adăugarea cuvintelor pentru sute, zeci și unități
        if sute > 1:
            if sute == 2:
                rezultat += 'două sute '
            else:
                rezultat += cifre[sute] + ' sute '
        elif sute == 1:
            rezultat += 'o sută '

        if zeci == 1:
            if unitati == 0:
                rezultat += 'zece'
            elif unitati == 1:
                rezultat += 'unsprezece'
            elif unitati == 2:
                rezultat += 'doisprezece'
            elif unitati == 3:
                rezultat += 'treisprezece'
            else:
                rezultat += cifre[unitati] + 'sprezece'
        else:
            if zeci == 6:
                rezultat += ' șaizeci '
            if zeci == 2:
                rezultat += 'douazeci '
            elif zeci > 1 and zeci != 6:
                rezultat += cifre[zeci] + 'zeci '
            if unitati > 0:
                if rezultat:
                    rezultat += 'și '
                rezultat += cifre[unitati]

        # Adăugarea cuvintelor pentru grupuri de cifre
        if grup_index >= 1 and (zeci >= 2 or sute >= 2):
            rezultat = rezultat + ' de '

        if grup_index % 2 == 0 and grup_index != 0 and numar != 0:
            cuvant = grupuri[grup_index]
            if cuvant.endswith('on') or cuvant.endswith('ion'):
                rezultat = rezultat+' '+cuvant[:-2] + 'oane'

        if grup_index % 2 == 1 and grup_index != 0 and numar != 0:
            cuvant = grupuri[grup_index]
            if cuvant.endswith('rd') or cuvant.endswith('rd'):
                rezultat = rezultat+' '+cuvant[:-2] + 'rde'

        return rezultat.strip()

    if not isinstance(numar, int) or numar < 0:
        return 'Eroare: Numărul trebuie să fie un întreg pozitiv.'

    if numar == 0:
        return cifre[numar]

    rezultat_final = ''
    grup_index = 0

    while numar > 0:
        grup = numar % 1000
        if grup > 0:
            rezultat = converteste_mii(grup, grup_index)
            if grup_index > 0:
                prepozitie = ' ' + grupuri[grup_index]
                if grup == 1:
                    prepozitie += 'e'
                elif grup_index >= 2:
                    prepozitie = ' '
                else:
                    prepozitie += 'i'
                rezultat = rezultat + prepozitie

            rezultat_final = rezultat + ' ' + rezultat_final

        grup_index += 1
        numar //= 1000

    return rezultat_final.strip()


# Introduce un numar
numar = 5987652149856541956419366548988525
print(numar_in_cuvinte(numar))
