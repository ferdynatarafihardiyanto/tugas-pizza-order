#Nama Toko
print('=' * 30)
print('          Pizza Hut        ')
print('=' * 30)
#Daftar Menu 
print("Pizza Menu                 Harga")
print("1. Frankfurter BBQ        :43.000")
print("2. Meat Monsta            :43.000")
print("3. Super Supreme          :43.000")
print("4. Super Supreme Chicken  :43.000")
#Input 
pesan_pizza = input("Pilih jenis pizza : ").lower()
print("Crust Pizza                      Harga")
print("1. Pan                          : Free")
print("2. StuffedCrust Cheese          : 12.000")
print("3. StuffedCrust Sausage         : 9.000")
print("4. Cheesy Bites                 : 14.000")
print("5. Crown Crust                  : 12.000")
crust_pizza = input("Pilih Crust : ").lower()
print("Ukuran Pizza      Harga")
print("1. Personal      : Free")
print("2. Reguler       : 57.000")
print("3. Large         : 89.000")
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
elif crust_pizza == "cheesy bites":
    harga_crust = 14000
elif crust_pizza == "crown crust":
    harga_crust = 12000
else:
    print("Jenis Crust tidak valid.")
    exit()
# Biaya ukuran
if ukuran_pizza == "personal":
    ukuran_price = 0
elif ukuran_pizza == "reguler":
    ukuran_price = 57000
elif ukuran_pizza == "large":
    ukuran_price = 89000
else:
    print("Ukuran pizza tidak valid.")
    exit()
# Biaya tambahan keju
harga_keju = 13000 if nambah_keju else 0
# Total biaya
total_cost = harga_pizza + harga_crust + ukuran_price + harga_keju
# Menampilkan pesanan dan total biaya
print("Thank you for choosing Pizza Hut Delivery!")
print("Your final bill will be: Rp", total_cost)
  
