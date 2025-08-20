def terbilang(n):
    angka = ["", "satu", "dua", "tiga", "empat", "lima",
             "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"]
    n = int(n)
    hasil = ""
 
    if n < 12:
        hasil = angka[n]
    elif n < 20:
        hasil = terbilang(n - 10) + " belas"
    elif n < 100:
        hasil = terbilang(n // 10) + " puluh " + terbilang(n % 10)
    elif n < 200:
        hasil = "seratus " + terbilang(n - 100)
    elif n < 1000:
        hasil = terbilang(n // 100) + " ratus " + terbilang(n % 100)
    elif n < 2000:
        hasil = "seribu " + terbilang(n - 1000)
    elif n < 1_000_000:
        hasil = terbilang(n // 1000) + " ribu " + terbilang(n % 1000)
    elif n < 1_000_000_000:
        hasil = terbilang(n // 1_000_000) + " juta " + terbilang(n % 1_000_000)
    elif n < 1_000_000_000_000:
        hasil = terbilang(n // 1_000_000_000) + " miliar " + terbilang(n % 1_000_000_000)
    else:
        hasil = "Angka terlalu besar"
 
    return hasil.strip()
 
 
def main():
    while True:
        try:
            angka_input = int(input("Masukkan angka: "))
            break
        except ValueError:
            print("Input tidak valid! Masukkan hanya angka tanpa huruf atau karakter lain.")
 
    hasil = terbilang(angka_input)
    print(f"{angka_input} = {hasil} rupiah")
 
 
if __name__ == "__main__":
    main()