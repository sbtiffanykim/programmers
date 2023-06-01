str = input()
converted_string = [c.upper() if c.islower() else c.lower() for c in str]
print(''.join(converted_string))