jawab = 'y'
while(jawab == 'y') :
    no = input("no: ")
    nama = input("nama: ")
    nim = input("nim: ")
    tugas = float(input("tugas: "))
    uts = float(input("uts: "))
    uas = float(input("uas: "))
    nakhir = (tugas*30/100+uts*35/100+uas*35/100)
    print (nakhir)
    jawab = input("tambah data (y/t): ")
if(jawab == 't') :
    print ("+--------------------------------------------------------+")
    print ("| No |  Nama  |  Nim  |  Tugas  |  Uts  |  Uas  |  nakhir |")
    print ("+--------------------------------------------------------+")
    print ("|",no,"|",nama,"|",nim,"|",tugas,"|",uts,"|",uas,"|",nakhir,"|")
    
        




