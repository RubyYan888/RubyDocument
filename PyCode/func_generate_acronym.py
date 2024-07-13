# func_generate_acronym.py
def func_generate_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())

print(func_generate_acronym("As Soon As Possible"))
