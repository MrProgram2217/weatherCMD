import time

russian = ['о', 'а', 'е', 'и', 'т', 'н', 'р', 'ж', 'з', 'г', 'й', 'к', 'л', 'м', 'в', 'б', 'п', 'ё', 'с', 'д', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'я', 'ы', 'ь', 'э', 'ю', 'ъ', ' ', '\n', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '!', '?']
crypt   = ['Ё', '#', '4', '/', '}', '2', '№', 'y', '|', '*', '(', '@', 'h', '&', '=', '+', '%', '-', '_', 'Д', '1', ':', ']', '{', '~', 'т', '<', '$', ';', 'Ж', 'Џ', '0', '6', 'v', '\n', 'Ђ', 'Ў', '"', '>', 'µ', 'Є', 'ћ', '^', 'Ї', 'Ѕ', 'Э', '`', 'Ъ', 'Ц']

decrypted_text = ''
e = str(input('введите название файла:  '))
fileName = e + '.txt'

start_time = time.time()

print('decryption start...')
f = open(fileName, 'r')           # открытие файла и его длина
lenText = len(f.read()) + 1
f.seek(0)
'''textInpt = f.read()
f.seek(0)'''
print('название файла: ',fileName)

for i in range (1, lenText):        # замена элементов
    enc = f.read(1)
    try:
        encIndex = crypt.index(enc)
        rus = russian[encIndex]
    except:
        rus = enc
    decrypted_text += rus

f2 = open('decrypted_gen.txt', 'w')
f2.write(decrypted_text)

print('successfully decrypded')
print("--- %s seconds ---" % (time.time() - start_time))
input('tap for exit')
