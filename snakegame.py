import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Couleurs
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()

# Directions possibles
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_cell(x, y, color):
    """Dessine une cellule à l'écran."""
    pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def random_position():
    """Génère une position aléatoire pour la nourriture."""
    return random.randint(0, COLS - 1), random.randint(0, ROWS - 1)

def main():
    """Boucle principale du jeu."""
    # Initialisation du serpent et de la nourriture
    snake = [(COLS // 2, ROWS // 2)]  # Liste de tuples représentant les segments du serpent
    direction = RIGHT
    food = random_position()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Déplacement du serpent
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])

        # Vérification des collisions
        if (
            new_head in snake or  # Collision avec soi-même
            new_head[0] < 0 or new_head[0] >= COLS or  # Collision avec les murs (horizontal)
            new_head[1] < 0 or new_head[1] >= ROWS  # Collision avec les murs (vertical)
        ):
            print(f"Game Over! Your score: {score}")
            pygame.quit()
            sys.exit()

        # Ajout de la nouvelle tête
        snake.insert(0, new_head)

        # Vérification si la nourriture est mangée
        if new_head == food:
            score += 1
            food = random_position()  # Nouvelle nourriture
        else:
            snake.pop()  # Retire la queue du serpent

        # Dessin de l'écran
        screen.fill(BLACK)

        # Dessiner la nourriture
        draw_cell(food[0], food[1], RED)

        # Dessiner le serpent
        for segment in snake:
            draw_cell(segment[0], segment[1], GREEN)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Contrôler la vitesse
        clock.tick(30)

if __name__ == "__main__":
    main()
