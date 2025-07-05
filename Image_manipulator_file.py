from bmp import *

class ImageProcessor:
    def __init__(self, filename):
        self.pixelgrid = ReadBMP(filename)
        self.height = len(self.pixelgrid) #the number of rows
        self.width = len(self.pixelgrid[0]) #the number of columns per row

    def save(self, newName):
        WriteBMP(self.pixelgrid, newName)

    def invert(self):
        for row in range(self.height):
            for col in range(self.width):
                #self.pixelgrid[row][pixel][0] = 255 - self.pixelgrid[row][pixel][0]
                for color in range(3):
                    self.pixelgrid[row][col][color] = 255 - self.pixelgrid[row][col][color]

    def displayChannel(self, Channel):
        for row in range(self.height):
            for col in range(self.width):
                if Channel == 'r':
                    #set green and blue to 0:
                    self.pixelgrid[row][col][1] = 0
                    self.pixelgrid[row][col][2] = 0

                elif Channel == 'g':
                    #set red and blue to 0:
                    self.pixelgrid[row][col][0] = 0
                    self.pixelgrid[row][col][2] = 0

                elif Channel == 'b':
                    #set red and green to 0:
                    self.pixelgrid[row][col][0] = 0
                    self.pixelgrid[row][col][1] = 0

    def flip(self,axis):
        if axis == 'v':
            self.pixelgrid.reverse()
        if axis == 'h':
            for row in self.pixelgrid:
                row = row.reverse()


    def greyscale(self):
         for row in range(self.height):
            for col in range(self.width):
                grey_number = (self.pixelgrid[row][col][0] + self.pixelgrid[row][col][1] + self.pixelgrid[row][col][2]) // 3
                self.pixelgrid[row][col][0] = grey_number
                self.pixelgrid[row][col][1] = grey_number
                self.pixelgrid[row][col][2] = grey_number


    def brightness(self, operation):
        if operation == '+':
            for row in range(self.height):
                for col in range(self.width):
                    for color in range(3):
                        self.pixelgrid[row][col][color] += 25
                        if self.pixelgrid[row][col][color] > 255:
                            self.pixelgrid[row][col][color] = 255

        elif operation == '-':
             for row in range(self.height):
                for col in range(self.width):
                    for color in range(3):
                        self.pixelgrid[row][col][color] -= 25
                        if self.pixelgrid[row][col][color] < 0:
                            self.pixelgrid[row][col][color] = 0




    def contrast(self):
        contrast_answer = input("Would you like to increase or decrease image contrast (press '+' for increase,'-' for decrease, or enter 'q' to end)?")

        while contrast_answer not in ['+', '-', 'q']:
            print("Invalid contrast option.")
            contrast_answer = input("Would you like to increase or decrease image contrast (press '+' for increase,'-' for decrease, or enter 'q' to end)?")

        while contrast_answer != 'q':

            if contrast_answer == '+':
                C = 45
                factor = (259*(C+255))/(255*(259-C))
                for row in range(self.height):
                    for col in range(self.width):
                        for color in range(3):
                            self.pixelgrid[row][col][color] = int(factor*(self.pixelgrid[row][col][color] - 128) + 128)
                            if self.pixelgrid[row][col][color] > 255:
                                self.pixelgrid[row][col][color] = 255
                            elif self.pixelgrid[row][col][color] < 0:
                                self.pixelgrid[row][col][color] = 0

            elif contrast_answer == '-':
                C = -45
                factor = (259*(C+255))/(255*(259-C))
                for row in range(self.height):
                    for col in range(self.width):
                        for color in range(3):
                            self.pixelgrid[row][col][color] = int(factor*(self.pixelgrid[row][col][color] - 128) + 128)
                            if self.pixelgrid[row][col][color] > 255:
                                self.pixelgrid[row][col][color] = 255
                            elif self.pixelgrid[row][col][color] < 0:
                                self.pixelgrid[row][col][color] = 0



            print("Enter additional increases or decreases in contrast or enter 'q' to end.")
            contrast_answer = input("Would you like to increase or decrease image contrast (press '+' for increase or '-' for decrease)?")


def main():
    """Trial run: Cathedral.bmp"""
    picture = input("Enter filename containing source image (must be .bmp): ")
    while picture[-4:] != '.bmp':
        print("The file must be a .bmp file.")
        picture = input("Enter filename containing source image (must be .bmp): ")

    myPicture = ImageProcessor(picture)

    menu = """
    ============================================
            Python Basic Image Processor
    ============================================
    a) Invert Colors
    b) Flip Image
    c) Display color channel
    d) Convert to grayscale
    e) Adjust brightness
    f) Adjust contrast
    s) SAVE current image
    ------------------------
    o) Open new image
    q) Quit
    """

    selection = input(menu)

    while selection not in ('a', 'b', 'c', 'd', 'e', 'f', 's', 'o', 'q'):
        print("Invalid option. Please try again.")
        selection = input(menu)

    while selection in ('a', 'b', 'c', 'd', 'e', 'f', 's', 'o', 'q'):

        if selection == 'a':
            myPicture.invert()
            selection = input(menu)

        elif selection == 'b':
            flip_option = input("Enter 'v' for vertical flip or 'h' for horizontal flip: ")
            while flip_option not in ['v', 'h']:
                print("Invalid flip option.")
                flip_option = input("Enter 'v' for vertical flip or 'h' for horizontal flip: ")
            myPicture.flip(flip_option)
            selection = input(menu)

        elif selection == 'c':
            channel_option = input("Enter 'r' for red, 'g' for green, or 'b' for blue: ")
            while channel_option not in ['r','g','b']:
                print("Invalid channel option.")
                channel_option = input("Enter 'r' for red, 'g' for green, or 'b' for blue: ")
            myPicture.displayChannel(channel_option)
            selection = input(menu)

        elif selection == 'd':
            myPicture.greyscale()
            selection = input(menu)

        elif selection == 'e':

            brightness_option = input("Enter '+' to increase brightness,'-' to decrease brightness, or 'q' to end: ")

            while brightness_option not in ['+','-','q']:
                print("Invalid brightness option.")
                brightness_option = input("Enter '+' to increase brightness,'-' to decrease brightness, or 'q' to end: ")

            while brightness_option != 'q':
                myPicture.brightness(brightness_option)
                print("Enter additional increases or decreases in brightness or enter 'q' to end.")
                brightness_option = input("Enter '+' to increase brightness or '-' to decrease brightness: ")
            selection = input(menu)

        elif selection == 'f':
            myPicture.contrast()
            selection = input(menu)

        elif selection == 's':
            new_name = input("Enter a file name to save the image (must include .bmp): ")
            while new_name[-4:] != ".bmp":
                print("Must be a .bmp file.")
                new_name = input("Enter a file name to save the image (must include .bmp: ")
            myPicture.save(new_name)
            selection = input(menu)

        elif selection == 'o':
            picture = input("Enter filename containing source image (must be .bmp): ")
            while picture[-4:] != '.bmp':
                print("The file must be a .bmp file.")
                picture = input("Enter filename containing source image (must be .bmp): ")
            myPicture = ImageProcessor(picture)
            selection = input(menu)

        elif selection == 'q':
            print("Enjoy your new image.")
            break


if __name__ == "__main__":
    main()
