text=input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(text)}')
print(f'Só tem espaços? {text.isspace()}')
print(f'É um número? {text.isnumeric()}')
print(f'É alfabético? {text.isalpha()}')
print(f'É alfanumérico? {text.isalnum()}')
print(f'Está em maiúsculas? {text.isupper()}')
print(f'Está em minúsculas? {text.islower()}')
print(f'Está capitalizada? {text.istitle()}')