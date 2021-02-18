from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

import keras.models
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
import numpy as np
import scipy.misc
import json

CATEGORIES =["Acne-Rosacea", "Basal cell carcinoma"," Hair Loss Alopecia and other Hair Diseases",
             " Herpes"," Melanoma Skin Cancer Nevi and Moles"," Nail Fungus and other Nail Disease","seborrheic-keratoses", " Vasculitis", "Urticaria Hives"," Warts"]
model = load_model('./models/DERMYSOLv2skin_net_frz10_100ep.hdf5')
model.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Create your views here.
def predictimage(request):
    if request.method == 'POST':
        fileobj = request.FILES['filepath']
        fs = FileSystemStorage()
        filePathName=fs.save(fileobj.name,fileobj)
        filePathName = fs.url(filePathName)
        testimage = '.'+filePathName
        img = image.load_img(testimage, target_size=(243, 243))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        images = np.vstack([x])
        classes = model.predict(images)
        maximum = 0.9
        for i, value in enumerate(classes[0]):
            if value > maximum:
                index = i
        prediction = CATEGORIES[index]
        context = {'filePathName':filePathName,'prediction':prediction}
        return render(request, 'uimage/displayimage.html', context)
    else:
        return render(request, 'uimage/upload.html')

