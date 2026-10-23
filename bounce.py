from tkinter import *
window = Tk()
window.title('My Profile Card')
window.geometry('400x380')
title = Label(window, text = 'My Profile Card', fg='white', bg='purple', width=40)
title.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
name_label = Label(window, text='Name:', fg='black', bg='white')
name_label.grid(row=1, column=0, columnspan=0, padx=10, pady=5)
name_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
name_entry.grid(row=1, column=1, padx=10, pady=5)
hobby_label = Label(window, text='Hobby:', fg='black', bg='white')
hobby_label.grid(row=2, column=0, padx=10, pady=5)
hobby_entry = Entry(window, fg='blue', bg='lightyellow', width=25)
hobby_entry.grid(row=2, column=1, padx=10, pady=5)
about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
about_label = Label(about_frame, text='About Me:')
about_label.pack()
about_text = Text(about_frame, fg='green', bg='lightyellow', width=40, height=4)
about_text.pack()
submit = Button(window, text='Show My Card', bg='purple', fg='white', width=20)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
window.mainloop()
import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')
YELLOW = pygame.Color('yellow')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]
        def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW, MAGENTA, ORANGE, WHITE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE, 20, 30)
sp1.rect.x = random.randint(0, 480)
