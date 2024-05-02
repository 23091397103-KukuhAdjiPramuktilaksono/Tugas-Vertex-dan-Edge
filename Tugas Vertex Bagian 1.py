class Peta: 
    def __init__(self):
        self.cityList = {}

    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":", self.cityList[kota])

    def tambahkanKota(self, kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self, kotaDihapus):
        if kotaDihapus in self.cityList:
            # Hapus kotaDihapus dari setiap kota lain
            for kotalain in self.cityList:
                # Cek apakah kota yang ingin dihapus ada jalannya ke kota lain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            # Hapus kotaDihapus dari daftar kota
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            # Masukkan kota1 di list kota2
            self.cityList[kota2].append(kota1)
            # Masukkan kota2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            # Hapus kota1 di list kota2
            self.cityList[kota2].remove(kota1)
            # Hapus kota2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False

petaIndonesia = Peta()
petaIndonesia.tambahkanKota("Bangkalan")
petaIndonesia.tambahkanKota("Lamongan")
petaIndonesia.tambahkanKota("Bojonegoro")
petaIndonesia.tambahkanKota("Gresik")
petaIndonesia.tambahkanKota("Surabaya")
petaIndonesia.tambahkanKota("Sidoarjo")
petaIndonesia.tambahkanKota("Mojokerto")
petaIndonesia.tambahkanKota("Nganjuk")
petaIndonesia.tambahkanKota("Pasuruan")
petaIndonesia.tambahkanKota("Malang")
petaIndonesia.tambahkanKota("Probolinggo")
petaIndonesia.tambahkanKota("Lumajang")
petaIndonesia.tambahkanKota("Kediri")
petaIndonesia.tambahkanKota("Blitar")
petaIndonesia.tambahkanJalan("Bangkalan", "Surabaya")
petaIndonesia.tambahkanJalan("Surabaya", "Sidoarjo")
petaIndonesia.tambahkanJalan("Sidoarjo", "Pasuruan")
petaIndonesia.tambahkanJalan("Pasuruan", "Probolinggo")
petaIndonesia.tambahkanJalan("Probolinggo", "Lumajang")
petaIndonesia.tambahkanJalan("Lumajang", "Malang")
petaIndonesia.tambahkanJalan("Malang", "Mojokerto")
petaIndonesia.tambahkanJalan("Mojokerto", "Gresik")
petaIndonesia.tambahkanJalan("Gresik", "Lamongan")
petaIndonesia.tambahkanJalan("Lamongan", "Bojonegoro")
petaIndonesia.tambahkanJalan("Bojonegoro", "Nganjuk")
petaIndonesia.tambahkanJalan("Nganjuk", "Kediri")
petaIndonesia.tambahkanJalan("Kediri", "Blitar")
petaIndonesia.tambahkanJalan("Blitar", "Malang")
petaIndonesia.tambahkanJalan("Surabaya", "Gresik")
petaIndonesia.tambahkanJalan("Sidoarjo", "Malang")
petaIndonesia.tambahkanJalan("Mojokerto", "Kediri")
petaIndonesia.tambahkanJalan("Lamongan", "Surabaya")
petaIndonesia.tambahkanJalan("Pasuruan", "Malang")
petaIndonesia.tambahkanJalan("Sidoarjo", "Mojokerto")
petaIndonesia.printPeta()
print('------------------------------')
petaIndonesia.hapusKota("Bangkalan")
petaIndonesia.printPeta()
