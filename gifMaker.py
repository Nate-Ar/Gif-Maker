from PIL import Image
import time
import os
i = 0
t = 0
askfor = input("What is the file path to the forground image$ ")
back1 = input("What is the file path to the background image$ ")
try:
    ximage = Image.open(askfor)
    back = Image.open(back1)
except:
     print('That is not a compatible file')
     exit()
area = (275,275)
fitx = ximage.resize((250,250))
back.paste(fitx, area)
while i != 360:
    i = i + 40
    print(i)
    t = t + 1
    back.rotate(i).save('{}Background.png'.format(t))
time.sleep(5)
os.system('convert -delay 10 -loop 1 *.png -scale 800x800 Done.gif')
os.system('rm *.png')
try:
     os.system('open Done.gif')
except:
     print('done')