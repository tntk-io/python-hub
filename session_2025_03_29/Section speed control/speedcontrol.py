from datetime import datetime, timedelta
from typing import List


class Vehicle:
    distance = 10

    def __init__(self, license_plate,
                 entry_hour, entry_min, entry_sec, entry_mil,
                 exit_hour, exit_min, exit_sec, exit_mil):
        self.license_plate = license_plate
        self.entry = timedelta(hours=int(entry_hour), minutes=int(entry_min), seconds=int(entry_sec),
                               milliseconds=int(entry_mil))
        self.exit = timedelta(hours=int(exit_hour), minutes=int(exit_min), seconds=int(exit_sec),
                              milliseconds=int(exit_mil))

    @property
    def entry_datetime(self):
        return datetime(1, 1, 1) + self.entry

    @property
    def exit_datetime(self):
        return datetime(1, 1, 1) + self.exit

    @property
    def average_speed(self):
        return 3600 / (self.exit - self.entry).total_seconds() * Vehicle.distance


vehicles: List[Vehicle] = []

with open('measurements.txt') as file:
    for line in file:
        vehicles.append(Vehicle(*line.split()))

print('Exercise 2')
print(f'Number of vehicles: {len(vehicles)}')

print('Exercise 3')
print(f'Number of vehicles that passed before 9 o\'clock {sum(1 for v in vehicles if v.exit_datetime.hour < 9)}')

print('Exercise 4/a')
hour, minute = 8, 20
# hour, minute = map(int, input('Enter the hour and the minute in the given format (HH:MM): ').split(':'))
print(
    f'Number of vehicles that passed at {str(hour).zfill(2)}:{str(minute).zfill(2)} is '
    f'{sum(1 for v in vehicles if v.entry_datetime.hour == hour and v.entry_datetime.minute == minute)}')

print('Exercise 4/b')
density = sum(1 for v in vehicles if
              (v.entry_datetime.hour <= hour and v.entry_datetime.minute <= minute) and
              (v.exit_datetime.hour >= hour and v.exit_datetime.minute >= minute)) / Vehicle.distance
print(f'The traffic intensity is {density}')

print('Exercise 5')
fastest = max(vehicles, key=lambda v: v.average_speed)
print('The data of the vehicle with the highest speed are')
print(f'\t\tlicense plate number: {fastest.license_plate}')
print(f'\t\taverage speed: {int(fastest.average_speed)} km/h')
print(
    f'\t\tnumber of overtaken vehicles: {sum(1 for v in vehicles if v.entry < fastest.entry and v.exit > fastest.exit)}')
print(fastest.license_plate)

print('Exercise 6')
total_speeding = sum(1 for v in vehicles if v.average_speed > 90)
print(f'{total_speeding / len(vehicles) * 100:.2f}% percent of the vehicles were speeding. ')

print('Exercise 7')
speeding_vehicles = [v for v in vehicles if v.average_speed > 104]
with open('fines.txt', 'w') as file:
    fine = 0
    for v in speeding_vehicles:
        if 104 < v.average_speed <= 121:
            fine = 30_000
        elif 121 < v.average_speed <= 136:
            fine = 45_000
        elif 136 < v.average_speed <= 151:
            fine = 60_000
        else:
            fine = 200_000
        file.write(f'{v.license_plate}\t{int(v.average_speed)} km/h\t\t{fine} Ft\n')
