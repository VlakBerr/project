import pygame
from table.cell import Cell
from table.row import Row
from table.table import Table
WIDTH, HEIGHT = 700, 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    cell = Cell(size=200,text= "1",font_size= 25)
    cell2 = Cell(size=200,text= "2",font_size= 25)
    cell3 = Cell(size=200,text= "3",font_size= 25)
    row = Row([cell, cell2, cell3], 35)
    row2 = Row([cell2, cell3, cell], 35)
    table = Table([row, row2], 35)
    table.draw(0, 0, screen)
    pygame.display.flip()