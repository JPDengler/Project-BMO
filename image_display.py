import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 320

# Set the path to the directory containing your images and audio
current_directory = os.path.dirname(os.path.realpath(__file__))
image_folder = os.path.join(current_directory, "images")
audio_folder = os.path.join(current_directory, "audio")
loading_folder = os.path.join(image_folder, "loading")

# Get a list of image file names in the loading folder
loading_images = [os.path.join(loading_folder, f"{i}.jpg") for i in range(1, 5)]

# Function to display the loading scene
def display_loading():
    for i, image_path in enumerate(loading_images):
        # Clear the screen
        screen.fill((0, 0, 0))
        # Load and blit the current loading image onto the screen
        image = pygame.image.load(image_path)
        screen.blit(image, (0, 0))
        # Update the display
        pygame.display.flip()
        # Pause for a short duration between each image
        pygame.time.wait(300)  # 500 milliseconds (half a second)

# Function to display the default scene
def display_default():
    # Clear the screen
    screen.fill((0, 0, 0))
    # Load and blit the default image onto the screen
    image_path = os.path.join(image_folder, "default.jpg")
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    # Update the display
    pygame.display.flip()

# Function to display the welcome scene
def display_welcome():
    # Clear the screen
    screen.fill((0, 0, 0))
    # Load and blit the welcome image onto the screen
    image_path = os.path.join(image_folder, "bigsmile.jpg")
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    # Update the display
    pygame.display.flip()

    # Play the welcome sound
    audio_path = os.path.join(audio_folder, "welcomeFriends.mp3")
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    # Wait for a short duration (500 milliseconds)
    pygame.time.wait(6000) 

    # Load and blit the laughing image onto the screen
    image_path = os.path.join(image_folder, "laughing.jpg")
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    # Update the display
    pygame.display.flip()

    # Wait for a short duration (1000 milliseconds)
    pygame.time.wait(2000) 

    # Load and blit the default image onto the screen
    image_path = os.path.join(image_folder, "default.jpg")
    image = pygame.image.load(image_path)
    screen.blit(image, (0, 0))
    # Update the display
    pygame.display.flip()

# Main loop
def main_loop():
    running = True
    welcome_played = False  # Flag to track whether the welcome scene has been played
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Calculate elapsed time
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time

        if elapsed_time < 3000:
            display_loading()
        elif elapsed_time < 6000:  # 3000 + 3000 milliseconds
            display_default()
        else:
            if not welcome_played:
                display_welcome()
                welcome_played = True
            else:
                display_default()
                pygame.time.wait(3000)  # Wait for 3 seconds (3000 milliseconds)

    # Quit Pygame
    pygame.quit()
    sys.exit()
# Set up the display in fullscreen mode
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Image Display")

# Play the startup sound
audio_path = os.path.join(audio_folder, "startUp.mp3")
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

# Get the current time
start_time = pygame.time.get_ticks()

# Start the main loop
main_loop()