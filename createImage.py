from PIL import Image
import numpy as np

def joinHorizontal(chordsArray, row_number):
    imgs = [Image.open(f"chordsImages/{elem}.png") for elem in chordsArray]
    min_shape = sorted([(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack(np.asarray(i.resize(min_shape)) for i in imgs)
    imgs_comb = Image.fromarray(imgs_comb)
    imgs_comb.save(f"tempChords/{row_number}.png")    

def joinVertical(number_of_rows, name):
    imgs = [Image.open(f"tempChords/{elem}.png") for elem in range(number_of_rows)]
    min_shape = sorted([(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.vstack((np.asarray(i.resize(min_shape)) for i in imgs))
    imgs_comb = Image.fromarray( imgs_comb)
    imgs_comb.save(f"outputChords/{name}.png")    

chords = ['A', 'A6', 'A7', 'A9']
for i in range(4):
    joinHorizontal(chords, i)
joinVertical(4, "test")