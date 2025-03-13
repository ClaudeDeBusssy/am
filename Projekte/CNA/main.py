import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hex Grid with Camera")

# Define colors
blue = (0, 0, 255)
border_color = (0, 0, 0)  # Black border
background_color = (255, 255, 255)

# Hexagon settings
hex_size = 40  # Base size of the hexagons
hex_height = math.sqrt(3) * hex_size
hex_width = 2 * hex_size

# Camera settings
camera_x, camera_y = 0, 0
zoom_level = 1.0

# Zoom limits
min_zoom = 0.5  # Minimum zoom level
max_zoom = 3.0  # Maximum zoom level

# Function to calculate hexagon vertices
def hexagon_vertices(center, size):
    return [
        (
            center[0] + size * math.cos(math.radians(angle)),
            center[1] + size * math.sin(math.radians(angle))
        )
        for angle in range(0, 360, 60)
    ]

# Function to draw a hexagon grid
def draw_hex_grid():
    for row in range(-10, 10):
        for col in range(-10, 10):
            # Calculate hexagon position
            x = (col * 1.5 * hex_size * zoom_level) + camera_x
            y = (row * hex_height * zoom_level) + (col % 2) * (hex_height / 2 * zoom_level) + camera_y

            # Calculate vertices for the hexagon
            vertices = hexagon_vertices((x, y), hex_size * zoom_level)

            # Draw filled hexagon
            pygame.draw.polygon(screen, blue, vertices)

            # Draw hexagon border
            pygame.draw.polygon(screen, border_color, vertices, width=2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Camera movement with WASD
    if keys[pygame.K_a]:  # Move left
        camera_x += 5
    if keys[pygame.K_d]:  # Move right
        camera_x -= 5
    if keys[pygame.K_w]:  # Move up
        camera_y += 5
    if keys[pygame.K_s]:  # Move down
        camera_y -= 5

    # Zooming in and out (slower zoom)
    if keys[pygame.K_q]:  # Zoom in
        zoom_level *= 1.02  # Slower zoom in
    if keys[pygame.K_e]:  # Zoom out
        zoom_level *= 0.98  # Slower zoom out

    # Clamp zoom level to limits
    zoom_level = max(min_zoom, min(max_zoom, zoom_level))

    # Fill the background
    screen.fill(background_color)

    # Draw the hexagonal grid
    draw_hex_grid()

    # Update the display
    pygame.display.flip()
