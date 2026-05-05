import turtle

screen = turtle.Screen()
screen.title("Dharani's Square Designs")
screen.setup(800, 600)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)
t.pencolor("white")

designs = [
    {"bg": "#1a1a2e", "colors": ["#e94560", "#0f3460", "#533483", "#e94560", "#16213e"]},
    {"bg": "#f9f3e3", "colors": ["#e07a5f", "#3d405b", "#81b29a", "#f2cc8f", "#e07a5f"]},
    {"bg": "#0d0d0d", "colors": ["#00ff88", "#00ccff", "#ff00ff", "#ffff00", "#ff6600"]},
]

SIZE, PAD, COLS, ROWS = 90, 30, 3, 2
grid_w = COLS * SIZE + (COLS - 1) * PAD
grid_h = ROWS * SIZE + (ROWS - 1) * PAD

def draw_square(x, y, color):
    t.penup(); t.goto(x, y); t.pendown()
    t.fillcolor(color); t.begin_fill()
    for _ in range(4):
        t.forward(SIZE); t.right(90)
    t.end_fill()

for design in designs:
    screen.bgcolor(design["bg"])
    t.clear()
    for i, (row, col) in enumerate([(r, c) for r in range(ROWS) for c in range(COLS)]):
        draw_square(
            -(grid_w // 2) + col * (SIZE + PAD),
             (grid_h // 2) - row * (SIZE + PAD),
            design["colors"][i % len(design["colors"])]
        )
    screen.update()

screen.exitonclick()
