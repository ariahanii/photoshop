from PIL import Image, ImageFilter
import os
import tkinter.filedialog

def ToIco()->None:
    file_path = tkinter.filedialog.askopenfilename()
    f, e = os.path.splitext(file_path)
    try:
        with Image.open(file_path) as im:
            im.save(f + ".ico")
            print(f)
    except:
        f"unable to convert {file_path}"