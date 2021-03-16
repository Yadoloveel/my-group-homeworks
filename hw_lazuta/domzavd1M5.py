import string
'''
Реализуйте шифратор и дешифратор по шифру Цезаря.
Спросить пользователя, что он хочет сделать-зашифровать или расшифровать файл.
Если зашифровать, попросить у него ввести имя шифруемого файла, 
имя файла, который мы получим на выходе(зашифрованного) и 
ключ(ключем будет уроваень сдвига). Если расшифровать, попросить ввести 
имя зашифрованного файла, имя файла на выходе(расшифрованного) и ключ.
'''

alpha = f"{string.ascii_letters}{string.digits}{string.punctuation} \n"
ask_crypt = input('Обери дію! Напиши crypt або encrypt, щоб вийти (e): ')


def func_vubor(vubor):
    """Функція перевірки вводу даних від користувача та передачі параметрів для
     функцій шифрування або дешифрування"""
    vubor = vubor.lower()
    if vubor == '' or vubor == 'e':
        print('Потрібно обрати crypt або encrypt! Спробуйте знову.')
    else:
        while True:
            vvod_free = input('Введите имя_файла для шифрування: ')
            if func_vvodusfl(vvod_free):
                break
            else:
                continue
        vvod_cr = input('Введите имя_зашифрованого файлу: ')
        while True:
            kcrypt = input("Визначте ключ(число): ")
            if func_vvodkey(kcrypt):
                break
            else:
                continue
        if vubor == 'crypt':
            func_crypt(vvod_free, vvod_cr, kcrypt)
        elif vubor == 'encrypt':
            func_encrypt(vvod_free, vvod_cr, kcrypt)


def func_vvodusfl(name):
    """Функція перевірки наявності файлів"""
    try:
        with open(f"{name}.txt") as f:
            return True
    except FileNotFoundError:
        print(f"Введений файл не існує, будьте уважні")
        return False


def func_vvodkey(crkey):
    """Функція перевірки введення числа, як ключа для шифрування"""
    try:
        crkey = int(crkey)
        return True
    except ValueError:
        print("Ви ввели не число! Спробуйте знову.")
        return False


def func_crypt(nfstart, nfend, keycr):
    """Функція приймає файли та ключ та робить шифрування"""
    with open(f"{nfstart}.txt") as ffree, open(f"{nfend}.txt", 'w') as fcr:
        ftext = ffree.read()
        rescr = ''
        for c in ftext:
            rescr += alpha[(alpha.index(c) + int(keycr)) % len(alpha)]
        fcr.writelines(f"{rescr}")
        print(f"Вміст файла {nfstart} -- зашифровано у файл {nfend})")


def func_encrypt(nfstart, nfend, keycr):
    """Функція приймає файли та ключ та робить дешифрування"""
    with open(f"{nfstart}.txt") as ffree, open(f"{nfend}.txt", 'w') as fcr:
        ftext = ffree.read()
        rescr = ''
        for c in ftext:
            rescr += alpha[(alpha.index(c) - int(keycr)) % len(alpha)]
        fcr.writelines(f"{rescr}")
        print(f"Вміст файла {nfstart} -- розшифровано у файл {nfend})")


func_vubor(ask_crypt)

