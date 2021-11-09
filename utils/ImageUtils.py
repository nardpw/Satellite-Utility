import discord
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
from sklearn.cluster import KMeans

def download_img(att:discord.Attachment, name):
    with open(name, 'wb') as f:
        f.write(att.read())
    return name

def to_int(list):
    return [int(i) for i in list]

def int_to_hex(int):
    return '#%02x%02x%02x' % (int[0], int[1], int[2])

def invert_color(color):
    return [255 - i for i in color]

def get_black(color):
    return 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]

def is_white(color):
    return get_black(color) > 127

def is_black(color):
    return get_black(color) < 127

def get_text_width(text, font):
    font = ImageFont.truetype('arial.ttf', font)
    return font.getsize(text)[0]

def colors_to_image(colors, save_path):
    size = 128
    img = Image.new('RGB', (len(colors)*size, size))
    draw = ImageDraw.Draw(img)
    for i, color in enumerate(colors):
        color_int_arry = to_int(color)
        color = int_to_hex(color_int_arry)
        draw.rectangle([(i * size, 0), (i * size + size, size)] , fill=color)
        text_color = 'black' if is_white(color_int_arry) else 'white'
        draw.text((i * size - int(get_text_width(color, 15) / 2) + size / 2, 4), color, fill=text_color, font=ImageFont.truetype('arial.ttf', 15))
    img.save(save_path)

def extract_main_color(img_path, color_num = 7):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (200, 200))
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    clt = KMeans(n_clusters=color_num)
    clt.fit(img)
    return clt.cluster_centers_

if __name__ == '__main__':
    picked_colors = extract_main_color('5ee5d302ffc990c67f1fe14c34428799.png')
    colors_to_image(picked_colors, 'colors.png')