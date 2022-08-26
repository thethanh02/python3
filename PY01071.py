
def python_file(s):
    s = s.lower()
    if s[-3:] != '.py':
        return 'no'
    return 'yes'

s = input()
print(python_file(s))