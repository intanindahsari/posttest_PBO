# Posttest PBO - Toko Bouquet Bunga

Program ini adalah simulasi sederhana toko bunga yang menerapkan konsep **Relasi UML** (asosiasi, agregasi, komposisi) dan **Inheritance** (pewarisan) di Python.

## Kelas yang dipilih

Program ini punya 7 class:

1. **BouquetBunga** (superclass / class induk)

   atributnya ada:
   - `id_bouquet` identitas unik untuk setiap buket (publik)
   - `nama_bouquet` nama dari produk buket (publik)
   - `_harga` harga jual dasar per buket, atribut protected (ditandai `_` di awal) supaya bisa dipakai langsung oleh subclass
   - `_stok` ketersediaan stok buket, atribut protected juga
   - `__harga_modal` modal pembuatan buket, atribut private (ditandai `__` di awal) karena ini data rahasia yang cuma boleh dipakai di dalam class ini
   - `total_bouquet` atribut kelas yang dimiliki bersama oleh seluruh objek BouquetBunga (termasuk subclass-nya), berfungsi untuk mencatat berapa total buket yang telah dibuat

   metodenya ada:
   - `harga` dan `stok` (property) cara untuk membaca `_harga` dan `_stok` dari luar class
   - `dari_dict()` (class method) cara alternatif membuat objek langsung dari kamus data (berguna kalau data datang dari file/database)
   - `hitung_harga()` (instance method) mengembalikan harga jual buket, nanti di-override oleh subclass
   - `kurangi_stok()` (instance method) mengurangi stok saat ada pembelian, ditolak kalau jumlah <= 0 atau lebih besar dari stok yang ada, hasilnya `True` kalau berhasil dan `False` kalau gagal
   - `hitung_keuntungan()` (instance method) menghitung untung = harga jual dikurangi `__harga_modal`
   - `tampilkan_info()` (instance method) menampilkan detail satu buket

2. **BouquetPremium** (subclass dari BouquetBunga)

   atribut tambahan yang cuma dimiliki class ini:
   - `jenis_kemasan` jenis kemasan buket, contohnya "Box Beludru" (publik)
   - `biaya_kemasan` biaya tambahan untuk kemasan (publik)

   metodenya ada:
   - `__init__()` memanggil `super().__init__()` supaya atribut milik induk ikut terisi
   - `hitung_harga()` (override) harga jadi `_harga + biaya_kemasan`
   - `tampilkan_info()` (override) menjalankan versi induk dulu lewat `super()`, lalu menambah baris info kemasan
   - `coba_akses_modal()` method khusus untuk demo, sengaja mencoba mengambil `__harga_modal` milik induk (hasilnya error, karena private tidak bisa dipakai subclass)

3. **BouquetCustom** (subclass dari BouquetBunga)

   atribut tambahan yang cuma dimiliki class ini:
   - `BIAYA_CUSTOM` atribut kelas, biaya custom tetap sebesar Rp 20.000
   - `pesan_kartu` isi kartu ucapan yang ditulis pembeli (publik)

   metodenya ada:
   - `__init__()` memanggil `super().__init__()`
   - `hitung_harga()` (override) harga jadi `_harga + BIAYA_CUSTOM`
   - `tampilkan_info()` (override) versi induk ditambah baris pesan kartu

4. **Pelanggan**

   atributnya ada:
   - `id_pelanggan` kode identifikasi pelanggan (publik)
   - `nama_pelanggan` nama pelanggan (publik)
   - `__no_telepon` nomor pelanggan, merupakan atribut private
   - `total_pelanggan` atribut kelas yang menghitung jumlah pelanggan yang terdaftar

   metodenya ada:
   - `no_telepon` (property + setter) untuk baca dan ubah nomor telepon, setter menolak nomor yang bukan angka atau kurang dari 12 digit
   - `beli_bouquet()` (instance method) pelanggan membeli bouquet, objek bouquet diterima lewat parameter lalu dipakai untuk mengurangi stok (ini contoh **asosiasi**)
   - `tampilkan_info()` (instance method) menampilkan detail pelanggan
   - `validasi_Id_pelanggan()` (static method) cuma fungsi bantuan untuk cek format ID (harus diawali huruf "P" dan panjang 4 karakter), tidak butuh data dari objek manapun

5. **DetailTransaksi**

   atributnya ada:
   - `id_bouquet`, `nama_bouquet` diambil dari objek bouquet yang dibeli
   - `jumlah` kuantitas buket yang dibeli
   - `subtotal` dihitung otomatis dari `hitung_harga()` buket × jumlah

   class ini tidak dibuat sendiri di program utama, tapi dibuat otomatis di dalam class Transaksi.

6. **Transaksi**

   atributnya ada:
   - `id_transaksi` kode unik untuk setiap transaksi (publik)
   - `tanggal` waktu transaksi dilaksanakan (publik)
   - `id_pelanggan`, `nama_pelanggan` diambil secara otomatis dari objek Pelanggan yang digunakan saat transaksi
   - `detail` objek DetailTransaksi yang dibuat langsung di dalam `__init__` (ini contoh **komposisi**)
   - `total_harga` diambil dari `detail.subtotal`
   - `total_transaksi` atribut kelas yang mencatat jumlah total transaksi yang telah terjadi

   metodenya ada:
   - `tampilkan_transaksi()` (instance method) menampilkan ringkasan transaksi lengkap

7. **TokoBunga**

   atributnya ada:
   - `nama_toko` nama toko (publik)
   - `_daftar_bouquet` list penampung bouquet
   - `_daftar_pelanggan` list penampung pelanggan

   metodenya ada:
   - `tambah_bouquet()` dan `tambah_pelanggan()` memasukkan objek yang sudah dibuat di luar ke dalam toko (ini contoh **agregasi**)
   - `tampilkan_katalog()` menampilkan semua bouquet di toko
   - `tampilkan_pelanggan()` menampilkan semua pelanggan di toko

## Relasi UML

1. **Asosiasi** ("menggunakan")
   - `Pelanggan.beli_bouquet(bouquet, jumlah)` objek bouquet cuma diterima lewat parameter, dipakai sebentar, tidak disimpan sebagai atribut
   - `Transaksi` juga menerima objek `pelanggan` dan `bouquet` lewat parameter, lalu hanya mengambil datanya

2. **Agregasi** ("memiliki")
   - `TokoBunga` menampung bouquet dan pelanggan yang dibuat di luar toko, disimpan di dalam list
   - buktinya: setelah `del toko`, objek bouquet (misalnya `b1`) tetap ada dan masih bisa ditampilkan

3. **Komposisi** ("terdiri dari")
   - `Transaksi` membuat `DetailTransaksi` langsung di dalam `__init__`-nya sendiri
   - `DetailTransaksi` tidak punya arti kalau tidak ada transaksinya

## Inheritance

1. Superclass: `BouquetBunga`, subclass: `BouquetPremium` dan `BouquetCustom` (satu induk punya dua anak)
2. Kedua subclass memanggil konstruktor induk lewat `super().__init__(...)`
3. Atribut unik: `BouquetPremium` punya `jenis_kemasan` dan `biaya_kemasan`, `BouquetCustom` punya `pesan_kartu`
4. Method overriding: `hitung_harga()` dan `tampilkan_info()` ditulis ulang di kedua subclass dengan perilaku yang berbeda
5. Tingkat akses:
   - `_harga` dan `_stok` (protected) dipakai langsung oleh subclass, contohnya di `hitung_harga()` dan `tampilkan_info()`
   - `__harga_modal` (private) cuma bisa dipakai di dalam `BouquetBunga` lewat `hitung_keuntungan()`, kalau subclass mencoba mengambilnya langsung akan muncul `AttributeError`

## Program Pengujian (kode utama)

1. Membuat & menampilkan data buket
   - `b1` dibuat langsung melalui `__init__` (BouquetBunga biasa, Mawar Merah)
   - `b2` dibuat dari `BouquetPremium` (Tulip Pink, kemasan Box Beludru)
   - `b3` dibuat lewat `dari_dict()` (metode kelas), dari kamus data Lily Putih
   - `b4` dibuat dari `BouquetCustom` (Matahari, kartu "Selamat Ulang Tahun James!")
   - Semuanya dimasukkan ke `TokoBunga` lalu ditampilkan lewat `tampilkan_katalog()`
   - Harga Tulip Pink tampil Rp 250.000 (200.000 + kemasan 50.000), harga Matahari tampil Rp 140.000 (120.000 + biaya custom 20.000)

2. Membuat & menampilkan data pelanggan
   - `p1` = Ella, 081234567891
   - `p2` = Juhoon, 081298765432

3. Proses pembelian & membuat transaksi
   - `t1` = Ella beli 3 Bouquet Mawar Merah total Rp 450.000
   - `t2` = Juhoon beli 2 Bouquet Tulip Pink total Rp 500.000
   - `t3` = Ella beli 1 Bouquet Matahari total Rp 140.000
   - Juhoon mencoba beli 5 Bouquet Lily Putih, padahal stoknya cuma 3, jadi muncul pesan "Stok Bouquet Lily Putih tidak cukup (sisa 3)." dan transaksinya tidak dibuat

4. Uji inheritance (overriding & polymorphism)
   - BouquetBunga: harga jual Rp 150.000, untung Rp 60.000
   - BouquetPremium: harga jual Rp 250.000, untung Rp 130.000
   - BouquetCustom: harga jual Rp 140.000, untung Rp 70.000
   - Method yang dipanggil sama (`hitung_harga()` dan `hitung_keuntungan()`), tapi hasilnya beda tergantung jenis buketnya

5. Cek relasi pewarisan
   - `isinstance(b2, BouquetBunga)` hasilnya `True`, karena Premium adalah jenis Bouquet
   - `isinstance(b2, BouquetCustom)` hasilnya `False`
   - `issubclass(BouquetCustom, BouquetBunga)` hasilnya `True`

6. Menguji atribut private dari class anak
   - `b2.coba_akses_modal()` dipanggil di dalam `try-except`
   - Hasilnya muncul pesan error: `'BouquetPremium' object has no attribute '_BouquetPremium__harga_modal'`, artinya `__harga_modal` memang tidak bisa diakses subclass

7. Menguji setter dengan data yang tidak valid
   - `p1.no_telepon = "abc123"` (bukan angka jadi ditolak)
   - `p1.no_telepon = "0812"` (kurang dari 12 digit jadi ditolak)

   Hasilnya akan muncul pesan "Nomor telepon tidak valid (harus angka, minimal 12 digit)." dan nomor lama tetap dipakai (tidak berubah).

8. Menguji metode statis
   - `Pelanggan.validasi_Id_pelanggan("X123")`
   - Hasilnya jadi: `False`, karena ID tidak diawali huruf "P", dicetak "ID Pelanggan X123 tidak valid."

9. Menguji setter dengan data yang valid
   - `p1.no_telepon = "081211112222"`
   - Hasilnya: berhasil, nomor telepon Ella berubah jadi `081211112222`.

10. Bukti agregasi
    - `del toko` menghapus objek toko
    - `b1.tampilkan_info()` tetap bisa menampilkan Bouquet Mawar Merah (stok 7), artinya bouquet tidak ikut hilang

11. Menampilkan atribut kelas
    - `BouquetBunga.total_bouquet` # 4
    - `Pelanggan.total_pelanggan` # 2
    - `Transaksi.total_transaksi` # 3

## Cara menjalankan

Simpan kodenya dalam satu file Python, lalu jalankan lewat terminal:

```
python nama_file.py
```