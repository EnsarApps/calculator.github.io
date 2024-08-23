def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme hatası: Sıfıra bölme hatası"

def hesap_makinesi():
    print("Calculator v0.1 Alpha Turkish")
    print("Yapmak istediğiniz işlemi seçin:")
    print("1: Toplama")
    print("2: Çıkarma")
    print("3: Çarpma")
    print("4: Bölme")
    
    secim = input("Seçiminizi yapın (1/2/3/4): ")

    if secim not in ['1', '2', '3', '4']:
        print("Geçersiz seçim")
        return

    try:
        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))
    except ValueError:
        print("Geçersiz sayı")
        return

    if secim == '1':
        print(f"Sonuç: {toplama(num1, num2)}")
    elif secim == '2':
        print(f"Sonuç: {cikarma(num1, num2)}")
    elif secim == '3':
        print(f"Sonuç: {carpma(num1, num2)}")
    elif secim == '4':
        print(f"Sonuç: {bolme(num1, num2)}")

if __name__ == "__main__":
    while True:
        hesap_makinesi()
        devam = input("Başka bir işlem yapmak ister misiniz? (e/h): ")
        if devam.lower() != 'e':
            break
