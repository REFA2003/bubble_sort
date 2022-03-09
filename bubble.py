#membuat garis

from time import process_time_ns


def garis():
    print("------------------------------------------------------------------------------------")

#Buat fungsi bubble ascending (dari kecil ke besar)
def sort_asc(array):
    n = len(array) #n jumlah baris
    #perulangan pertama
    for i in range(n) :
        #perulangan kedua
        for j in range(n - i - 1) : #n - i - 1 artinya nyari kurang dari satu
            #bandingkan elemen ke kanan
            if array[j] > array[j+1] : #yang sebelah kanan di bandikan dengan sebelah kiri
                #jika lebih besar maka dia pindah, ke kiri(berpindah)
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#fungsi bubble descending ( daru besar ke kecil )
def sort_dsc(array):
    n = len(array) # n jumlah baris
    #perulangan pertama
    for i in range(n) :
        #perulangan kedua
        for j in range(n - i - 1) : #n - i - 1 artinya nyari kurang dari satu
            #bandinkan elemen ke kanan
            if array[j] < array[j+1] : #yang sebelah kanan dibandingkan dengan sebelah kiri
                #jika lebih besar maka dia pindah, ke kiri(berpindah)
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

#fungsi rata - rata
def rata_rata(angka):
  return sum(angka) / len(angka)
#input memasukan nilai
garis()
print("Masukkan nilai sebanyak yang kamu mau !")
print("Contoh : 7 6 5 4 8")
angka = list(map(int, input("Masukkan Nilainya : ").split()))
garis()
print()

#input memilih pilihan asc dan dsc
garis()
print("Pilih Metodenya!")
print("Ascending = 1 | Descending = 2")
pilih = int(input("Pilihan = "))
garis()

#menentukan nilai
if pilih == 1:
    print()
    print("HASIL AKHIR-----")
    print("Urutan angka ascending", (sort_asc(angka)))
else:
    print("Urutan angka descending", (sort_dsc(angka)))

#cari angka terbesar
print("Angka Terbesar : ", max(angka))

#cari angka terkecil
print("Angka Terkecil : ", min(angka))

#Jumlahkan angkanya
print("Jumlahnya : ", sum(angka))

#rata rata
print("Rata - ratanya : ", round(rata_rata(angka), 2))


