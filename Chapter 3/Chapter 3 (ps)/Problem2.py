'''Write a program to fill in a lalter template givon below with name and date.
'''

letter = '''Dear <|NAME|>
You are selected!
<|DATE|>'''

print(letter.replace("<|NAME|>", "Hiren").replace("<|DATE|>", "1st Jan"))

