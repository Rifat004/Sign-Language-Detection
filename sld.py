import tensorflow as tf
config = tf.compat.v1.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.compat.v1.Session(config=config)

import tkinter as tk
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import model_from_json

from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
#load the trained model to classify sign
from tensorflow.keras.models import load_model


json_file = open('sld.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("sld.h5")
loaded_model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


classes = { 0:'A',
            1:'B',
            2:'C', 
            3:'D', 
            4:'E', 
            5:'F', 
            6:'G', 
            7:'H', 
            8:'I',  
            10:'K', 
            11:'L', 
            12:'M', 
            13:'N', 
            14:'O', 
            15:'P', 
            16:'Q', 
            17:'R', 
            18:'S', 
            19:'T', 
            20:'U', 
            21:'V', 
            22:'W', 
            23:'X', 
            24:'Y' 
             
 }

#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Sign Language Detection')
top.configure(background='#5b8ae3')
label=Label(top,background='#5b8ae3', font=('arial',15,'bold'))
sign_image = Label(top)
def classify(file_path):
    global label_packed
    img = Image.open(file_path)
    image=img.resize((28,28))
    image=numpy.asarray(image)/255
    image = numpy.mean(image, axis=2)
    image = numpy.expand_dims(image, axis=2)
    image = numpy.expand_dims(image, axis=0)


    pred = loaded_model.predict_classes([image])[0]
    sign = classes[pred]
    print(sign)
    label.configure(foreground='#000000', text=sign) 
def show_classify_button(file_path):
    classify_b=Button(top,text="Classify Image",command=lambda: classify(file_path),padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload an image",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)
heading = Label(top, text="Sign Language Classification",pady=20, font=('arial',20,'bold'))
heading.configure(background='#5b8ae3',foreground='#364156')
heading.pack()
top.mainloop()