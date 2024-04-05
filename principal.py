import pygame
import sys

# Inicializar pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Definir tamaño de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Control de Círculo")

# Definir el círculo
circle_radius = 20
circle_x = WIDTH // 2
circle_y = HEIGHT // 2
circle_speed = 69

clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener las teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento del círculo
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed

    # Asegurar que el círculo aparezca en el lado opuesto si sale de la ventana
    if circle_x > WIDTH:
        circle_x = 0
    elif circle_x < 0:
        circle_x = WIDTH
    if circle_y > HEIGHT:
        circle_y = 0
    elif circle_y < 0:
        circle_y = HEIGHT

    # Dibujar el círculo en su nueva posición
    pygame.draw.circle(screen, BLACK, (circle_x, circle_y), circle_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
