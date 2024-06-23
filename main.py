import pygame
from table.cell import Cell
from table.row import Row
from table.table import Table
from table_seeder import TableSeeder

WIDTH, HEIGHT = 700, 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    seeder = TableSeeder()
    table = seeder.generateTable(order_col="price")
   
    table.draw(0,0,screen)
    
    pygame.display.flip()