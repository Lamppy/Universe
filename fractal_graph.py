import turtle as tl

def fractal_graph(lvl, count):
"""Инструкция"""
    if count==13:
        return lvl
    new_lvl = ''
    for i_c in lvl:
        if i_c =='+':
            new_lvl = new_lvl + '+'
        elif i_c == '-':
            new_lvl = new_lvl +'-'
        elif i_c == 'F':
            new_lvl = new_lvl +'F'
        elif i_c == 'X':
            new_lvl = new_lvl +'X+YF+'
        elif i_c == 'Y':
            new_lvl = new_lvl +'-FX-Y'    
    lvl = new_lvl
    new_lvl = ''
    return fractal_graph(lvl, count+1)
result = fractal_graph('FX', 1)
print(result)
tl.speed(1000000000)
tl.penup()
tl.setx(300)
tl.sety(100)
tl.pendown()
for i_c in result:
    if i_c == '-':
        tl.left(90)
    elif i_c == '+':
        tl.right(90)
    else:
        tl.forward(3)
