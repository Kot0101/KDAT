import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cube_x = WIDTH // 2
cube_y = HEIGHT // 2
size = 100
speed = 10

dragging = False

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # палец на телефоне
        elif event.type == pygame.FINGERDOWN:
            dragging = True

        elif event.type == pygame.FINGERUP:
            dragging = False

        elif event.type == pygame.FINGERMOTION and dragging:
            cube_x = int(event.x * WIDTH)
            cube_y = int(event.y * HEIGHT)

        # мышка
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        elif event.type == pygame.MOUSEMOTION and dragging:
            cube_x, cube_y = event.pos

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        cube_x -= speed
    if keys[pygame.K_d]:
        cube_x += speed
    if keys[pygame.K_w]:
        cube_y -= speed
    if keys[pygame.K_s]:
        cube_y += speed

    screen.fill((20, 20, 20))

    pygame.draw.rect(
        screen,
        (255, 0, 0),
        (cube_x - size // 2,
         cube_y - size // 2,
         size,
         size)
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()   