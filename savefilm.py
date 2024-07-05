import os
from PIL import Image, ImageDraw, ImageFont
from math import ceil
from makefilm import SCREEN_Y,EXPORT_PATH, FRAME_PATH, SCREEN_X, SCREEN_Y
from vidwrite import vidwrite

FONT_PATH = 'C:\Windows\Fonts\consola.ttf'
FONT_SIZE = 40
offset = 10

def savef(filepath = EXPORT_PATH, folderpath = FRAME_PATH):
   
    #create a font
    if not os.path.exists(FONT_PATH):
        raise FileNotFoundError(f"Font missing: {FONT_PATH}")
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    
    #size of frame(according to character size)
    width = ceil(font.getlength(".") * SCREEN_X + 2 * offset)
    height = ceil(FONT_SIZE * SCREEN_Y + 2 * offset)

    with open(filepath, 'r') as fin:
        #line number
        lnum = 1
        #frame number
        fnum = 1
        
        frame = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(frame)
        
        for line in fin:
                       
            #print(line.strip('\n'))
            draw.multiline_text((offset, offset + FONT_SIZE * (lnum-1)), line, font=font, fill=(255, 255, 255))
            
            if lnum == SCREEN_Y:
                frame.save(f'{folderpath}\\frame{fnum}.png')
                frame = Image.new('RGB', (width, height), (0, 0, 0))
                draw = ImageDraw.Draw(frame)
                lnum = 0
                fnum += 1
            
            lnum += 1
        fin.close()
    print(f"Save ended at frame{fnum-1}.")
    
    print("Writing video...")
    vidwrite()


if __name__ == "__main__":
    savef()