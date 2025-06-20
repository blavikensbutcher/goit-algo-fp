import turtle

def draw_branch(t, branch_length, level):
    if level == 0:
        return


    t.forward(branch_length)


    pos = t.pos()
    heading = t.heading()


    t.left(30)
    draw_branch(t, branch_length * 0.7, level - 1)


    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()


    t.right(30)
    draw_branch(t, branch_length * 0.7, level - 1)


    t.penup()
    t.setpos(pos)
    t.setheading(heading)
    t.pendown()

def main():
    depth = int(input("Введіть рівень рекурсії (наприклад, 9): "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("brown")
    t.left(90) 

    t.penup()
    t.goto(0, -300)
    t.pendown()

    draw_branch(t, 100, depth)

    screen.mainloop()

if __name__ == "__main__":
    main()