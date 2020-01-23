from PIL import Image

class CaptureScreen:
    def __init__(self, driver):
        self.driver = driver

    def capture(self, element, path):
        location = element.location
        size = element.size
        self.driver.save_screenshot(path)
        x = location['x']
        y = location['y']
        width = location['x'] + size['width']
        height = location['y'] + size['height']
        i = Image.open(path)
        i = i.crop((int(x), int(y), int(width), int(height)))
        i.save(path)