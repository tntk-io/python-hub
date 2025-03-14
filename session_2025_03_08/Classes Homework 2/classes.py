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

    @property
    def average_resolution(self):
        if not self.list_of_cameras:
            return 0

        total_res = 0
        count = 0

        for camera in self.list_of_cameras:
            total_res += camera.resolution
            count += 1

        return total_res / count


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

### Task 1
highest_res_camera = max(phones, key=lambda p: p.highest_res())
print(f'Phone with the highest resolution camera: {highest_res_camera.name} ({highest_res_camera.highest_res()} MP)')

### Task 2
phones_with_jack = []
for phone in phones:
    if phone.has_jack == True:
        phones_with_jack.append(phone.name)
print(f'Phones with a jack: {phones_with_jack}')

### Task 3
for phone in phones:
    if phone.markets:
        string_markets = ', '.join(phone.markets)
        print(f'{phone.name} - {string_markets}')
    else:
        print(f'{phone.name} - N/A')

### Task 4
for phone in phones:
    print(f'{phone.name} - Average Camera Resolution: {phone.average_resolution:.2f} MP')

### Task 5
operating_systems = []
count = 0
for phone in phones:
    if phone.os not in operating_systems:
        operating_systems.append(phone.os)
        count += 1
print(f'The amount of different operating system is - {count}')

### Task 6
strongest_battery_phone = phones[0]
for phone in phones:
    if phone.battery > strongest_battery_phone.battery:
        strongest_battery_phone = phone

print(f'The phone with the strongest battery is {strongest_battery_phone.name} with {strongest_battery_phone.battery}mAh')

### Task 7
phones_without_widevine_l1 = []
for phone in phones:
    if phone.widevine_level != 'L1':
        phones_without_widevine_l1.append(phone.name)
print(f'Phones without WideVine level L1: {phones_without_widevine_l1}')
