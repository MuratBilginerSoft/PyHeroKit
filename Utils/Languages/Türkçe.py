# region JsonMessages

class Messages():

    menu = {

        "1": {"process": "1. String İfadeyi Harf Harf Büyüt"},
        "1.1": {"process": "1. String İle İşlem Yap"},
        "1.2": {"process": "2. Dosya İle İşlem Yap  (.txt)"},

        "2": {"process": "2. Txt Dosyasının İçeriğini Göster"},

        "C": {"process": "Seçiminiz (1,2,3... Yaz & Enter): "},

        "L": {"process": "L. Dil Değiştir"},

        "L1": {"process": "1. English"},
        "L2": {"process": "2. Türkçe"},

        "LE": {"process": "Bir Dil Seçin (1 or 2 & Enter): "},

        "E": {"process": "Kapatmak için Enter Tuşuna Basın..."},

        "D": {"process": "Devam Etmek İçin (D or d & Enter) - Kapatmak İçin (Enter): "},

        "G": {"process": "Geri Dmek İçin (G or g & Enter) - Kapatmak İçin (Enter): "},

    }

    process = {
            
            "1": {"message": "Dönüştürülecek String İfadenizi Girin: "},
            "2": {"message": "Kaynak Dosya Yolunu Girin: "},
            "3": {"message": "Hedef Dosya Yolunu Girin: "},
    }

    system = {

        "1": {"message": "Lütfen Bir Seçenek Belirleyin: "},
        "2": {"message": "Geçersiz Seçim..."},
        "3": {"message": "İşlem Tamamlandı..."},
        "4": {"message": "Dil Türkçe Olarak Değiştirildi..."},
        "5": {"message": "Program Kapandı..."}
    }

    info = {

        "201": {"message": "İşlem Başarıyla Gerçekleştirildi"},

        "401": {"message": ".txt Uzantılı Bir Dosya Seçmediniz..."},
        "402": {"message": "İşlem Başarısız Oldu"},
        "403": {"message": "Dosya Bulunamadı..."},
    }

# endregion
