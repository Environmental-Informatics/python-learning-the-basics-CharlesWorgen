#!/usr/bin/env python3
"""
2020/1/24
by Charles Huang

ThinkPython2e - Excercise 3.3
This program contains functions to create grids of 2x2 and 4x4


"""
# The function used to draw horizontal lines of the 2x2 grid
def draw_horiline2():
    print('+','- '*4,end='')
    print('+','- '*4,end='')
    print('+')

# The function used to draw vertical lines of the 2x2 grid   
def draw_vertline2():
    print('|','  '*4,end='')
    print('|','  '*4,end='')
    print('|')
 
# The function used to draw horizontal lines of the 4x4 grid
def draw_horiline4():
    print('+','- '*4,end='')
    print('+','- '*4,end='')
    print('+','- '*4,end='')
    print('+','- '*4,end='')
    print('+')

# The function used to draw vertical lines of the 4x4 grid   
def draw_vertline4():
    print('|','  '*4,end='')
    print('|','  '*4,end='')
    print('|','  '*4,end='')
    print('|','  '*4,end='')
    print('|')
    
# The function to repeat assigned function four times
def do_four(f):
    f()
    f()
    f()
    f()
    
#### Result    
# The function to draw a 2 x 2 grid
def draw_2x2grid():
    draw_horiline2()
    do_four(draw_vertline2)
    draw_horiline2()
    do_four(draw_vertline2)
    draw_horiline2()
    
# The function to draw a 4 x 4 grid
def draw_4x4grid():
    draw_horiline4()
    do_four(draw_vertline4)
    draw_horiline4()
    do_four(draw_vertline4)
    draw_horiline4()
    do_four(draw_vertline4)
    draw_horiline4()
    do_four(draw_vertline4)
    draw_horiline4()

#### Test
draw_2x2grid()
draw_4x4grid()  