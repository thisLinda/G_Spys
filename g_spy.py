from tkinter import *
from tkinter import Button
from tkinter import Label
from PIL import ImageTk
from PIL import Image

root = Tk()
root.title('')
root.attributes('-toolwindow', True)
root.geometry('620x660+100+0')

text0 = 'I took a walk and spied...'
text1 = 'A bag of poop!'
text2 = 'A rainbow, not in the sky!'
text4 = 'Dangly, weird seed pods.'
text5 = 'A stoney grin.'
text6 = 'A lane just for bikes.'
text7 = 'A different way to count called binary. Just zeros and ones.'
text8 = 'I bet someone\'s feet are cold!'
text9 = 'Fancy cornices.'
text10 = 'Do you recognize this place?'
text11 = 'Someone is hiding.'
text12 = 'The falcons\' home...waaaay in the distance.'
text13 = 'A forest of seedlings.'
text14 = 'A frieze.'
text15 = 'My car.'
text16 = 'A ghoooooost in spring!'
text17 = 'My tower.'
text18 = 'A clever way to add a new building to an old building.'
text19 = 'Ivy without leaves.'
text20 = 'Ivy WITH leaves.'
text21 = 'A magnolia tree.'
text22 = 'A mural.'
text23 = 'A nest.'
text24 = 'A car from out-of-state.'
text25 = 'A phone booth from out-of-this-country!'
text27 = 'Somebody "burned rubber."'
text28 = 'Seven steeple decorations...look closely.'
text30 = 'A striped roof.'
text31 = 'A castle turret? In Manchester? Is it there? Is it real?'
text32 = 'An escaping tulip.'
text33 = 'Is this a toy car?'
text34 = 'Evidence of wind.'
text35 = 'Evidence of where two windows used to be.'
text36 = 'My tower again!'
text37 = 'Wisteria. My favorite.'
text38 = 'Plants will grow anywhere!'
text39 = 'Behold, the power of roots.'
text40 = 'A skull! Is it scary?'
text41 = 'That\'s the end; let\'s take a real walk soon and spy together!'

text_lst = [text0, text1, text2, text4, text5, text6, text7, text8, text9, text10,
            text11, text12, text13, text14, text15, text16, text17, text18, text19,
            text20, text21, text22, text23, text24, text25, text27, text28, text30,
            text31, text32, text33, text34, text35, text36, text37, text38, text39,
            text40, text41]


# return txt to advance text with images
def text(text_num):
    for txt in text_lst:
        return txt


# Tkinter widget LabelFrame provides title area for text
make_frame = LabelFrame(root, text=text(0), width=100, height=100,
                        font=('Arial', 14, 'bold'), fg='red', bd=10)
# grid geometry manager to place text on screen based on rows/columns
make_frame.grid(row=0, column=1, columnspan=5)

# creates Tkinter-compatible photo image
img0 = ImageTk.PhotoImage(Image.open('spy_images/overlay560.PNG'))
img1 = ImageTk.PhotoImage(Image.open('spy_images/poop.jpg'))
img2 = ImageTk.PhotoImage(Image.open('spy_images/rainbow.jpg'))
img4 = ImageTk.PhotoImage(Image.open('spy_images/pods.jpg'))
img5 = ImageTk.PhotoImage(Image.open('spy_images/lion.jpg'))
img6 = ImageTk.PhotoImage(Image.open('spy_images/bike.jpg'))
img7 = ImageTk.PhotoImage(Image.open('spy_images/binary.jpg'))
img8 = ImageTk.PhotoImage(Image.open('spy_images/boots.jpg'))
img9 = ImageTk.PhotoImage(Image.open('spy_images/cornice560.jpg'))
img10 = ImageTk.PhotoImage(Image.open('spy_images/diner.jpg'))
img11 = ImageTk.PhotoImage(Image.open('spy_images/face.jpg'))
img12 = ImageTk.PhotoImage(Image.open('spy_images/falcon.jpg'))
img13 = ImageTk.PhotoImage(Image.open('spy_images/seedling560.jpg'))
img14 = ImageTk.PhotoImage(Image.open('spy_images/frieze.jpg'))
img15 = ImageTk.PhotoImage(Image.open('spy_images/gcar.jpg'))
img16 = ImageTk.PhotoImage(Image.open('spy_images/ghost.jpg'))
img17 = ImageTk.PhotoImage(Image.open('spy_images/ghouse.jpg'))
img18 = ImageTk.PhotoImage(Image.open('spy_images/interesting.jpg'))
img19 = ImageTk.PhotoImage(Image.open('spy_images/ivy.jpg'))
img20 = ImageTk.PhotoImage(Image.open('spy_images/ivy2.jpg'))
img21 = ImageTk.PhotoImage(Image.open('spy_images/magnolia.jpg'))
img22 = ImageTk.PhotoImage(Image.open('spy_images/mural.jpg'))
img23 = ImageTk.PhotoImage(Image.open('spy_images/nest.jpg'))
img24 = ImageTk.PhotoImage(Image.open('spy_images/outostate.jpg'))
img25 = ImageTk.PhotoImage(Image.open('spy_images/phoneuse560.jpg'))
img27 = ImageTk.PhotoImage(Image.open('spy_images/rubber.jpg'))
img28 = ImageTk.PhotoImage(Image.open('spy_images/steeples.jpg'))
img30 = ImageTk.PhotoImage(Image.open('spy_images/striped560.jpg'))
img31 = ImageTk.PhotoImage(Image.open('spy_images/tower.jpg'))
img32 = ImageTk.PhotoImage(Image.open('spy_images/tulip.jpg'))
img33 = ImageTk.PhotoImage(Image.open('spy_images/weensy.jpg'))
img34 = ImageTk.PhotoImage(Image.open('spy_images/wind.jpg'))
img35 = ImageTk.PhotoImage(Image.open('spy_images/windows.jpg'))
img36 = ImageTk.PhotoImage(Image.open('spy_images/ghouse2.jpg'))
img37 = ImageTk.PhotoImage(Image.open('spy_images/wisteria.jpg'))
img38 = ImageTk.PhotoImage(Image.open('spy_images/tree.jpg'))
img39 = ImageTk.PhotoImage(Image.open('spy_images/roots560.jpg'))
img40 = ImageTk.PhotoImage(Image.open('spy_images/scary560.jpg'))
img41 = ImageTk.PhotoImage(Image.open('spy_images/funny560.jpg'))

image_lst = [img0, img1, img2, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13,
             img14, img15, img16, img17, img18, img19, img20, img21, img22, img23, img24, img25,
             img27, img28, img30, img31, img32, img33, img34, img35, img36, img37, img38, img39,
             img40, img41]

make_frame = LabelFrame(root, text=text(0), width=100, height=100,
                        font=('Arial', 14, 'bold'), fg='red', bd=10)
make_frame.grid(row=0, column=1, columnspan=5)

# Tkinter doesn't handle references to images, code creates a reference and attaches to widget attribute
img_filename = 'spy_images/overlay560.PNG'
PIL_image = Image.open(img_filename)
img = ImageTk.PhotoImage(PIL_image)

in_frame = Label(make_frame, image=img)
in_frame.grid(padx=10, pady=10)


# destroys current, recreates new, >> button moves image/text forward
def forward(image_num, txt_num):
    global make_frame
    global in_frame
    global button_back
    global button_forward

    in_frame.destroy()
    make_frame.destroy()

    make_frame = LabelFrame(root, text=text_lst[txt_num], width=100, height=100,
                            font=('Arial', 14, 'bold'), fg='red', bd=10)
    in_frame = Label(make_frame, image=image_lst[image_num])

    button_back = Button(root, text='<<', command=lambda: back(image_num - 1, txt_num - 1), bg='#d9d5d4',
                         font=('Arial', 14, 'bold'))
    button_forward = Button(root, text='>>', command=lambda: forward(image_num + 1, txt_num + 1), bg='#d9d5d4',
                            font=('Arial', 14, 'bold'))

    # disable button to prevent further, inaccurate forward at last image
    if image_num == 38:
        button_forward = Button(root, text='>>', state=DISABLED, bg='#d9d5d4', font=('Arial', 14, 'bold'))

    # grid places on screen, best practice: keep separate from create
    make_frame.grid(row=0, column=1, columnspan=5)
    in_frame.grid(row=0, column=0, columnspan=5)
    in_frame.grid(padx=10, pady=10)

    button_back.grid(row=1, column=1)
    button_forward.grid(row=1, column=5)
    button_back.grid_columnconfigure(0, weight=1)
    button_forward.grid_columnconfigure(4, weight=1)


# destroys current, recreates new, << button moves image/text backward
def back(image_num, txt_num):
    global make_frame
    global in_frame
    global button_back
    global button_forward

    in_frame.destroy()
    make_frame.destroy()

    make_frame = LabelFrame(root, text=text_lst[txt_num], width=100, height=100,
                            font=('Arial', 14, 'bold'), fg='red', bd=10)
    in_frame = Label(make_frame, image=image_lst[image_num])

    button_back = Button(root, text='<<', command=lambda: back(image_num - 1, txt_num - 1), bg='#d9d5d4',
                         font=('Arial', 14, 'bold'))
    button_forward = Button(root, text='>>', command=lambda: forward(image_num + 1, txt_num + 1), bg='#d9d5d4',
                            font=('Arial', 14, 'bold'))

    # disable button to prevent further, inaccurate backward at initial image
    if image_num == 0:
        button_back = Button(root, text='<<', state=DISABLED, bg='#d9d5d4', font=('Arial', 14, 'bold'))

    make_frame.grid(row=0, column=1, columnspan=5)
    in_frame.grid(row=0, column=0, columnspan=5)
    in_frame.grid(padx=10, pady=10)

    button_back.grid(row=1, column=1)
    button_forward.grid(row=1, column=5)
    button_back.grid_columnconfigure(0, weight=1)
    button_forward.grid_columnconfigure(4, weight=1)


# creates initial screen
button_back = Button(root, text='<<', command=back, state=DISABLED, bg='#d9d5d4',
                     font=('Arial', 14, 'bold'))
button_exit = Button(root, text='Cancel', command=root.quit, bg='#d9d5d4', font=('Arial', 12))
button_forward = Button(root, text='>>', command=lambda: forward(1, 1), bg='#d9d5d4', font=('Arial', 14, 'bold'))

button_back.grid(row=1, column=1)
button_exit.grid(row=1, column=3)
button_forward.grid(row=1, column=5)

button_back.grid_columnconfigure(0, weight=1)
button_exit.grid_columnconfigure(2, weight=1)
button_forward.grid_columnconfigure(4, weight=1)

# mainloop code runs/images persist, essentially an infinite loop
root.mainloop()

