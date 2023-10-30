ukuran_pizza = input("Pilih ukuran pizza : ").lower()
nambah_keju = (input("Tambah 13.000 untuk Extra Keju (ya/tidak): ")).lower() == "y"
# Harga pizza
if pesan_pizza == "frankfurter bbq":
    harga_pizza = 43000
elif pesan_pizza == "meat monsta":
    harga_pizza = 43000
elif pesan_pizza == "super supreme":
    harga_pizza = 43000
elif pesan_pizza == "super supreme chicken":
    harga_pizza = 43000
else:
    print("Jenis pizza tidak valid.")
    exit()
# Biaya topping
if crust_pizza == "pan":
    harga_crust = 0
elif crust_pizza == "stuffedcrust cheese":
    harga_crust = 12000
elif crust_pizza == "stuffedcrust sausage":
    harga_crust = 9000
