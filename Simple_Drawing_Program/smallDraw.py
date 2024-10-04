import pygame

pygame.init()

width = 800
height = 800

screen = pygame.display.set_mode((width, height))

player = pygame.Rect((300, 250, 50, 50))

colors = {
    pygame.K_r: (255, 0, 0),    # Red
    pygame.K_g: (0, 255, 0),    # Green
    pygame.K_b: (0, 0, 255),    # Blue
    pygame.K_c: (0, 255, 255),  # Cyan
    pygame.K_m: (255, 0, 255),  # Magenta
    pygame.K_y: (255, 255, 0),  # Yellow
    pygame.K_o: (255, 100, 0),  # Orange
    pygame.K_w: (255, 255, 255) # White
}

def drawText():
    size_text = font.render(f"Size: {player.width}", True, (255, 255, 255))  # White text
    text_rect = size_text.get_rect()
    text_rect.topleft = (10, 10)
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect((5, 5, text_rect.width + 10, text_rect.height + 10)))
    pygame.draw.rect(screen, (255, 255, 255), text_rect.inflate(10, 10), 2)  # White outline
    screen.blit(size_text, text_rect)

curr = colors[pygame.K_r]
font = pygame.font.SysFont(None, 36)  # Default system font
run = True
while run:
    mousex, mousey = pygame.mouse.get_pos()
    player.x, player.y = mousex - player.width/2, mousey - player.height/2

    if pygame.mouse.get_pressed()[0]: #left click to draw
        pygame.draw.rect(screen, curr, player)
    if pygame.mouse.get_pressed()[1]:
        pygame.draw.rect(screen, (0,0,0), player)
    if pygame.mouse.get_pressed()[2]: #right click to clear screen
        screen.fill((0, 0, 0))

    drawText()

    key = pygame.key.get_pressed()
    for type in colors:
        if key[type]:
            curr = colors[type]

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check for window close event
            run = False
        if event.type == pygame.MOUSEWHEEL:  # Check for window close event

            if event.y == -1:
                if player.width > 10:
                    player.width -= 10
                    player.height -= 10
            elif event.y == 1:
                if player.width < 250:
                    player.width += 10
                    player.height += 10

pygame.quit()