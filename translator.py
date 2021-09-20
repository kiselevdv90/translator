from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import sqlite3
from random import choice

def sound(lang):
    
    tts = gTTS(lang)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    os.remove('hello.mp3')


translator = sqlite3.connect('vocabulary.db')
data = translator.cursor()
data.execute('''CREATE TABLE IF NOT EXISTS vocabulary (
	Word_en TEXT,
	Word_ru TEXT)''')
translator.commit()

Question = input('Тренировка или перевод?  ')

if Question == 'перевод':

    while True:
        # ОСТАНОВКА ЦИКЛА
        Word_ru = input('Введите текст: ')
        if Word_ru  == 'все':
            break

        # Переводит с русского на английский
        translator = Translator()
        Word_en = translator.translate(Word_ru, dest='en')
        Word_en = Word_en.text
        print(Word_en)

        # ОЗВУЧИВАНИЕ ТЕКСТА
        tts = gTTS(Word_en)
        tts.save('hello.mp3')
        playsound('hello.mp3')
        os.remove('hello.mp3')

        # ЗАПИСЫВАЕТ СЛОВА В БАЗУ ДАННЫХ
        translator = sqlite3.connect('vocabulary.db')
        data = translator.cursor()
        data.execute(
            f'''SELECT Word_en FROM vocabulary WHERE Word_en = "{Word_en}"''')
        if data.fetchone() is None:
            data.execute(f'INSERT INTO vocabulary VALUES (?,?)',
                         (Word_en, Word_ru))
            translator.commit()
            data.close()
        else:
            print('Запись есть')

        data.close()

else:
    r = data.execute('''SELECT * fROM vocabulary''').fetchall()
    data.close()
    languages = input('1 Русский-Английский, 2 Английский-Русский ')
    if languages == 1:
        while True:
            a = choice(r)
            print(a[1])

            tts = gTTS(a[1])
            tts.save('hello.mp3')
            playsound('hello.mp3')
            os.remove('hello.mp3')

            b = input('Напиши перевод: ')
            if b == 'все':
                break
            if a[0] == b:
                print('Молодец!')
            else:
                print('Неправильно. Ответ: ' + a[0])
    else:
        while True:
            a = choice(r)
            print(a[0])

            tts = gTTS(a[0])
            tts.save('hello.mp3')
            playsound('hello.mp3')
            os.remove('hello.mp3')

            b = input('Напиши перевод: ')
            if b == 'все':
                break
            if a[1] == b:
                print('Молодец!')
            else:
                print('Неправильно. Ответ: ' + a[1])







	

