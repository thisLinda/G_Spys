from PIL import Image, ImageDraw, ImageFilter


from resizeimage import resizeimage

#with open('C:/Users/linda/Desktop/guis/fauci30.PNG', 'r+b') as f:
with open('images/spy_images/cornice.jpg', 'r+b') as f:

    with Image.open(f) as image:
        cover = resizeimage.resize_cover(image, [600, 600])
        #cover = cover.rotate(90)
        cover.save('images/spy_images/cornice.jpg', image.format)

'''
# checks if an image is RGBA
im = Image.open('images/spy_images/me.png')
print(im.mode)

# converts an rgb.png to rgba, NOTE: can't use jpg
im_rgb = Image.open('images/spy_images/me.PNG')
im_rgba = im_rgb.copy()
# set alpha 0-255, 128 is 50%
im_rgba.putalpha(128)
im_rgba.save('images/spy_images/me.png')
'''