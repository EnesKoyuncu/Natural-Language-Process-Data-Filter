import re
import nltk
from nltk.corpus import stopwords
from langdetect import detect


# Anahtar kelimelerinizi buraya ekleyin
anahtar_kelimeler = ["kelime1", "games"]


# İngilizce stopwords (durak kelimeler) listesini indiriyoruz.
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def metin_isleme(kaynak_dosya, sonuc_dosya):
    with open(kaynak_dosya, 'r', encoding='utf-8') as dosya:
        text = dosya.read()

    # Cümleleri ayırıyoruz.
    cumleler = re.split(r'(?<=[.!?]) +', text)

    processed_cumleler = []
    for cumle in cumleler:
        # Noktalama işaretlerini kaldırıyoruz.
        cumle = re.sub(r'[^\w\s]', '', cumle)

        # Tüm kelimeleri küçük harf yapıyoruz.
        cumle = cumle.lower()

        # Rakamları ve sayısal tüm ifadeleri kaldırıyoruz.
        cumle = re.sub(r'\d+', '', cumle)

        # Stopwords kelimeleri kaldırıyoruz.
        cumle = ' '.join(kelime for kelime in cumle.split() if kelime not in stop_words)

        # 1 ve 2 harfli kelimeleri kaldırıyoruz.
        cumle = ' '.join(kelime for kelime in cumle.split() if len(kelime) > 2)

        # İngiliz alfabesinde olmayan harf veya karakterler görürse satırdaki cümleyi komple siliyoruz.
        if re.search(r'[^a-zA-Z\s]', cumle):
            continue

        # Satırdaki cümle 3 kelimeden daha kısaysa satırdaki cümleyi komple siliyoruz.
        if len(cumle.split()) < 3:
            continue

        # Satırdaki cümlenin ingilizce olup olmadığını test ediyoruz.
        try:
            if detect(cumle) != 'en':
                continue
        except:
            continue

        # Anahtar kelime kontrolü
        if not any(kelime in cumle for kelime in anahtar_kelimeler):
            continue

        processed_cumleler.append(cumle)

    # Sonuçları bir dosyaya yazıyoruz
    with open(sonuc_dosya, 'w', encoding='utf-8') as dosya:
        dosya.write('\n'.join(processed_cumleler))

    print(f"'{sonuc_dosya}' dosyası başarıyla oluşturuldu ve işlendi.")

# İşlemi başlatıyoruz.
metin_isleme('kaynak_metin.txt', 'sonuc_metin_anahtar_kelimeler.txt')
