import os as o, webbrowser as w, platform as p # imports
link = ("easteregg","https://youtu.be/Drgg4VpQpFI", "https://youtu.be/HvMGPvduqGg", "https://youtu.be/Rh5MYx02iNM", "https://youtu.be/rFnXvhX9GLU", "https://youtu.be/nqA3YVx72Ic", "https://youtu.be/Qi3iiu_bRR8", "https://youtu.be/CotoizBwjqI", "https://youtu.be/wGo4vf8BFvU", "https://youtu.be/nkgGBBGJeSA", "https://youtu.be/514yU6WcPGk", "https://youtu.be/bBtl_h9lYd0") # links

def mulai():
    global sistemc
    if p.system() == "Windows" or p.system() == "win64" or p.system() == "win32":
        sistemc = "cls"
        o.system("cls")
        menu()
        error()
        pilih()

    elif p.system() == "Linux" or p.system() == "OS X" or p.system() == "linux" or p.system() == "linux2" or p.system() == "darwin" or p.system() == "Darwin":
        sistemc = "clear"
        o.system("clear")
        menu()
        error()
        pilih()

    else:
        print("OS Anda tidak di support\n")
        android = input("Apakah Anda menggunakan Android?\n[y/n] = ")
        if android == "y" or android == "Y" :
            sistemc = "clear"
            o.system("clear")
            menu()
            error()
            pilih()
        
        elif android == "n" or android == "N" :
            print("Bye\n")
            import time as t
            for i in range (7):
                t.sleep(1)
                print('{:2d}'.format(5-i),end="\r")
            sistemc = ""
            o.system("exit")

        else:
            print("Ketik y/n saja. Y/y artinya yes (iya) dan N/n artinya no (tidak)\n")
            mulai()

def menu():
    print("\n1. Pengenalan\n2. Game Development\n3. Tips untuk Game Development\n4. Mengenal Game Dadulfall Post Mortem\n5. Instalasi unity & setup project\n6. Membuat player\n7. Player bisa gerak & game manager\n8. Membuat UI\n9. Membuat peluru player\n10. Membuat musuh\n11. Musuh bisa menembak\n12. Download e-certificate")
    
def error():
    print("\n\n99. Error, link tidak membuka browser")

def pilih():
    global pilih
    try :
        pilih = int(input("\nPilih = ")) # Pemilihan
        if pilih != "" :
            pembuka()

        else:
            print("Masukkan angkanya contoh 1 atau bisa juga 1.")
            mulai()

    except ValueError:
        if sistemc != "" :
            o.system(sistemc)
        print("\nAnda hanya boleh memasukkan angka\n\n")

def pembuka():
    if pilih != "" and pilih != int("0") and pilih != int("99"):
        w.open(link[pilih])

    elif pilih == int("0") :
        if p.system() == "Windows" or p.system() == "win64" or p.system() == "win32":
            w.open(link[pilih])

        else:
            o.system(sistemc)
            print("\nMaaf angka 0 hanya tersedia untuk Windows (Windows 10)\n\n")

    elif pilih == int("99") :
        o.system(sistemc)
        menu()

        pilihError = int(input("\n[Error mode]\nPilih  = "))
        if pilihError != "" and pilihError != int("0"):
            print("\nLink video =", link[pilihError], end="\n\n")

        elif pilihError == int("0") :
            if p.system() == "Windows" or p.system() == "win64" or p.system() == "win32":
                w.open(link[pilihError])

            else:
                o.system(sistemc)
                print("\nMaaf angka 0 hanya tersedia untuk Windows (Windows 10)\n\n")

        else:
            print("Masukkan angkanya contoh 1 atau bisa juga 1.")
            mulai()

    else:
        print("Masukkan angkanya contoh \"1\"")
        mulai()

if __name__ == "__main__" :
    mulai()
