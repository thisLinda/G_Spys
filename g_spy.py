# Image Slider code instructed by Codemy.com https://www.youtube.com/watch?v=zg4c92pNFeo
# New learning: root, Tk(), lambda, state (in Python)
# Code works with title page and list of pics separately but not together
# No text associated with pics


from tkinter import *
from tkinter import Button
from tkinter import Label
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('')
root.attributes('-toolwindow', True)
root.geometry('600x600')


#img1 = ImageTk.PhotoImage(Image.open('images/spy_images/poop.jpg'))
'''
labelframe = LabelFrame(root, text='A bag of poop!', font=('Arial', 14, 'bold'),
                        fg='red')

labelframe.grid(row=0, column=0)

left = Label(labelframe, text="Inside the LabelFrame")
left.grid()
'''
make_frame = LabelFrame(root, text='A bag of poop!', width=100, height=100,
                        font=('Arial', 14, 'bold'), fg='red')
make_frame.pack()

stim_filename = 'spy_images/poop.jpg'

PIL_image = Image.open(stim_filename)

width = 100
height = 100

img = ImageTk.PhotoImage(PIL_image)
in_frame = Label(make_frame, image=img)
in_frame.pack()

root.mainloop()

'''
def main():
    title_page()
    pics()



def pics():
    green_frame = Frame(root)
    green_frame.grid()

    frame_canvas = Canvas(green_frame, bg='#234227', width=600, height=600)
    frame_canvas.grid()

    background = PhotoImage(file='images/spy_images/me500.PNG')
    frame_canvas.create_image(300, 300, image=background)

    foreground = PhotoImage(file='images/spy_images/greenspy500.PNG')
    frame_canvas.create_image(300, 300, image=foreground)


pics()

img1 = ImageTk.PhotoImage(Image.open('images/spy_images/poop.jpg'))
img2 = ImageTk.PhotoImage(Image.open('images/spy_images/rainbow.jpg'))
img4 = ImageTk.PhotoImage(Image.open('images/spy_images/pods.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/spy_images/lion.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/spy_images/bike.jpg'))
img7 = ImageTk.PhotoImage(Image.open('images/spy_images/binary.jpg'))
img8 = ImageTk.PhotoImage(Image.open('images/spy_images/boots.jpg'))
img9 = ImageTk.PhotoImage(Image.open('images/spy_images/cornice.jpg'))
img10 = ImageTk.PhotoImage(Image.open('images/spy_images/diner.jpg'))
img11 = ImageTk.PhotoImage(Image.open('images/spy_images/face.jpg'))
img12 = ImageTk.PhotoImage(Image.open('images/spy_images/falcon.jpg'))
img13 = ImageTk.PhotoImage(Image.open('images/spy_images/seedling.jpg'))
img14 = ImageTk.PhotoImage(Image.open('images/spy_images/frieze.jpg'))
img15 = ImageTk.PhotoImage(Image.open('images/spy_images/gcar.jpg'))
img16 = ImageTk.PhotoImage(Image.open('images/spy_images/ghost.jpg'))
img17 = ImageTk.PhotoImage(Image.open('images/spy_images/ghouse.jpg'))
img18 = ImageTk.PhotoImage(Image.open('images/spy_images/interesting.jpg'))
img19 = ImageTk.PhotoImage(Image.open('images/spy_images/ivy.jpg'))
img20 = ImageTk.PhotoImage(Image.open('images/spy_images/ivy2.jpg'))
img21 = ImageTk.PhotoImage(Image.open('images/spy_images/magnolia.jpg'))
img22 = ImageTk.PhotoImage(Image.open('images/spy_images/mural.jpg'))
img23 = ImageTk.PhotoImage(Image.open('images/spy_images/nest.jpg'))
img24 = ImageTk.PhotoImage(Image.open('images/spy_images/outostate.jpg'))
img25 = ImageTk.PhotoImage(Image.open('images/spy_images/phoneuse.jpg'))
img27 = ImageTk.PhotoImage(Image.open('images/spy_images/rubber.jpg'))
img28 = ImageTk.PhotoImage(Image.open('images/spy_images/steeples.jpg'))
img30 = ImageTk.PhotoImage(Image.open('images/spy_images/striped.jpg'))
img31 = ImageTk.PhotoImage(Image.open('images/spy_images/tower.jpg'))
img32 = ImageTk.PhotoImage(Image.open('images/spy_images/tulip.jpg'))
img33 = ImageTk.PhotoImage(Image.open('images/spy_images/weensy.jpg'))
img34 = ImageTk.PhotoImage(Image.open('images/spy_images/wind.jpg'))
img35 = ImageTk.PhotoImage(Image.open('images/spy_images/windows.jpg'))
img36 = ImageTk.PhotoImage(Image.open('images/spy_images/ghouse2.jpg'))
img37 = ImageTk.PhotoImage(Image.open('images/spy_images/wisteria.jpg'))
img38 = ImageTk.PhotoImage(Image.open('images/spy_images/tree.jpg'))
img39 = ImageTk.PhotoImage(Image.open('images/spy_images/roots.jpg'))
img40 = ImageTk.PhotoImage(Image.open('images/spy_images/scary.jpg'))

image_list = [img1, img2, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13,
              img14, img15, img16, img17, img18, img19, img20, img21, img22, img23, img24, img25,
              img27, img28, img30, img31, img32, img33, img34, img35, img36, img37, img38, img39,
              img40]

my_label = Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num-1])
    button_forward = Button(root, text='>>', command=lambda:
                            forward(image_num+1))
    button_back = Button(root, text='<<', command=lambda:
                         back(image_num-1))

    if image_num == 37:
        button_forward = Button(root, text='>>', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


def back(image_num):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num - 1])
    button_forward = Button(root, text='>>', command=lambda:
                            forward(image_num + 1))
    button_back = Button(root, text='<<', command=lambda:
                         back(image_num - 1))

    if image_num == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3, bg='#ede9e8')
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)


button_back = Button(root, text='<<', command=back, state=DISABLED, bg='#d9d5d4',
                     font=('Arial', 14, 'bold'))
button_exit = Button(root, text='Cancel', command=root.quit, bg='#d9d5d4', font=('Arial', 12))
button_forward = Button(root, text='>>', command=lambda: forward(2), bg='#d9d5d4', font=('Arial', 14, 'bold'))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

'''
#root.mainloop()


