import turtle
def up():
    old_pos = turtle.pos()
    x = old_pos[0]
    y = old_pos[1]
    turtle.goto(x, y+10)
    print(turtle.pos())
turtle.mainloop()
