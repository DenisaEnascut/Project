# Dat textul "admitere Facultate Automatica si Calculatoare 2023", realizati un program care proceseaza un text si obtine un numar dupa urmatorul algoritm(pasii se vor executa in serie/cascada):
# 1. literele mari se convertesc la llitere mici
# 2. orice caracter in afara de litera mica,cifra si spatiu este ignorat
# 3. sorteaza descrescator caracterele unice din sirul de mai sus in functie de frecventa in sirul dat . Daca sunt mai multe caractere va avea asociat un numar. Numarul reprezinta indexul in sortarea de mai sus.
# Ex. caracterul 'e' apare cel mai des, de 5 ori, ia valoarea 0, caracterul 't' apare de 4 ori ia valoarea 1 caracterul ' ','2','i','n' apar de 3 ori.Vor primi valorile:2,3,4 si respectiv 5

# Rezultatul final se obtine adunand pentru fiecare pozitie texul original, pozitia respectiva plus valoarea asociata caracterului aflat pe acea positie in urma procesarii de mai sus.Pe exemplul de mai sus avem
# ex: pentru t:suma +=0+1
# ex: pentru e: suma +=1+0


def process_text(text):
    # Pasul 1: Conversia literelor mari în litere mici
    text = text.lower()

    # Pasul 2: Eliminarea caracterelor nepermise
    allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789 ')
    filtered_text = ''.join(c for c in text if c in allowed_chars)

    # Pasul 3: Obținerea frecvențelor caracterelor unice și sortarea descrescătoare
    char_freq = {}
    for char in filtered_text:
        char_freq[char] = char_freq.get(char, 0) + 1
    sorted_chars = sorted(
        char_freq.keys(), key=lambda x: char_freq[x], reverse=True)

    # Calcularea sumei finale
    total_sum = 0
    for i, char in enumerate(text):
        if char in sorted_chars:
            char_index = sorted_chars.index(char)
            total_sum += i + char_index

    return total_sum


# Exemplu de utilizare
text = "admitere Facultate Automatica si Calculatoare 2023"
result = process_text(text)
print(result)
