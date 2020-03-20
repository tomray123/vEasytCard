from PIL import Image, ImageDraw 
import copy
import math

img = Image.open("screenshot0.png")
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
color = list()
colorsNum = list()
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
			if isFirst and r == 0 and c == 0 and count_m[a] >= 100:
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

for i in range(len(color)):
	print(color[i], colorsNum[i])



'''
		if r == 0 and c == 0:
			color.append([])
			color[len(color) - 1] = copy.copy(main_colors_m)
			colorsNum.append([])
			colorsNum[len(colorsNum) - 1] = copy.copy(color_num_m)
			count_m.clear()
			color_m.clear()
			color_num_m.clear()
			main_colors_m.clear()
		else:
			isColor = False
			for sch1 in range(len(color)):
				for sch2 in range(len(color[sch1])):
					for sch3 in range(len(color_num_m))
						if color[sch1, sch2] == color_num_m[sch3] and isColor == False:
							count_m.clear()
							color_m.clear()
							color_num_m.clear()
							main_colors_m.clear()
							isColor = True

				if isColor == False:		
					color.append([])
					color[len(color) - 1] = copy.copy(main_colors_m)
					colorsNum.append([])
					colorsNum[len(colorsNum) - 1] = copy.copy(color_num_m)
					count_m.clear()
					color_m.clear()
					color_num_m.clear()
					main_colors_m.clear()



		


num = 0
for i in range(fin_row):
	for j in range(fin_col):
		#print(r, c)
		#print([j+50*c, i+50*r])
		if num == 0:
			color_m.append(obj[j+50*12, i+50])
			count_m.append(1)
			num += 1
		else:
			d = num
			flag = 0

			for cnt in range(d):
				
				if color_m[cnt] == obj[j+50*12, i+50] and flag == 0:
					count_m[cnt] += 1
					flag = 1
			if flag == 0:	
				color_m.append([j+50*12, i+50])
				count_m.append(1)
				num += 1
			
print(count_m)
color.append(color_m)
count.append(count_m)
print(num)

for a in range(num):
	if(count_m[a] >= 200):
		color_num_m.append(count_m[a])   #Основные цвета для маленького квадрата
		main_colors_m.append(color_m[a]) #Количество основных цветов для маленького квадрата'''

#print(color_num)

