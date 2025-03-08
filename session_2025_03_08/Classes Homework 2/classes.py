from typing import List


class Camera:
    def __init__(self, resolution, type, f_number=None):
        self.resolution = resolution
        self.camera_type = type
        self.f_number = f_number


class Display:
    def __init__(self, size, type):
        self.size = size
        self.type = type


class Phone:
    def __init__(self, name, list_of_cameras: List[Camera], display, os,
                 has_jack, battery, widevine_level=None, markets=None):
        self.name = name
        self.list_of_cameras = list_of_cameras
        self.display = display
        self.os = os
        self.has_jack = has_jack
        self.battery = battery
        self.widevine_level = widevine_level
        if markets:
            self.markets = markets
        else:
            self.markets = []

    def highest_res(self):
        return max(c.resolution for c in self.list_of_cameras)


samsung = Phone(
    name='Samsung Galaxy S25 Ultra',
    list_of_cameras=[
        Camera(resolution=200, type='wide', f_number=1.7),
        Camera(resolution=10, type='telephoto', f_number=2.4),
        Camera(resolution=50, type='periscope telephoto', f_number=3.4),
        Camera(resolution=50, type='ultrawide', f_number=1.9)
    ],
    display=Display(size=6.9, type='AMOLED'),
    os='Android',
    has_jack=False,
    battery=5000,
    widevine_level='L1',
    markets=['World']
)

iphone = Phone(
    name='Apple iPhone 16 Pro Max',
    list_of_cameras=[
        Camera(resolution=48, type='wide', f_number=1.8),
        Camera(resolution=12, type='periscope telephoto', f_number=2.8),
        Camera(resolution=48, type='ultrawide', f_number=2.2),
    ],
    display=Display(size=6.9, type='OLED'),
    os='iOS',
    has_jack=False,
    battery=4685,
    widevine_level='L1',
    markets=['World']
)

honor = Phone(
    name='Honor Magic V3',
    list_of_cameras=[
        Camera(resolution=50, type='wide'),
        Camera(resolution=50, type='periscope telephoto'),
        Camera(resolution=40, type='ultrawide'),
    ],
    display=Display(size=7.92, type='AMOLED'),
    os='Android',
    has_jack=False,
    battery=5150,
    markets=['World']
)

oppo = Phone(
    name='Oppo Find N5',
    list_of_cameras=[
        Camera(resolution=50, type='wide'),
        Camera(resolution=50, type='periscope telephoto'),
        Camera(resolution=8, type='ultrawide'),
    ],
    display=Display(size=8.12, type='OLED'),
    os='Android',
    has_jack=False,
    battery=5600,
    markets=['India']
)

asus = Phone(
    name='Asus ROG Phone 8',
    list_of_cameras=[
        Camera(resolution=50, type='wide'),
        Camera(resolution=32, type='telephoto'),
        Camera(resolution=13, type='ultrawide'),
    ],
    display=Display(size=8.12, type='OLED'),
    os='Android',
    has_jack=True,
    battery=5500,
)

phones = [samsung, iphone, honor, oppo, asus]

highest_res_camera = max(phones, key=lambda p: p.highest_res())
print(f'Phone with the highest resolution camera: {highest_res_camera.name} ({highest_res_camera.highest_res()} MP)')
