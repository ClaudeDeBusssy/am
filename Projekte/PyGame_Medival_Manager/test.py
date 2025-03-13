import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rectangle attributes
RECT_WIDTH = 50
RECT_HEIGHT = 150
RECT1_X = 50
RECT2_X = WIDTH - RECT_WIDTH - 50
RECT_Y = HEIGHT // 2 - RECT_HEIGHT // 2

# Ball attributes
BALL_RADIUS = 10
BALL_SPEED = 5
ball_x = RECT1_X + RECT_WIDTH + BALL_RADIUS
ball_y = HEIGHT // 2
ball_direction = 1  # 1 for moving right, -1 for moving left
ball_moving = False

# Function to draw rectangles and ball
def draw_elements():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (RECT1_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
    pygame.draw.rect(screen, BLUE, (RECT2_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
    if ball_moving:
        pygame.draw.circle(screen, BLACK, (int(ball_x), int(ball_y)), BALL_RADIUS)

# Main game loop
running = True
rect1_clicked = False
rect2_clicked = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if RECT1_X <= mouse_x <= RECT1_X + RECT_WIDTH and RECT_Y <= mouse_y <= RECT_Y + RECT_HEIGHT:
                rect1_clicked = True
            if RECT2_X <= mouse_x <= RECT2_X + RECT_WIDTH and RECT_Y <= mouse_y <= RECT_Y + RECT_HEIGHT:
                rect2_clicked = True

    # Check if both rectangles are clicked
    if rect1_clicked and rect2_clicked:
        ball_moving = True

    # Move the ball
    if ball_moving:
        if ball_direction == 1:
            ball_x += BALL_SPEED
            if ball_x >= RECT2_X - BALL_RADIUS:
                ball_direction = -1
        else:
            ball_x -= BALL_SPEED
            if ball_x <= RECT1_X + RECT_WIDTH + BALL_RADIUS:
                ball_direction = 1

    # Update the screen
    draw_elements()
    pygame.display.flip()

    # Check if the ball goes beyond the rectangles
    if ball_moving and (ball_x + BALL_RADIUS >= WIDTH or ball_x - BALL_RADIUS <= 0):
        ball_moving = False
        rect1_clicked = False
        rect2_clicked = False
        ball_x = RECT1_X + RECT_WIDTH + BALL_RADIUS
        ball_direction = 1

    # Control the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
