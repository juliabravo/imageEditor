from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
pathOut = '/editedImgs'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    
    width_200 = 200
    height_200 = 200

    width_120 = 120
    height_120 = 120

    width_85 = 85
    height_85 = 85

    canvas_size = (300, 200)

    # Resize original image to 200x200 and apply an unsharp mask before saving
    edit1 = img.resize((width_200, height_200), Image.LANCZOS)
    edit1 = edit1.filter(ImageFilter.UnsharpMask(radius=0.5, percent=200, threshold=0))
    clean_name = os.path.splitext(filename)[0]
    edit1.save(f'.{pathOut}/{clean_name}-200.png',quality=95)

    # Resize 200x200 image to 120x120 and apply an unsharp mask before saving
    edit2 = edit1.resize((width_120, height_120), Image.LANCZOS)
    edit2 = edit2.filter(ImageFilter.UnsharpMask(radius=0.6, percent=220, threshold=0))
    clean_name = os.path.splitext(filename)[0]
    edit2.save(f'.{pathOut}/{clean_name}-120.png',quality=95)

    # Resize 120x120 image to 85x85 and apply an unsharp mask before saving
    edit3 = edit2.resize((width_85, height_85), Image.LANCZOS)
    edit3 = edit3.filter(ImageFilter.UnsharpMask(radius=0.7, percent=230, threshold=0))
    clean_name = os.path.splitext(filename)[0]
    edit3.save(f'.{pathOut}/{clean_name}-85.png',quality=95)

    # Create new image with transparent background at 300x200 and paste 200x200 image in the center
    edit4 = Image.new('RGBA', canvas_size, (0,0,0,0))
    offset = ((canvas_size[0] - edit1.width) // 2, (canvas_size[1] - edit1.height) // 2)
    edit4.paste(edit1, offset)
    edit4.save(f'.{pathOut}/{clean_name}-300.png',quality=95)

