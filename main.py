from PIL import Image
import time
import os

time_1 = 0
time_2 = 0
time_3 = 0
time_4 = 0
time_5 = 0

time_1 = time.time()

filepath = input('Informe o caminho da imagem: ')
limit = int(input('Informe o limite de busca: '))

image_size = os.stat(filepath).st_size / 1024

image, extension = Image.open(filepath), '.%s' % filepath.split('.')[1]

width, height = image.size

replaced_pixels = 0

data = []
colors = []

for x in range(width):
    temp_data = []
    for y in range(height):
        xy = (x, y)
        temp_data.append(image.getpixel(xy))

    data.append(temp_data)

time_2 = time.time()

old_pixel = (-350, -350, -350, 1)

for x in range(width):
    for y in range(height):
        xy = (x, y)
        pixel = data[x][y]

        aux_time_3 = time.time()

        exist_color = False

        for r, g, b in reversed(colors):
            if (pixel[0] > (r - limit) and pixel[0] < (r + limit)) and (
                pixel[1] > (g - limit) and pixel[1] < (g + limit)) and (
                pixel[2] > (b - limit) and pixel[2] < (b + limit)):
                color = (r,g,b)
                image.putpixel(xy, color)
                old_pixel = color
                exist_color = True
                replaced_pixels += 1
                break

        if not exist_color:
            colors.append(pixel)

        time_3 += time.time() - aux_time_3

    print('Linha %d / %d' % (x, width))
time_2 = time.time() - time_2

image.save('images/minified%s' % extension)
time_1 = time.time() - time_1

new_size = os.stat('images/minified%s' % extension).st_size / 1024

print('A imagem diminuiu em %.2f%%' % (100 - 100 * (new_size / image_size)))
print('Foi salvo %d cores' % len(colors))
print('Foi substituido %d pixeis' % replaced_pixels)
print('O programa demorou %.2f minutos' % float(time_1 / 60))
#print('All Put Pixel: %.2f minutos' % float(time_2 / 60))
# print('All Just Put Pixel: %.2f minutos' % float(time_3 / 60))
#print('Find Colors: %.2f minutos' % float(time_3 / 60))
#print('Put Pixel Function: %.2f minutos' % float(time_5 / 60))
