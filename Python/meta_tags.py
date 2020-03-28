import re

st = '''
    This is Pessage for example
    We are doing python right now
    Simple is better than complex
'''

r = re.findall("[A-Z][a-z]{3}", st)
#r = re.findall("[A-Z][a-z]+", st)
print(r)