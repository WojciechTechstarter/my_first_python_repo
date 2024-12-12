# Elegante Lösung

#note_11 = input("Gib Zahl 1 ein:")  # string
#note_11_int = int(note_11)
#print(f"Der Typ von Zahl1 ist: {type(note_11)}")
#print(f"Der Typ von Zahl1 ist: {type(note_11_int)}")
#note_12 = input("Gib Zahl 2 ein:")
#print(f"Der Typ von Zahl 2 ist: {type(note_12)}")
#addition_zahl11_12 = note_11 + note_12
#print(f"Das Ergebnis ist {addition_zahl11_12}")

#############################

# Frage nach das alter

person_1 = input('Wie alt bist du:')
person_2 = input('Wie alt bist du:')

# Was für ein Datentyp das ist?

print(f'Der Typ von Person_1 ist: {type(person_1)}')
print(f'Der Typ von Person_2 ist: {type(person_2)}')

# String addieren

zusammen_str = person_1 + person_2

# Print

print(f'Das alter von beiden Personen nebeneinander ist: {zusammen_str}')

# Umwandeln von Datentyp string in Datentyp int

person_1_int = int(person_1)
person_2_int = int(person_2)

# Integer addieren

zusammen_int = person_1_int + person_2_int

# Print

print(f'Das alter von beiden Personen ist: {zusammen_int}')
