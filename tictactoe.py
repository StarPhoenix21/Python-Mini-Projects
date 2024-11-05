import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
canvas_width=300
canvas_height=300
grid=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
turn='X'
won=False
def switch_turn():
    global turn,info
    if turn=='X':
        turn='O'
    else:
        turn='X'
    info.set_text('Player turn: '+ turn)
def check_win():
    for a in range(0,3):
        if grid[a][0]!=' ' and grid[a][0]==grid[a][1]==grid[a][2]:
            return True
    for b in range(0,3):
        if grid[0][b]!=' ' and grid[0][b]==grid[1][b]==grid[2][b]:
            return True
    if grid[0][0]== grid [1][1]== grid[2][2] and grid[0][0]!=' ':
        return True
    if grid[0][2]== grid [1][1]== grid[2][0] and grid[0][2]!=' ':
        return True
    else:
        return False
def mouseclick(pos):
    global won,info
    if not won:
        r=pos[1]//(canvas_height//3)
        c=pos[0]//(canvas_width//3)
        if grid[r][c]==" ":
            grid[r][c]=turn
            if check_win():
                won=True
                info.set_text('Player '+turn+' wins!')
            else:
                switch_turn()
def draw(canvas):
    global color
#     canvas.draw_line((100,0),(100,300),8,'white')
#     canvas.draw_line((200,0),(200,300),8,'white')
#     canvas.draw_line((0,100),(300,100),8,'white')
#     canvas.draw_line((0,200),(300,200),8,'white')
    canvas.draw_line([0,canvas_height//3],[canvas_width,canvas_height//3],1,'white')
    canvas.draw_line([0,canvas_height//3*2],[canvas_width,canvas_height//3*2],1,'white')
    canvas.draw_line([canvas_width//3,0],[canvas_width//3,canvas_height],1,'white')
    canvas.draw_line([canvas_width//3*2,0],[canvas_width//3*2,canvas_height],1,'white')
    for r in range(0,3):
        for c in range(0,3):
            if grid[r][c]=='X':
                canvas.draw_text(grid[r][c],[c*canvas_width//3+20,r*canvas_height//3+80],80,'yellow')
            else:
                canvas.draw_text(grid[r][c],[c*canvas_width//3+20,r*canvas_height//3+80],80,'pink')

frame=simplegui.create_frame('Tic Tac Toe',canvas_width,canvas_height)
frame.set_draw_handler(draw)
info=frame.add_label('Player turn: '+turn)
frame.set_mouseclick_handler(mouseclick)
frame.start()