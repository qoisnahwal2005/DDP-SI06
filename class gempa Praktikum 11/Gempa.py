class Gempa:
    # konstruktor inisialisasi atribut
    def __init__(self, lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
    
    # Method Penentu Skala Gempa
    def dampak(self):
        # Logika Statemant
        if self.skala < 2:
           print('Gempa tidak berasa')
        elif 2 <= self.skala <= 4:
            print('Gempa berdampak bangunan retak')
        elif 4 <= self.skala <= 6:
            print('Gempa berdampak bangunan roboh')
        elif self.skala > 6:
            print('Dampak gempa bangunan roboh dan berpotensi tsunami ')
        
        # Menampilkan lokasi dan skala gempa 
        print(f'Lokasi gempa: {self.lokasi}')
        print(f'Skala gempa: {self.skala}')
