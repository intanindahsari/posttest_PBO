class BouquetBunga:
    total_bouquet = 0

    def __init__(self, id_bouquet, nama_bouquet, harga, stok):
        self.id_bouquet = id_bouquet      
        self.nama_bouquet = nama_bouquet   
        self.harga = harga                 
        self.stok = stok                 

        BouquetBunga.total_bouquet += 1

    @classmethod
    def dari_dict(cls, data):
        return cls(data["id_bouquet"], data["nama_bouquet"], data["harga"], data["stok"])

    def tampilkan_info(self):
        print(f"{self.id_bouquet} | {self.nama_bouquet} | Rp {self.harga} | Stok: {self.stok}")


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

    def tampilkan_info(self):
        print(f"{self.id_pelanggan} | {self.nama_pelanggan} | {self.no_telepon}")
    @staticmethod
    def validasi_Id_pelanggan(id_pelanggan):
        if id_pelanggan.startswith("P") and len(id_pelanggan) == 4:
            return True
        else:
            return False


class Transaksi:

    total_transaksi = 0

    def __init__(self, id_transaksi, tanggal, pelanggan, bouquet, jumlah):
        self.id_transaksi = id_transaksi
        self.tanggal = tanggal
        self.id_pelanggan = pelanggan.id_pelanggan
        self.nama_pelanggan = pelanggan.nama_pelanggan  
        self.id_bouquet = bouquet.id_bouquet
        self.nama_bouquet = bouquet.nama_bouquet          
        self.jumlah = jumlah
        self.total_harga = bouquet.harga * jumlah

        Transaksi.total_transaksi += 1

    def tampilkan_transaksi(self):
        print(f"{self.id_transaksi} | {self.tanggal} "
            f"| Pelanggan: {self.nama_pelanggan} | Bouquet: {self.nama_bouquet} "
            f"| Jumlah: {self.jumlah} | Total: Rp {self.total_harga}")


# =====================================================================
# PENGUJIAN PROGRAM (MAIN CODE)
# =====================================================================

b1 = BouquetBunga("BQ001", "Bouquet Mawar Merah", 150000, 10)
b2 = BouquetBunga("BQ002", "Bouquet Tulip Pink", 200000, 5)
data_lily = {"id_bouquet": "BQ003", "nama_bouquet": "Bouquet Lily Putih", "harga": 250000, "stok": 3}
b3 = BouquetBunga.dari_dict(data_lily)
b3.tampilkan_info() 

print("Daftar Bouquet")
b1.tampilkan_info()
b2.tampilkan_info()
b3.tampilkan_info()

p1 = Pelanggan("P001", "Sari", "081234567891")
p2 = Pelanggan("P002", "Budi", "081298765432")

print("\nDaftar Pelanggan")
p1.tampilkan_info()
p2.tampilkan_info()

t1 = Transaksi("T001", "20-09-2023", p1, b1, 3)
t2 = Transaksi("T002", "20-09-2023", p2, b2, 2)

print("\nDaftar Transaksi")
t1.tampilkan_transaksi()
t2.tampilkan_transaksi()

print("\nUji data tidak valid")
p1.no_telepon = "abc123"    
p1.no_telepon = "0812" 
print(f"Nomor telepon {p1.nama_pelanggan} tidak berubah, tetap = {p1.no_telepon}")

print("\nUji data tidak valid")
id_pelanggan_baru = "X123"
if Pelanggan.validasi_Id_pelanggan(id_pelanggan_baru):
    print(f"ID Pelanggan {id_pelanggan_baru} valid.")
else:
    print(f"ID Pelanggan {id_pelanggan_baru} tidak valid.")

print("\nUji data valid")
p1.no_telepon = "081211112222"
print(f"Nomor telepon {p1.nama_pelanggan} baru = {p1.no_telepon}")

print(f"\nTotal bouquet = {BouquetBunga.total_bouquet}")
print(f"Total pelanggan = {Pelanggan.total_pelanggan}")
print(f"Total transaksi = {Transaksi.total_transaksi}")
