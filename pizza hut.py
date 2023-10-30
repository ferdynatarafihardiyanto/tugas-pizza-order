#nama toko
print("      PIZZA HUT DELIVERY      ")
print("==============================")
#daftar menu
print("Daftar Menu               Harga")
print("frankfurter BBQ      = Rp 43.000")
print("meat monsta          = Rp 43.000")
print("super supreme        = Rp 43.000")
print("super supreme chiken = Rp 43.000")
menu_pizza = input("pilih menu anda : ").lower()
print(" ")
#pilihan crust
print("Pilih Crust            Harga")
print("pan                  = free")
print("stuffedcrust cheese  = Rp 12.000")
print("stuffedcrust sausage = Rp 9.000")
print("cheesy bites         = Rp 14.000")
print("crown crust          = Rp 12.000")
crust_pizza = input("pilih crust anda : ").lower()
print(" ")
#pilihan size
print("Pilih Size          Harga")
print("personal          = free")
print("reguler           = Rp 57.000")
print("large             = Rp 89.000")
size_pizza = input("pilih size anda : ").lower()
print(" ")
#tambahan keju
extracheese = input("Tambah Rp 13.000 untuk extracheese (ya/tidak) : ").lower()== "ya"

#input
if menu_pizza == "frankturter BBQ":
    harga_menu = 43000
elif menu_pizza == "meat monsta":
    harga_menu = 43000
elif menu_pizza == "super supreme":
    harga_menu = 43000
elif menu_pizza == "super supreme chicken":
    harga_menu = 43000
else:
    print("menu pizza tidak valid")

if crust_pizza == "pan":
    harga_crust = 0
elif crust_pizza == "stuffedcrust cheese":
    harga_crust = 12000
elif crust_pizza == "stuffedcrust sausage":
    harga_crust = 9000
elif crust_pizza == "cheesy bites":
    harga_crust = 14000
elif crust_pizza == "crown crust":
    harga_crust = 12000
else:
    print("crust anda tidak valid")

if size_pizza == "personal":
    harga_size = 0
elif size_pizza == "reguler":
    harga_size = 57000
elif size_pizza == "large":
    harga_size = 89000
else:
    print("size anda tidak valid")

harga_extracheese = 13000 if extracheese else 0
total_harga = harga_menu + harga_crust + harga_size + harga_extracheese
#output
print("==============================")
print("Harga Total : Rp",total_harga)
print("==============================")
print("==============================")
print("SELAMAT MENIKMATI")
print("TERIMA KASIH ATAS PESANAN ANDA")
print("      PIZZA HUT DELIVERY      ")
print("==============================")