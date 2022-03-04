import turtle as tl

def fractal_graph(lvl, count):
    """[summary]

    Args:
        lvl ([type]): [description]
        count ([type]): [description]

    Returns:
        [type]: [description]
    """
    if count==13:
        return lvl
    new_lvl = ''
    for i_c1 in lvl:
        if i_c1 =='+':
            new_lvl = new_lvl + '+'
        elif i_c1 == '-':
            new_lvl = new_lvl +'-'
        elif i_c1 == 'F':
            new_lvl = new_lvl +'F'
        elif i_c1 == 'X':
            new_lvl = new_lvl +'X+YF+'
        elif i_c1 == 'Y':
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
