from PIL import Image, ImageDraw, ImageFont
import math
import random

inp = random.randint(0, 1)
if inp == 0:
	#-------------------------------------------------------------------------------Sample1-----------------------------------------------------------------------------
	image = Image.open("Samples\\Sample2.png") #Открываем изображение. 
	logo = Image.open("Samples\\bk.png") #Открываем лого. 
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 

	widthImg = image.size[0] #Определяем ширину карточки. 
	heightImg = image.size[1] #Определяем высоту карточки. 	
	widthLogo = logo.size[0] #Определяем ширину лого. 
	heightLogo = logo.size[1] #Определяем высоту лого.

	koef = float('{:.5f}'.format(widthLogo / heightLogo)) #Коэффицент отношения ширины лого к длине

	#Новые размеры для лого
	if widthLogo > 155 or heightLogo > 160:
		if widthLogo > heightLogo:
			newLSize = (155, math.ceil(155 / koef))  
		else:
			newLSize = (math.ceil(160 * koef), 160) 
		resizedLogo = logo.resize(newLSize)
	else:
		resizedLogo = logo

	background = (argv[1], argv[2], argv[3]) #Цвет фона
	textColor = (argv[4], argv[5], argv[6]) 

	#Координаты центра логотипа
	xCent = 1000
	yCent = 400

	#Координаты логотипа
	x = 240 #int(xCent - math.ceil(newLSize[0] / 2))
	y = 215 #int(yCent - math.ceil(newLSize[1] / 2))

	#Задаем цвет фона
	for i in range(widthImg):
		for j in range(heightImg):
			draw.point((i, j), background)

	#Вставляем логотип
	image.paste(resizedLogo, (x, y), resizedLogo)

	#------------------------Работа с текстом
	#Главный текст
	txt = argv[7]
	xText = 1000
	yText = 800
	font_size = 70
	font = ImageFont.truetype('Fonts\\DIN Condensed Bold.ttf', size=font_size)
	w, h = draw.textsize(txt, font=font)
	xt = 450#int(xText - math.ceil(w / 2))
	yt = 215#int(yText - math.ceil(h / 2))
	draw.text((xt, yt), txt, textColor, font=font)

	#Слоган
	txt = argv[8]
	xText = 1000
	yText = 800
	font_size = 36
	font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
	w, h = draw.textsize(txt, font=font)
	xt = 450#int(xText - math.ceil(w / 2))
	yt = 340#int(yText - math.ceil(h / 2))
	draw.text((xt, yt), txt, textColor, font=font)

	#Сайт
	space = 10 #Отступ сверху
	txt = argv[9]
	xText = 1000
	yText = yText + h + space
	font_size = 30
	font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
	w, h = draw.textsize(txt, font=font)
	xt = 395#int(xText - math.ceil(w / 2))
	yt = 530#int(yText - math.ceil(h / 2))
	draw.text((xt, yt), txt, textColor, font=font)

	#Телефон
	space = 10 #Отступ сверху
	txt = ""
	xText = 1000
	yText = yText + h + space
	font_size = 80
	font = ImageFont.truetype('Fonts\\Roboto-Light.ttf', size=font_size)
	w, h = draw.textsize(txt, font=font)
	xt = int(xText - math.ceil(w / 2))
	yt = int(yText - math.ceil(h / 2))
	draw.text((xt, yt), txt, textColor, font=font)

	#Почта
	space = 10 #Отступ сверху
	txt = ""
	xText = 1000
	yText = yText + h + space
	font_size = 80
	font = ImageFont.truetype('Fonts\\Roboto-Light.ttf', size=font_size)
	w, h = draw.textsize(txt, font=font)
	xt = int(xText - math.ceil(w / 2))
	yt = int(yText - math.ceil(h / 2))
	draw.text((xt, yt), txt, textColor, font=font)
	#------------------------Конец работы с текстом

	#Сохраняем результат
	img1 = image.save("Samples\\s1.png", "PNG")
	#-------------------------------------------------------------------------------Sample1 Ends-----------------------------------------------------------------------------
elif inp == 1:
	#-------------------------------------------------------------------------------Sample2-----------------------------------------------------------------------------
	image = Image.open("Samples\\Sample2.png") #Открываем изображение. 
	logo = Image.open("Samples\\bk.png") #Открываем лого. 
	mask = Image.open("Samples\\maskSample2.png")
	icons = Image.open("Samples\\iconsSample2.png")
	drawImg = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
	drawM = ImageDraw.Draw(mask) #Создаем инструмент для рисования. 
	drawIco = ImageDraw.Draw(icons) #Создаем инструмент для рисования. 
	pixM = mask.load()
	pixI = icons.load()

	widthImg = image.size[0] #Определяем ширину карточки. 
	heightImg = image.size[1] #Определяем высоту карточки. 	
	widthLogo = logo.size[0] #Определяем ширину лого. 
	heightLogo = logo.size[1] #Определяем высоту лого.

	koef = float('{:.5f}'.format(widthLogo / heightLogo)) #Коэффицент отношения ширины лого к длине

	#Новые размеры для лого
	if widthLogo > 155 or heightLogo > 160:
		if widthLogo > heightLogo:
			newLSize = (155, math.ceil(155 / koef))  
		else:
			newLSize = (math.ceil(160 * koef), 160) 
		resizedLogo = logo.resize(newLSize)
	else:
		resizedLogo = logo

	background = (argv[1], argv[2], argv[3]) #Цвет фона
	textColor = (argv[4], argv[5], argv[6]) 

	#Координаты центра логотипа
	xCent = 1000
	yCent = 400

	#Координаты логотипа
	x = 780 #int(xCent - math.ceil(newLSize[0] / 2))
	y = 385 #int(yCent - math.ceil(newLSize[1] / 2))

	#Задаем цвет фона
	for i in range(widthImg):
		for j in range(heightImg):
			drawImg.point((i, j), background)

	#Задаем цвет фона
	for i in range(widthImg):
		for j in range(heightImg):
			if pixM[i, j][3] != 0:
				drawM.point((i, j), textColor)

	#Задаем цвет фона
	for i in range(widthImg):
		for j in range(heightImg):
			if pixI[i, j][3] != 0:
				drawIco.point((i, j), background)

	#Вставляем логотип
	image.paste(resizedLogo, (x, y), resizedLogo)
	image.paste(mask, (0, 0), mask)
	image.paste(icons, (0, 0), icons)

	#------------------------Работа с текстом
	#Главный текст
	txt = argv[7]
	xText = 1000
	yText = 800
	font_size = 60
	font = ImageFont.truetype('Fonts\\DIN Condensed Bold.ttf', size=font_size)
	w, h = drawImg.textsize(txt, font=font)
	xt = 870 - w#int(xText - math.ceil(w / 2))
	yt = 50#int(yText - math.ceil(h / 2))
	drawImg.text((xt, yt), txt, textColor, font=font)

	#Слоган
	txt = argv[8]
	xText = 1000
	yText = 800
	font_size = 35
	font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
	w, h = drawImg.textsize(txt, font=font)
	xt = 870 - w#int(xText - math.ceil(w / 2))
	yt = 105#int(yText - math.ceil(h / 2))
	drawImg.text((xt, yt), txt, textColor, font=font)

	#Сайт
	space = 10 #Отступ сверху
	txt = argv[9]
	xText = 1000
	yText = 390
	font_size = 30
	font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
	w, h = drawImg.textsize(txt, font=font)
	xt = 145#int(xText - math.ceil(w / 2))
	yt = int(yText - math.ceil(h / 2))
	drawImg.text((xt, yt), txt, textColor, font=font)

	#Телефон
	space = 10 #Отступ сверху
	txt = argv[10]
	xText = 1000
	yText = 325
	font_size = 30
	font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
	w, h = drawImg.textsize(txt, font=font)
	xt = 145#int(xText - math.ceil(w / 2))
	yt = int(yText - math.ceil(h / 2))
	drawImg.text((xt, yt), txt, textColor, font=font)

	#Почта
	space = 10 #Отступ сверху
	txt = argv[11]
	xText = 1000
	yText = 450
	font_size = 30
	font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
	w, h = drawImg.textsize(txt, font=font)
	xt = 145#int(xText - math.ceil(w / 2))
	yt = int(yText - math.ceil(h / 2))
	drawImg.text((xt, yt), txt, textColor, font=font)
	#------------------------Конец работы с текстом

	#Сохраняем результат
	img1 = image.save("Samples\\s2.png", "PNG")
	#-------------------------------------------------------------------------------Sample2 Ends-----------------------------------------------------------------------------