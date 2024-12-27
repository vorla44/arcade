# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# Explanation video: http://youtu.be/sxFIxD8Gd3A
# salaus.py

plain_text = "This is a test. ABC abc"

print(f"Alkuperäinen teksti: {plain_text}")

encrypted_text = ""
for c in plain_text:
    x = ord(c)  # muunna kirjain numeroksi ASCII taulukon mukaisesti
    x = x + 1
    c2 = chr(x)  # muunna numero kirjaimeksi
    encrypted_text = encrypted_text + c2 #merkkijonoja voidaan yhdistellä
print(f"Muutetaan salatuksi tekstiksi: {encrypted_text}")

# Muutetaan teksti takaisin alkuperäiseksi

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(f"Salattu teksti muutetaan alkuperäiseksi tekstiksi: {plain_text}")

