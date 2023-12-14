import PIL.Image as image
import sys

img = image.open(sys.argv[sys.argv.index('--path')+1] if "--path" in sys.argv else "img.png")
img = img.convert('RGB')
img = img.transpose(image.FLIP_TOP_BOTTOM)
x, y = img.size
n = f'import turtle\nt=turtle.Pen()\nt.hideturtle()\nt.speed(0)\nturtle.Screen().colormode(255)\nturtle.setup({x}, {y})\n'
print('open done')
for i in range(x):
    for j in range(y):
        r, g, b = img.getpixel((i, j))
        if [r, g, b] == [255, 255, 255]:
            continue
        n += f't.color({r}, {g}, {b})\n'
        n += 't.penup()\n'
        n += f't.goto({i}, {j})\n'
        n += 't.pendown()\n'
        n += 't.forward(1)\n\n'
        print(i, j, 'done')
n += 'turtle.done()'
open(f'{sys.argv[sys.argv.index("--name")+1] if "--name" in sys.argv else "output"}.py', 'w').write(n)
print('write done')
