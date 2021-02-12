import os as o, webbrowser as w, platform as p # imports
link = ("easteregg","https://youtu.be/Drgg4VpQpFI", "https://youtu.be/HvMGPvduqGg", "https://youtu.be/Rh5MYx02iNM", "https://youtu.be/rFnXvhX9GLU", "https://youtu.be/nqA3YVx72Ic", "https://youtu.be/Qi3iiu_bRR8", "https://youtu.be/CotoizBwjqI", "https://youtu.be/wGo4vf8BFvU", "https://youtu.be/nkgGBBGJeSA", "https://youtu.be/514yU6WcPGk", "https://youtu.be/bBtl_h9lYd0") # links

def mulai():
    if p.system() == "Windows" or p.system() == "win64" or p.system() == "win32":
        o.system("cls")
        menu()
    elif p.system() == "Linux" or p.system() == "OS X" or p.system() == "linux" or p.system() == "linux2" or p.system() == "darwin" or p.system() == "Darwin":
        o.system("clear")
        menu()
    else:
        print("OS Anda tidak di support\n")
        android = input("Apakah Anda menggunakan Android?\n[y/n] = ")
        if android == "y" or android == "Y" :
            menu()
        
        elif android == "n" or android == "N" :
            print("Bye\n")
            import time as t
            for i in range (7):
                t.sleep(1)
                print('{:2d}'.format(5-i),end="\r")
            o.system("exit")

        else:
            print("Ketik y/n saja. Y/y artinya yes (iya) dan N/n artinya no (tidak)\n")
            mulai()

def menu():
    print("\n1. Pengenalan\n2. Game Development\n3. Tips untuk Game Development\n4. Mengenal Game Dadulfall Post Mortem\n5. Instalasi unity & setup project\n6. Membuat player\n7. Player bisa gerak & game manager\n8. Membuat UI\n9. Membuat peluru player\n10. Membuat musuh\n11. Musuh bisa menembak\n12. Download e-certificate")
    pilih()

def pilih():
    global pilih
    pilih = input("\nPilih = ") # Pemilihan
    if pilih != "" :
        pembuka()

    else:
        print("Masukkan angkanya contoh 1 atau bisa juga 1.")
        mulai()

def pembuka():
    if pilih == "1" or pilih == "1." :
        w.open(link[1])
    elif pilih == "2" or pilih == "2." :
        w.open(link[2])
    elif pilih == "3" or pilih == "3." :
        w.open(link[3])
    elif pilih == "4" or pilih == "4" :
        w.open(link[4])
    elif pilih == "5" or pilih == "5." :
        w.open(link[5])
    elif pilih == "6" or pilih == "6." :
        w.open(link[6])
    elif pilih == "7" or pilih == "7." :
        w.open(link[7])
    elif pilih == "8" or pilih == "8." :
        w.open(link[8])
    elif pilih == "9" or pilih == "9." :
        w.open(link[9])
    elif pilih == "10" or pilih == "10." :
        w.open(link[10])
    elif pilih == "11" or pilih == "11." :
        w.open(link[11])
    elif pilih == "12" or pilih == "12." :
        w.open(link[12])
    else:
        print("Masukkan angkanya contoh 1 atau bisa juga 1.")
        mulai()

if __name__ == "__main__" :
    mulai()
