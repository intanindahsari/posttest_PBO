class BouquetBunga:
    total_bouquet = 0
    def __init__(self, id_bouquet, nama_bouquet, harga, stok, harga_modal):
        self.id_bouquet = id_bouquet
        self.nama_bouquet = nama_bouquet
        self._harga = harga
        self._stok = stok
        self.__harga_modal = harga_modal

        BouquetBunga.total_bouquet += 1

    @classmethod
    def dari_dict(cls, data):
        return cls(data["id_bouquet"], data["nama_bouquet"],
                    data["harga"], data["stok"], data["harga_modal"])

    @property
    def harga(self):
        return self._harga

    @property
    def stok(self):
        return self._stok

    def hitung_harga(self):
        return self._harga

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            print(f"{self.nama_bouquet} - Jumlah pembelian tidak valid.")
            return False
        if jumlah > self._stok:
            print(f"  Stok {self.nama_bouquet} tidak cukup (sisa {self._stok}).")
            return False
        self._stok -= jumlah
        return True

    def hitung_keuntungan(self):
        return self.hitung_harga() - self.__harga_modal

    def tampilkan_info(self):
        print(f"{self.id_bouquet} | {self.nama_bouquet} | "
                f"Rp {self.hitung_harga()} | Stok: {self._stok}")

class BouquetPremium(BouquetBunga):
    def __init__(self, id_bouquet, nama_bouquet, harga, stok, harga_modal,
                jenis_kemasan, biaya_kemasan):
        super().__init__(id_bouquet, nama_bouquet, harga, stok, harga_modal)
        self.jenis_kemasan = jenis_kemasan
        self.biaya_kemasan = biaya_kemasan

    def hitung_harga(self):
        return self._harga + self.biaya_kemasan

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"======================================================")
        print(f"[PREMIUM] Kemasan: {self.jenis_kemasan} "
            f"(+Rp {self.biaya_kemasan})")
        print(f"======================================================")

    def coba_akses_modal(self):

        return self.__harga_modal

class BouquetCustom(BouquetBunga):
    BIAYA_CUSTOM = 20000

    def __init__(self, id_bouquet, nama_bouquet, harga, stok, harga_modal, pesan_kartu):
        super().__init__(id_bouquet, nama_bouquet, harga, stok, harga_modal)
        self.pesan_kartu = pesan_kartu

    def hitung_harga(self):
        return self._harga + BouquetCustom.BIAYA_CUSTOM

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"======================================================")
        print(f"[CUSTOM] Pesan kartu: \"{self.pesan_kartu}\"")
        print(f"======================================================")

class Pelanggan:
    total_pelanggan = 0

    def __init__(self, id_pelanggan, nama_pelanggan, no_telepon):
        self.id_pelanggan = id_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.__no_telepon = no_telepon

        Pelanggan.total_pelanggan += 1

    @property
    def no_telepon(self):
        return self.__no_telepon

    @no_telepon.setter
    def no_telepon(self, no_baru):
        if no_baru.isdigit() and len(no_baru) >= 12:
            self.__no_telepon = no_baru
        else:
            print("Nomor telepon tidak valid (harus angka, minimal 12 digit).")

    def beli_bouquet(self, bouquet, jumlah):
        print(f"{self.nama_pelanggan} memesan {jumlah} x {bouquet.nama_bouquet}")
        return bouquet.kurangi_stok(jumlah)

    def tampilkan_info(self):
        print(f"{self.id_pelanggan} | {self.nama_pelanggan} | {self.no_telepon}")

    @staticmethod
    def validasi_Id_pelanggan(id_pelanggan):
        if id_pelanggan.startswith("P") and len(id_pelanggan) == 4:
            return True
        else:
            return False

class DetailTransaksi:
    def __init__(self, bouquet, jumlah):
        self.id_bouquet = bouquet.id_bouquet
        self.nama_bouquet = bouquet.nama_bouquet
        self.jumlah = jumlah
        self.subtotal = bouquet.hitung_harga() * jumlah

class Transaksi:
    total_transaksi = 0

    def __init__(self, id_transaksi, tanggal, pelanggan, bouquet, jumlah):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.id_pelanggan = pelanggan.id_pelanggan
        self.nama_pelanggan = pelanggan.nama_pelanggan
        self.detail = DetailTransaksi(bouquet, jumlah)
        self.total_harga = self.detail.subtotal

        Transaksi.total_transaksi += 1

    def tampilkan_transaksi(self):
        print(f"{self.id_transaksi} | {self.tanggal} "
            f"   | Pelanggan: {self.nama_pelanggan} "
            f"   | Bouquet: {self.detail.nama_bouquet} "
            f"   | Jumlah: {self.detail.jumlah} "        
            f"   | Total: Rp {self.total_harga}")

class TokoBunga:
    def __init__(self, nama_toko):
        self.nama_toko = nama_toko
        self._daftar_bouquet = []
        self._daftar_pelanggan = []

    def tambah_bouquet(self, bouquet):
        self._daftar_bouquet.append(bouquet)

    def tambah_pelanggan(self, pelanggan):
        self._daftar_pelanggan.append(pelanggan)

    def tampilkan_katalog(self):
        for b in self._daftar_bouquet:
            b.tampilkan_info()

    def tampilkan_pelanggan(self):
        for p in self._daftar_pelanggan:
            p.tampilkan_info()


# =====================================================================
# PENGUJIAN PROGRAM (MAIN CODE)
# =====================================================================

b1 = BouquetBunga("BQ001", "Bouquet Mawar Merah", 150000, 10, 90000)
b2 = BouquetPremium("BQ002", "Bouquet Tulip Pink ", 200000, 5, 120000, "Box Beludru", 50000)
data_lily = {"id_bouquet": "BQ003", "nama_bouquet": "Bouquet Lily Putih",
            "harga": 250000, "stok": 3, "harga_modal": 150000}
b3 = BouquetBunga.dari_dict(data_lily)
b4 = BouquetCustom("BQ004", "Bouquet Matahari   ", 120000, 8, 70000, "Selamat Ulang Tahun James!")

p1 = Pelanggan("P001", "Ella  ", "081234567891") 
p2 = Pelanggan("P002", "Juhoon", "081298765432")

toko = TokoBunga("Florist Samarinda")
for b in (b1, b2, b3, b4):
    toko.tambah_bouquet(b)
toko.tambah_pelanggan(p1)
toko.tambah_pelanggan(p2)

print("\n+--------------------------------------------------------------------+")
print("|                           DAFTAR BOUQUET                           |")
print("+--------------------------------------------------------------------+")
toko.tampilkan_katalog()

print("\n+--------------------------------------------------------------------+")
print("|                          DAFTAR PELANGGAN                          |")
print("+--------------------------------------------------------------------+")
toko.tampilkan_pelanggan()

print("\n+--------------------------------------------------------------------+")
print("|                          PROSES PEMBELIAN                          |")
print("+--------------------------------------------------------------------+")
if p1.beli_bouquet(b1, 3):
    t1 = Transaksi("T001", "20-09-2023", p1, b1, 3)
if p2.beli_bouquet(b2, 2):
    t2 = Transaksi("T002", "20-09-2023", p2, b2, 2)
if p1.beli_bouquet(b4, 1):
    t3 = Transaksi("T003", "21-09-2023", p1, b4, 1)
p2.beli_bouquet(b3, 5)

print("\n+-----------------------------------------------------------------------------------------------------------------+")
print("|                                                   DAFTAR TRANSAKSI                                               |")
print("+-----------------------------------------------------------------------------------------------------------------+")
t1.tampilkan_transaksi()
t2.tampilkan_transaksi()
t3.tampilkan_transaksi()

print("\n+--------------------------------------------------------------------+")
print("|            UJI INHERITANCE (OVERRIDING & POLYMORPHISM)             |")
print("+--------------------------------------------------------------------+")
for b in (b1, b2, b4):
    print(f"{type(b).__name__:<15} | harga jual Rp {b.hitung_harga()} "
            f"| untung Rp {b.hitung_keuntungan()}")

print("\n+--------------------------------------------------------------------+")
print("|                        CEK RELASI PEWARISAN                        |")
print("+--------------------------------------------------------------------+")
print(isinstance(b2, BouquetBunga))
print(isinstance(b2, BouquetCustom))
print(issubclass(BouquetCustom, BouquetBunga))

print("\n+--------------------------------------------------------------------------+")
print("|               UJI ATRIBUT PRIVATE TIDAK BISA DIAKSES CLASS ANAK          |")
print("+--------------------------------------------------------------------------+")
try:
    b2.coba_akses_modal()
except AttributeError as e:
    print("Error:", e)

print("\n+--------------------------------------------------------------------+")
print("|                UJI DATA TIDAK VALID: NOMOR TELEPON                 |")
print("+--------------------------------------------------------------------+")
p1.no_telepon = "abc123"
p1.no_telepon = "0812"
print(f"Nomor telepon {p1.nama_pelanggan} tidak berubah, tetap = {p1.no_telepon}")

print("\n+--------------------------------------------------------------------+")
print("|                 UJI DATA TIDAK VALID: ID PELANGGAN                 |")
print("+--------------------------------------------------------------------+")
id_pelanggan_baru = "X123"
if Pelanggan.validasi_Id_pelanggan(id_pelanggan_baru):
    print(f"ID Pelanggan {id_pelanggan_baru} valid.")
else:
    print(f"ID Pelanggan {id_pelanggan_baru} tidak valid.")

print("\n+--------------------------------------------------------------------+")
print("|                           UJI DATA VALID                           |")
print("+--------------------------------------------------------------------+")
p1.no_telepon = "081211112222"
print(f"Nomor telepon {p1.nama_pelanggan} baru = {p1.no_telepon}")

print("\n+--------------------------------------------------------------------+")
print("|          BUKTI AGREGASI: TOKO DIHAPUS, BOUQUET TETAP ADA           |")
print("+--------------------------------------------------------------------+")
del toko
b1.tampilkan_info()

print("\n+--------------------------------------------------------------------+")
print("|                        RINGKASAN TOTAL DATA                        |")
print("+--------------------------------------------------------------------+")
print(f"Total bouquet = {BouquetBunga.total_bouquet}")
print(f"Total pelanggan = {Pelanggan.total_pelanggan}")
print(f"Total transaksi = {Transaksi.total_transaksi}")