import PIL
from PIL import Image
im = PIL.Image.open('PaintedImage.jpg', 'r')
pix_values = list(im.getdata())
better_pixel_list = []

output_im = PIL.Image.new(mode="RGB", size=(im.width,im.height))

for i in range(0, im.height):
    new_layer = []
    for j in range(0, im.width):
        pix_data = (i * im.width) + j             
        new_layer.append([pix_values[pix_data][0], pix_values[pix_data][1], pix_values[pix_data][2]])
    better_pixel_list.append(new_layer)

def getPixelColorDifference(pix1, pix2):
    return abs((pix1[0]-pix2[0])+(pix1[1]-pix2[1])+(pix1[2]-pix2[2]))

def simplifyImagePixelColoration(img_pixel_data, avg_pix_diff_thres):
    for i in range(0, len(img_pixel_data)):
        for j in range(0, len(img_pixel_data[0])):

            cur_data = img_pix_data[i][j]
            if i > 0: 
                target_data = img_pixel_data[i-1][j]
                if getPixelColorDifference(cur_data, target_data) < avg_pix_diff_thres:
                    averages = ((cur_data[0] + target_data[0]) / 2, (cur_data[1] + target_data[1]) / 2, (cur_data[2] + target_data[2]) / 2)
                    cur_data[0] = averages[0]
                    cur_data[1] = averages[1]
                    cur_data[2] = averages[2]


im.show()
