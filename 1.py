class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension
        
    def resize(self, res):
        self.resolution = res
        

image_1 = Image('1280x720', "image 1", '.JPG')
image_1.resize('600x400')
print(image_1.resolution)

image_2 = Image('1080x1080', "image 2", '.PNG')
image_2.resize('900x700')
print(image_2.resolution)

