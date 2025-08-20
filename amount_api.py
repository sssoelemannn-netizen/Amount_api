from flask import Flask, request, jsonify

app = Flask(__name__)

def terbilang(n):
    angka = ["", "satu", "dua", "tiga", "empat", "lima",
             "enam", "tujuh", "delapan", "sembilan", "sepuluh", "sebelas"]
    n = int(n)

    if n == 0:
        return ""
    elif n < 12:
        return angka[n]
    elif n < 20:
        return terbilang(n - 10) + " belas"
    elif n < 100:
        return terbilang(n // 10) + " puluh" + (" " + terbilang(n % 10) if n % 10 != 0 else "")
    elif n < 200:
        return "seratus" + (" " + terbilang(n - 100) if n - 100 != 0 else "")
    elif n < 1000:
        return terbilang(n // 100) + " ratus" + (" " + terbilang(n % 100) if n % 100 != 0 else "")
    elif n < 2000:
        return "seribu" + (" " + terbilang(n - 1000) if n - 1000 != 0 else "")
    elif n < 1_000_000:
        return terbilang(n // 1000) + " ribu" + (" " + terbilang(n % 1000) if n % 1000 != 0 else "")
    elif n < 1_000_000_000:
        return terbilang(n // 1_000_000) + " juta" + (" " + terbilang(n % 1_000_000) if n % 1_000_000 != 0 else "")
    elif n < 1_000_000_000_000:
        return terbilang(n // 1_000_000_000) + " miliar" + (" " + terbilang(n % 1_000_000_000) if n % 1_000_000_000 != 0 else "")
    elif n < 1_000_000_000_000_000:
        return terbilang(n // 1_000_000_000_000) + " triliun" + (" " + terbilang(n % 1_000_000_000_000) if n % 1_000_000_000_000 != 0 else "")
    else:
        return "Angka terlalu besar"

@app.route('/terbilang', methods=['GET'])
def convert():
    angka = request.args.get('angka', default='0', type=int)
    hasil = terbilang(angka).strip()
    hasil = " ".join(hasil.split())  # hapus spasi ganda
    return jsonify({
        'angka': angka,
        'terbilang': hasil + " rupiah"
    })

if __name__ == '__main__':
    app.run(port=5000)
