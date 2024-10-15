nama = str(input("Masukan nama karyawan :"))
gaji= int(input("Masukan Gaji :"))
banyak_produk = int(input("Masukan Banyaknya Produk :"))
harga_satuan = int(input("Masukan Harga Satuannya :"))

omset_penjualan = banyak_produk * harga_satuan

if banyak_produk >= 100:
    bonus = 0.2 * omset_penjualan
else:
    banyak_produk < 100
    bonus = 0.1 * omset_penjualan

total_gaji = gaji + bonus
print(f"Total Omset Penjualan :" , omset_penjualan)
print(f"Total Gaji Salesman :", total_gaji)
