from PIL import Image

def joinPngHorizontal(name1, name2, verboose = False):
    image1 = Image.open(f'chordsImages/{name1}.png')
    image2 = Image.open(f'chordsImages/{name2}.png')

    image1 = image1.resize((213, 240))
    image2 = image2.resize((213, 240))
    img_size = image1.size
    new_image = Image.new('RGB',(2*img_size[0], img_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(img_size[0],0))
    new_image.save("outputChords/merged_horizontal_image.png","png")
    if verboose:
        new_image.show()

def joinPngVertical(name1, name2, verboose = False):
    image1 = Image.open(f'chordsImages/{name1}.png')
    image2 = Image.open(f'chordsImages/{name2}.png')

    image1 = image1.resize((213, 240))
    image2 = image2.resize((213, 240))
    img_size = image1.size
    new_image = Image.new('RGB',(img_size[0], 2*img_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(0,img_size[1]))
    new_image.save("outputChords/merged_vertical_image.png","png")
    if verboose:
        new_image.show()
    
joinPngVertical("A","A7sus2",verboose=True)