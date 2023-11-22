#CAPSTONE MODULE 1 PURWADHIKA JCDS
#DATA NILAI MAHASISWA

#DAFTAR MAHASISWA
Data_Mahasiswa = [
    {'NIM' : 111, 'NAMA' : 'ASEP', 'JENIS KELAMIN' : 'LAKI-LAKI', 'NILAI' : 40, 'GRADE' : 'E', 'STATUS' : 'TIDAK LULUS' },
    {'NIM' : 112, 'NAMA' : 'BENI', 'JENIS KELAMIN' : 'LAKI-LAKI', 'NILAI' : 60, 'GRADE' : 'D', 'STATUS' : 'TIDAK LULUS' },
    {'NIM' : 113, 'NAMA' : 'CACA', 'JENIS KELAMIN' : 'PEREMPUAN', 'NILAI' : 90, 'GRADE' : 'A', 'STATUS' : 'LULUS' }]
#FUNCTION MEMBUAT TABLE
def table() :
    print('\n___________________|TABLE NILAI MAHASISWA 2023|__________________________')
    print('NIM\t| NAMA  \t| JENIS KELAMIN\t| NILAI\t | GRADE | STATUS')
    for i in range(len(Data_Mahasiswa)) :
        print('{}\t| {}  \t| {}\t| {}\t |   {}\t | {}'.format(Data_Mahasiswa[i]['NIM'],Data_Mahasiswa[i]['NAMA'],Data_Mahasiswa[i]['JENIS KELAMIN'],Data_Mahasiswa[i]['NILAI'],Data_Mahasiswa[i]['GRADE'],Data_Mahasiswa[i]['STATUS']))
#FUNCTION SEARCH
def cari():
    NIM_MHS = int(input('\t    Masukan NIM Mahasiswa yang dicari : '))
    for i in range(len(Data_Mahasiswa)):
        if NIM_MHS == Data_Mahasiswa[i]['NIM']:
            print('\n-----------------------Data ditemukan----------------------------')
            print('NIM\t| NAMA  \t| JENIS KELAMIN\t| NILAI\t | GRADE | STATUS')
            print('{}\t| {}  \t| {}\t| {}\t |   {}\t | {}'.format(Data_Mahasiswa[i]['NIM'],Data_Mahasiswa[i]['NAMA'],Data_Mahasiswa[i]['JENIS KELAMIN'],Data_Mahasiswa[i]['NILAI'],Data_Mahasiswa[i]['GRADE'],Data_Mahasiswa[i]['STATUS']))
#FUNCTION READ TABLE ATAU MENAMPILKAN DATA NILAI MAHASISWA
def read():
    while True:
        menuRead = int(input('''
            Menu read:
            1. Data nilai Mahasiswa
            2. Cari nilai Mahasiswa
            3. Kembali ke menu utama
                    
            Masukan nilai angka untuk memilih menu read [1-3] : '''))
        if menuRead == 1 :
            table()
        elif menuRead == 2:
            cari()
        elif menuRead == 3 :
            Menu_Utama()
        else :
            print('\n\t ***Inputan anda salah, Mohon untuk input angka*** [1-3]')
        read()
#FUNCTION CREATE DATA ATAU MEMBUAT ISI TABLE NILAI
def create() :
    while True:
        menuCreate = int(input('''
            Menu create:
            1. Data nilai Mahasiswa
            2. Tambah data nilai Mahasiswa
            3. Kembali ke Menu Utama
                           
            Masukan nilai angka untuk memilih menu create [1-3] : '''))
        if menuCreate == 1 :
            table()
        elif menuCreate == 2 :
            crete_nim = int(input('\nMasukkan NIM Mahasiswa : '))
            Cek_duplicate = list(filter(lambda data : data['NIM'] == crete_nim, Data_Mahasiswa))
            if len(Cek_duplicate):
                print('-------------------------Data sudah ada!---------------------------')
                print('-----------Terdeteksi Duplikat, silahkan input data lain-----------')
                return create()
            else:
                create_nama = input('Masukkan nama Mahasiswa : ').upper()
                create_JK = input('Jenis Kelamin Mahasiswa [L/P]: ').upper()
                create_nilai = int(input('Masukkan NILAI Mahasiswa : '))
                create_grade = ''
                create_status = ''

                if(create_nilai >= 90 and create_nilai <= 100) :
                    create_grade = 'A'
                elif(create_nilai >= 80 and create_nilai <= 89) :
                    create_grade = 'B'
                elif(create_nilai >= 70 and create_nilai <= 79) :
                    create_grade = 'C'
                elif(create_nilai >= 60 and create_nilai <= 69) :
                    create_grade = 'D'
                elif(create_nilai >= 0 and create_nilai <= 59) :
                    create_grade = 'E'
                else :
                    create_grade = 'BERMASALAH'

                if(create_grade == 'D') :
                    create_status = 'TIDAK LULUS'
                elif(create_grade == 'E') :
                    create_status = 'TIDAK LULUS'
                else :
                    create_status = 'LULUS'
                Confrim_Add = input('Apakah anda yakin manambah data tersebut [Y/N] : ')
                if Confrim_Add == 'Y':             
                    Data_Mahasiswa.append({
                                    'NIM': crete_nim,
                                    'NAMA': create_nama,
                                    'JENIS KELAMIN': create_JK,
                                    'NILAI' : create_nilai,
                                    'GRADE' : create_grade,
                                    'STATUS' : create_status
                                })
                    print('Data Berhasil ditambah')
                    table()
                elif Confrim_Add == 'N':
                    print('Data gagal ditambah')
                else:
                    create()

        elif menuCreate == 3 :
            Menu_Utama()
        else :
            print('\n\t ***Inputan anda salah, Mohon untuk input angka*** [1-3]')
        create()
#FUNCTION DELETE ISI TABLE
def delete():
    table()
    menudelete = int(input('''
        Menu delete:
        1. Menghapus data nilai mahasiswa
        2. Kembali ke menu utama
                           
        Masukan nilai angka untuk memilih menu delete [1-2] : '''))
    if menudelete == 1 :
        delete_data = int(input('Masukkan NIM Mahasiswa yang akan dihapus : '))
        for i in range(len(Data_Mahasiswa)):
            if delete_data == Data_Mahasiswa[i]['NIM']:
                while True:
                    print('Data ditemukan')
                    print('NIM\t| NAMA  \t| JENIS KELAMIN\t| NILAI\t | GRADE | STATUS')
                    print('{}\t| {}  \t| {}\t| {}\t |   {}\t | {}'.format(Data_Mahasiswa[i]['NIM'],Data_Mahasiswa[i]['NAMA'],Data_Mahasiswa[i]['JENIS KELAMIN'],Data_Mahasiswa[i]['NILAI'],Data_Mahasiswa[i]['GRADE'],Data_Mahasiswa[i]['STATUS']))
                    Confirm_del = input('Apakah anda yakin menghapus data tersebut [Y/N] : ')
                    if Confirm_del == 'Y' :
                        del Data_Mahasiswa[i]
                        print('Data Mahasiswa dgn NIM {} tersebut berhasil dihapus'.format(delete_data))
                        Menu_Utama()
                    else:
                     print('Data gagal dihapus')
                    break
                break
            elif (i == len(Data_Mahasiswa)-1) :
                print('Data tidak ditemukan, Silahkan masukan data yang lain')
                delete()

    elif menudelete == 2 :
            Menu_Utama()
    else :
        print('Masukan anda salah, silahkan memilih menu [1-2] : ')
        delete()
#FUNCTION UPDATE ATAU MENGUBAH ISI TABLE
def update():
    while True:
        table()
        menuupdate = int(input('''
        Menu Update:
        1. Mengganti data nilai mahasiswa
        2. Kembali ke menu utama
                           
        Masukan nilai angka untuk memilih menu update [1-2] : '''))
        if menuupdate == 1:
            update_data = int(input('\tMasukkan NIM Mahasiswa yang akan diupdate: '))
            for i in range(len(Data_Mahasiswa)):
                if update_data == Data_Mahasiswa[i]['NIM']:
                    while True:
                        print('\n-----------------------Data ditemukan----------------------------')
                        print('NIM\t| NAMA  \t| JENIS KELAMIN\t| NILAI\t | GRADE | STATUS')
                        print('{}\t| {}  \t| {}\t| {}\t |   {}\t | {}'.format(Data_Mahasiswa[i]['NIM'],Data_Mahasiswa[i]['NAMA'],Data_Mahasiswa[i]['JENIS KELAMIN'],Data_Mahasiswa[i]['NILAI'],Data_Mahasiswa[i]['GRADE'],Data_Mahasiswa[i]['STATUS']))
                        Confirm_Update = input('\tApakah anda yakin mengganti data tersebut [Y/N] : ').upper()
                        if Confirm_Update == 'Y':
                            while True:
                                update_value = int(input('''
                        Kolom mana yang ingin diubah ?
                            1. NIM
                            2. NAMA
                            3. JENIS KELAMIN
                            4. NILAI 
                            5. Kembali ke menu sebelumnya
                        Masukkan angka range [1-5]: '''))
                                if update_value == 1:
                                    ubah_NIM = int(input('\t\t\tMasukkan NIM Mahasiswa terbaru: '))
                                    if ubah_NIM == '' == False:
                                        print('\t\t\tHarap diisikan NIM Mahasiswa yang baru: ')
                                    else:
                                        Data_Mahasiswa[i]['NIM'] = ubah_NIM
                                elif update_value == 2:
                                    ubah_nama = input('\t\t\tMasukkan Nama Mahasiswa Terbaru: ')
                                    if ubah_nama == '' == False:
                                        print('\t\t\tHarap diisi dengan Nama Mahasiswa terbaru')
                                    else:
                                        Data_Mahasiswa[i]['NAMA'] = ubah_nama
                                elif update_value == 3:
                                    ubah_JK = input('\t\t\tJenis Kelamin L/P : ')
                                    if ubah_JK == 'L' :
                                        Data_Mahasiswa[i]['JENIS KELAMIN'] = 'Laki-Laki'
                                    else :
                                        Data_Mahasiswa[i]['JENIS KELAMIN'] = 'Perempuan'
                                elif update_value == 4:
                                    ubah_nilai = int(input('\t\t\tMasukan nilai Mahasiswa Terbaru: '))
                                    Data_Mahasiswa[i]['NILAI'] = ubah_nilai      
                                    if(ubah_nilai >= 90 and ubah_nilai <= 100) :
                                        ubah_grade = 'A'
                                    elif(ubah_nilai >= 80 and ubah_nilai <= 89) :
                                        ubah_grade = 'B'
                                    elif(ubah_nilai >= 70 and ubah_nilai <= 79) :
                                        ubah_grade = 'C'
                                    elif(ubah_nilai >= 60 and ubah_nilai <= 69) :
                                        ubah_grade = 'D'
                                    elif(ubah_nilai >= 0 and ubah_nilai <= 59) :
                                        ubah_grade = 'E'
                                    else :
                                        ubah_grade = 'T [BERMASALAH]'
                                    
                                    Data_Mahasiswa[i]['GRADE'] = ubah_grade

                                    if(ubah_grade == 'D') :
                                        ubah_status = 'TIDAK LULUS'
                                    elif(ubah_grade == 'E') :
                                        ubah_status = 'TIDAK LULUS'
                                    else :
                                        ubah_status = 'LULUS'

                                    Data_Mahasiswa[i]['STATUS'] =  ubah_status
                                break
                        break
                    update()
        elif menuupdate == 2:
                Menu_Utama()
        else:
            print('\n\t ***Inputan anda salah, Mohon untuk input angka*** [1-6]')
            update()
#FUNCTION MENU ATAU FITUR TAMBAHAN    
def fiturtambah():
    while True:
        menuBaru = int(input('''
        Menu Fitur Lainya:
                             
        1. Sorting by NIM
        2. Sorting by Nama
        3. Sorting by Ranking Nilai
        4. Sorting by Lulus/Tidak
        5. Kembali ke menu utama
                           
        Masukan nilai angka untuk memilih menu delete [1-5] : '''))
        if menuBaru == 1:
            SortingNIM = sorted(Data_Mahasiswa,key= lambda x: x['NIM'])
        elif menuBaru == 2:
            SortingNIM = sorted(Data_Mahasiswa,key= lambda x: x['NAMA'])
        elif menuBaru == 3:
            SortingNIM = sorted(Data_Mahasiswa,key= lambda x: x['NILAI'], reverse=True)
        elif menuBaru == 4:
            SortingNIM = sorted(Data_Mahasiswa,key= lambda x: x['STATUS'])
        elif menuBaru == 5:
            Menu_Utama()
        else:
            print('\n\t ***Inputan anda salah, Mohon untuk input angka*** [1-5]')
            fiturtambah()

        print('-------------------------DATA NILAI MAHASISWA----------------------')
        print('NIM\t| NAMA  \t| JENIS KELAMIN\t| NILAI\t | GRADE | STATUS')
        for i in range(len(SortingNIM)) :
                print('{}\t| {}  \t| {}\t| {}\t |   {}\t | {}'.format(SortingNIM[i]['NIM'],SortingNIM[i]['NAMA'],SortingNIM[i]['JENIS KELAMIN'],SortingNIM[i]['NILAI'],SortingNIM[i]['GRADE'],SortingNIM[i]['STATUS']))
#FUNCTION MENU UTAMA 
def Menu_Utama():
    while True:
        daftarMenu = int(input('''
            |DATA NILAI MAHASISWA|
            
            List Menu:
            1. Menampilkan data nilai Mahasiswa
            2. Menambahkan data nilai Mahasiswa
            3. Mengubah data nilai Mahasiswa
            4. Menghapus data nilai Mahasiswa
            5. Menu tambahan
            6. Exit Program
            
            Masukan nilai angka untuk memilih menu [1-6] :  '''))
        if(daftarMenu == 1) :
            read()
        elif(daftarMenu == 2) :
            create()
        elif(daftarMenu == 3) :
            update()
        elif(daftarMenu == 4) :
            delete()
        elif(daftarMenu == 5) :
            fiturtambah()
        elif(daftarMenu == 6) :
            exit()
        else:
            print('\n\t ***Inputan anda salah, Mohon untuk input angka*** [1-6]')
#CALL MENU UTAMA
Menu_Utama()           