# String initialization examples
s = ''
s = ""
s = ''' '''
s = "' '"

# String concatenation
name = 'Ajay'
name1 = "Krishna"
print(name + name1)          # AjayKrishna
print(name + ' ' + name1)    # Ajay Krishna

# Repetition and multiplication
print(name * 10)
print('*' * 100)
print('-' * 10)

# Indexing
name = 'Ajay Kumar'
print(name[3])     # y
print(name[-2])    # a
print(name[-5])    # K
print(name[1])     # j

# String slicing
names = 'AjayKrishnaSatishNishithaPreethiRuchitha'
print(names[0:4])     # Ajay
print(names[:4])      # Ajay
print(names[4:11])    # Krishna
print(names[11:17])   # Satish
print(names[17:25])   # Nishitha
print(names[25:32])   # Preethi
print(names[32:40])   # Ruchitha
print(names[32:])     # Ruchitha
print(names[0:4:2])   # Aa
print(names[::3])     # Ayinasiiaehuia
print(names[-8:])     # Ruchitha

# Reverse slicing
print(names[::-1])    # reversed string
print(names[4::-1])   # KyajA
print(names[3::-1])   # yajA
print(names[10:4:-1]) # anhsir
print(names[10:3:-1]) # anhsirK
print(names[16:10:-1]) # hsitaS
print(names[24:16:-1]) # ahtihsiN
print(names[31:24:-1]) # ihteerP
print(names[39:31:-1]) # ahtihcuR

# Membership
print('Ajay' in names)      # True
print('nithin' in names)    # False
print('priya' in names)     # False
print('sahithi' not in names) # True

# Case methods
print(names.upper())
print(names.lower())
print(names.swapcase())

# More string methods
l = 'python programming language'
print(l.capitalize())
print(l.title())
print("ß".casefold())

# Center, ljust, rjust, zfill
print(l.center(100, '*'))
print(l.center(50, '*'))
print(l.center(50, '-'))
print(l.center(50, '_'))
print(l.ljust(50, '-'))
print(l.ljust(50, ' ') + ':')
print(l.rjust(50, '-'))
print('2'.zfill(6))
print('202'.zfill(6))
print('202123'.zfill(6))

# Find, index, count
print(names.find('j'))
print(names.find('a'))
print(names.find('Ajay'))
print(names.find('z'))
print(names.rfind('a'))
print(names.index('K'))
print(names.index('a'))
print(names.rindex('a'))
print(names.count('a'))
print(names.count('e'))
print(names.count('i'))

# Replace examples
print(names.replace('a', '*'))
print(names.replace('sh', ''))
print(names.replace('sh', '00'))
print(names.replace('sh', '-00-'))
print(names.replace('Ajay', 'Anirudh'))

# maketrans and translate
trans_table = names.maketrans('aeiou', '*****')
print(names.translate(trans_table))

trans_table2 = str.maketrans('AEIOUaeiou', '1234500000')
print(names.translate(trans_table2))
