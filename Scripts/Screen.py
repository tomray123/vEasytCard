from selenium import webdriver
from PIL import Image, ImageDraw, ImageFont
import copy
import math
import random


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

width, height = 900, 400
options = webdriver.ChromeOptions()
'''options.add_argument('headless')'''
options.add_argument(f'window-size={width},{height}')

driver = webdriver.Chrome('D:\\chromedriver.exe', chrome_options = options)
#  https://burgerking.ru
#  http://nadin.miem.edu.ru
#  https://auto.ru
driver.get('https://auto.ru') 
elements = driver.find_elements_by_tag_name('header')
el_num = 0
for el in elements:
    elements[el_num].screenshot("screenshot" + str(el_num) + ".png")
    el_num += 1
driver.quit()

'''-------------------------------------------------------------------------Вычисление цветов'''
color = list()
colorsNum = list()
for scr in range(el_num):
    img = Image.open("screenshot" + str(scr) + ".png")
    obj = img.load()
    (width, height) = img.size

    width_m = 50
    height_m = 50

    if height != height_m:
        rows = (height // height_m) + 1
    else:
        rows = 1

    if width != width_m:
        cols = (width // width_m) + 1
    else:
        cols = 1

    if height >= height_m:
        fin_row = height % height_m
    else:
        fin_row = height

    if width >= width_m:
        fin_col = width % width_m
    else:
        fin_col = width

    color_m = list()
    color = list()
    count_m = list()
    count = list()
    cube_r = height_m
    cube_c = width_m
    color_num_m = list()
    main_colors_m = list()
    isFirst = True

    for r in range(rows):
        for c in range(cols):
            if r == rows - 1:
                cube_r = fin_row
            else:
                cube_r = height_m
            if c == cols - 1:
                cube_c = fin_col
            else:
                cube_c = width_m
            num = 0
            for i in range(cube_r):
                for j in range(cube_c):
                    if num == 0:
                        color_m.append(obj[j+50*c, i+50*r])
                        count_m.append(1)
                        num += 1
                    else:
                        d = num
                        flag = 0
                        cnt = 0
                        while cnt < d and flag == 0:
                            if color_m[cnt] == obj[j+50*c, i+50*r]:
                                count_m[cnt] += 1
                                flag = 1
                            cnt += 1

                        if flag == 0:       
                            color_m.append(obj[j+50*c, i+50*r])
                            count_m.append(1)
                            num += 1
            
            for a in range(num):
                if isFirst and r == 0 and c == 0 and el_num == 0 and count_m[a] >= 100:
                    color.append(copy.copy(color_m[a]))   #Основные цвета
                    colorsNum.append(copy.copy(count_m[a])) #Количество использований основных цветов
                    isFirst = False
                else:
                    isColor = False
                    sch1 = 0
                    while sch1 < len(color) and not isColor:
                        if math.fabs(color[sch1][0] - color_m[a][0]) <= 30 and math.fabs(color[sch1][1] - color_m[a][1]) <= 30 and math.fabs(color[sch1][2] - color_m[a][2]) <= 30:
                            colorsNum[sch1] += count_m[a]
                            isColor = True
                        sch1 += 1
                    if isColor == False and count_m[a] >= 100:
                        color.append(copy.copy(color_m[a]))   #Основные цвета
                        colorsNum.append(copy.copy(count_m[a])) #Количество использований основных цветов
            
            count_m.clear()
            color_m.clear()

buf = sorted(colorsNum, reverse = True)
maxim = buf[0]
almostMaxim = buf[1]
for i in range(len(color)):
    if colorsNum[i] == maxim:
        maxNum = i
    if colorsNum[i] == almostMaxim:
        almostMaxNum = i
    print(color[i], colorsNum[i])

background = (color[maxNum][0], color[maxNum][1] , color[maxNum][2])
textColor = (color[almostMaxNum][0], color[almostMaxNum][1] , color[almostMaxNum][2])

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

    #background = color #Цвет фона
    #textColor = (argv[4], argv[5], argv[6]) 

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
    txt = "Hello there"
    xText = 1000
    yText = 800
    font_size = 70
    font = ImageFont.truetype('Fonts\\DIN Condensed Bold.ttf', size=font_size)
    w, h = draw.textsize(txt, font=font)
    xt = 450#int(xText - math.ceil(w / 2))
    yt = 215#int(yText - math.ceil(h / 2))
    draw.text((xt, yt), txt, textColor, font=font)

    #Слоган
    txt = "Hello"
    xText = 1000
    yText = 800
    font_size = 36
    font = ImageFont.truetype('Fonts\\trebuc.ttf', size=font_size)
    w, h = draw.textsize(txt, font=font)
    xt = 450#int(xText - math.ceil(w / 2))
    yt = 340#int(yText - math.ceil(h / 2))
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

    #background = (argv[1], argv[2], argv[3]) #Цвет фона
    #textColor = (argv[4], argv[5], argv[6]) 

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
    txt = "Hello there"
    xText = 1000
    yText = 800
    font_size = 60
    font = ImageFont.truetype('Fonts\\DIN Condensed Bold.ttf', size=font_size)
    w, h = drawImg.textsize(txt, font=font)
    xt = 870 - w#int(xText - math.ceil(w / 2))
    yt = 50#int(yText - math.ceil(h / 2))
    drawImg.text((xt, yt), txt, textColor, font=font)

    #Слоган
    txt = "Hello"
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
    txt = "Hello here"
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
    txt = "88005553535"
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
    txt = "mail"
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