# region JsonMessages

class Messages():

    menu = {

        "1": {"process": "1. String İfadeyi Harf Harf Büyüt"},
        "1.1": {"process": "1. String İle İşlem Yap"},
        "1.2": {"process": "2. Dosya İle İşlem Yap  (.txt)"},

        "2": {"process": "2. Txt Dosyasının İçeriğini Göster"},
        "3": {"process": "3. String Karakter Sayısı Bul"},
        "4": {"process": "4. Klasör İçeriğini Göster"},
        "5": {"process": "5. Klasördeki İstediğim Uzantılı Dosyaları Sil"},
        "6": {"process": "6. Klasördeki İstediğim Alt Klasörleri Sil"},
        "7": {"process": "7. Klasördeki Dosyların Uzantısını Değiştir"},

        "C": {"process": "Seçiminiz (1,2,3... Yaz & Enter): "},

        "L": {"process": "L. Dil Değiştir"},
        "O": {"process": "O. Output Method Değiştir"},

        

        "L1": {"process": "1. English"},
        "L2": {"process": "2. Türkçe"},

        "O1": {"process": "1. Terminal"},
        "O2": {"process": "2. File"},

        "LE": {"process": "Lütfen Bir Dil Seçiniz (1 or 2 & Enter): "},
        "OE": {"process": "Lütfen Çıktı Methodu Seçiniz (1 or 2 & Enter): "},

        "E": {"process": "Kapatmak için Enter Tuşuna Basın..."},

        "D": {"process": "Ana Menü İçin (A or a) - Aynı İşlemi Tekrar Etmek İçin (D or d & Enter) - Kapatmak İçin (Enter): "},

        "G": {"process": "Geri Dmek İçin (G or g & Enter) - Kapatmak İçin (Enter): "},

        "S": {"process": "Yukarıdaki Dosyalarınız Silme İşleminden Etkilenecek Devam Etmek İstiyor Musunuz? (E or e & Enter): "},

    }

    process = {
            
            "1": {"message": "Dönüştürülecek String İfadenizi Girin: "},
            "2": {"message": "Kaynak Dosya Yolunu Girin: "},
            "3": {"message": "Hedef Dosya Yolunu Girin: "},
            "4": {"message": "String İfadenizi Girin: "},
            "5": {"message": "Klasör Yolunu Girin(C:\\Users\\UserName\\Masaüstü gibi): "},
            "6": {"message": "Dosya Uzantısını Girin(png gibi): "},
            "7": {"message": "Silinecek Klasör İsmini Girin: "},
            "8": {"message": "Değiştirilecek Dosya Uzantısını Girin(webp gibi): "},
            "9": {"message": "Yeni Dosya Uzantısını Girin(png gibi): "}, 
            "10": {"message": "Alt Klasörler Etkilensin mi? (E/H): "},
    }

    system = {

        "1": {"message": "Lütfen Bir Seçenek Belirleyin: "},
        "2": {"message": "Geçersiz Seçim..."},
        "3": {"message": "İşlem Tamamlandı..."},
        "4": {"message": "Dil Türkçe Olarak Değiştirildi..."},
        "5": {"message": "Program Kapandı..."},
        "6": {"message": "Çıktı Yöntemi"},
        "7": {"message": "Dil"},
        "8": {"message": "Karakter Sayısı: "},
        "9": {"message": "Harf Sayısı: "},
        "10": {"message": "Boşluk Sayısı: "},
        "11": {"message": "Noktalama İşareti Sayısı: "},
        "12": {"message": "Klasör Sayısı: "},
        "13": {"message": "Dosya Sayısı: "},
        "14": {"message": "Dosya Türleri: "},
        "15": {"message": "Dosya Türü Sayısı: "},
        "16": {"message": "Silinen Dosya Listesi: "},
        "17": {"message": "Silinecek Dosya Listesi: "},
        "18": {"message": "Silinecek Klasör Listesi: "},
        "19": {"message": "Silinen Klasör Listesi: "},
        "20": {"message": "Klasör Sayısı: "},
        "21": {"message": "Etkilenecek Dosya Listesi: "},
        "22": {"message": "Etkilenen Dosya Listesi: "},
    }

    info = {

        "201": {"message": "İşlem Başarıyla Gerçekleştirildi"},
        "202": {"message": "Dosya Okundu"},
        "203": {"message": "Dosyanız Oluşturuldu"},
        "204": {"message": "Dosya Silindi"},
        "205": {"message": "Klasör Silindi"},
        

        "301": {"message": "İşlem Devam Ediyor Lütfe Bekleyin..."},
        "302": {"message": "İlerleme: "},

        "401": {"message": ".txt Uzantılı Bir Dosya Seçmediniz..."},
        "402": {"message": "İşlem Başarısız Oldu"},
        "403": {"message": "Dosya Bulunamadı..."},
        "404": {"message": "Klasör Bulunamadı..."},
        "405": {"message": "Girilen Yol Bir Klasör Değil..."},
        "406": {"message": "İşlemden Vazgeçildi..."},


        "501": {"message": "Taranan Dosya: "},
        "502": {"message": "Taranan Klasör: "},

    }

# endregion
