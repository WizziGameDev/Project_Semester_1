import csv
import os

''' CRUD CSV Python '''

os.system('cls')

def createCsv(createData):
    ''' CREATE '''
    with open('data.csv', 'a', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        write_file.writerow(createData)

def readCsv():
    ''' READ + UPDATE '''
    with open('data.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        csvtoList = []
        for data_list in reader:
            csvtoList.append(data_list)
        return csvtoList

def deleateCsv(remove_data):
    ''' DELETE '''
    # Open File CSV nya
    openCsv = readCsv()

    ''' Remove Data '''
    for dataList in openCsv:
        if remove_data in dataList[1]: # jika ingin menghapus index ke berapa
            openCsv.remove(dataList)
    
    listRemove = openCsv
    print(listRemove)

    with open('data.csv', 'w', newline='') as csv_file:
        write_file = csv.writer(csv_file)
        for i in listRemove:
            write_file.writerow(i)

''' Bagian Jalan kan Function '''
# Penggunaan Create
dataMasuk = ('dilan', 'pros', 12) # Memasukkan 3 data dama 1 row
createCsv(dataMasuk)

# Penggunaan Read File
readCsv() # Harus ada

# Penggunaan Delete data
data_del = input(' Masukkan nama yang akan di hapus index 1 = ')
deleateCsv(data_del)