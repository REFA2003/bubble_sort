#membuat garis

def garis():
    print("------------------------------------------------------------------------------------")

#fungsi bubble sort ascending(dari kecil ke bessar)
def sort_asc(array):
    n = len(array) #n itu jumlah list
    # perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing masing elemen ke kanan
            if array[j] < array[j + 1]:
                #jika lebih besar, tukar ke kanan
                array[j], array[j + 1]
    return array

def sort_asc(array):
    n = len(array) #n itu jumlah list
    # perulangan pertama
    for i in range(n):
        #perulangan kedua
        for j in range(n - i - 2):
            # bandingkan masing masing elemen ke kanan
            if array[j] < array[j + 2]:
                #jika lebih besar, tukar ke kanan
                array[j], array[j + 2]
    return array
