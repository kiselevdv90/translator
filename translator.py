from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import sqlite3

translator = sqlite3.connect('vocabulary.db')
data = translator.cursor()
data.execute('''CREATE TABLE IF NOT EXISTS vocabulary (
	Word_en TEXT,
	Word_ru TEXT)''')
translator.commit()

while True :
	#ОСТАНОВКА ЦИКЛА	
	Word_ru = input('Введите текст: ')
	if Word_ru == 'все':
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

	#ЗАПИСЫВАЕТ СЛОВА В БАЗУ ДАННЫХ
	translator = sqlite3.connect('vocabulary.db')
	data = translator.cursor()
	data.execute('INSERT INTO vocabulary VALUES (?,?)', (Word_en, Word_ru))
	data.close()
	translator.commit()
	




	

