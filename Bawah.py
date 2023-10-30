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
