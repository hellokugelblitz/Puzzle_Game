# importing required library
import pygame
# Import the os module
import os
#I use PIL and image to read the size of the image before pygame is initilized
from PIL import Image

CWD = os.getcwd()
BACKGROUND = pygame.image.load(CWD+ "/background.jpg")
IMAGE_NAME = "dog.jpg"
img = Image.open(CWD+ "/" + IMAGE_NAME)
img_size_ref = (img.width, img.height)


def clip(surface, x, y, x_size, y_size): #Get a part of the image
    handle_surface = surface.copy() #Sprite that will get process later
    clipRect = pygame.Rect(x,y,x_size,y_size) #Part of the image
    handle_surface.set_clip(clipRect) #Clip or you can call cropped
    image = surface.subsurface(handle_surface.get_clip()) #Get subsurface
    return image.copy() #Return

def draw_image_squares(scrn, image):

    width = int(img_size_ref[1]/50)
    height = int(img_size_ref[0]/50)

    image_data_array = []

    for i in range(height):
        row = []
        for j in range(width):
            current_image = clip(image, i*50, j*50, 50,50)
            row.append([current_image, True])
        image_data_array.append(row)

    return width, height, image_data_array

"""
Main Program Sequence
"""
def main():
    # activate the pygame library .
    pygame.init()

    # set the pygame window name
    pygame.display.set_caption('image puzzle game')


    
    # create the display surface object
    # of specific dimension..e(X, Y).
    scrn = pygame.display.set_mode((img_size_ref[0] + 100, img_size_ref[1] + 100))

    # create a surface object, image is drawn on it.
    image = pygame.image.load(CWD+ "/" + IMAGE_NAME).convert()

    # paint screen one time
    pygame.display.flip()
    status = True
    while (status):
        #First we draw the background
        scrn.blit(BACKGROUND, (0, 0))

        # Using blit to copy content from one surface to other
        # scrn.blit(image, (50, 50))

        width, height, images = draw_image_squares(scrn, image)
        images[4][1][1] = False

        for i in range(height):
            for j in range(width):

                current_image_tuple = images[i][j]
                current_image = current_image_tuple[0]
                
                if current_image_tuple[1] == True:
                    scrn.blit(current_image, (50 + (i*51),50 + (j*51)))
                

        

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for i in pygame.event.get():
            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if i.type == pygame.QUIT:
                status = False
        
        pygame.display.update()
    
    # deactivates the pygame library
    pygame.quit()


main()