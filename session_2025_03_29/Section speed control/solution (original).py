from dataclasses import dataclass
import datetime as dt


class Vehicle:
    distance = 10

    def __init__(self, data):
        data = data.split()
        self.license_plate = data[0]
        self.entry = dt.timedelta(hours=int(data[1]), minutes=int(data[2]), seconds=int(data[3]),
                                  milliseconds=int(data[4]))
        self.exit = dt.timedelta(hours=int(data[5]), minutes=int(data[6]), seconds=int(data[7]),
                                 milliseconds=int(data[8]))

    @property
    def entry_datetime(self):
        return dt.datetime(1, 1, 1) + self.entry

    @property
    def exit_datetime(self):
        return dt.datetime(1, 1, 1) + self.exit

    @property
    def speed(self):
        one_hour = dt.timedelta(hours=1)
        return one_hour / (self.exit - self.entry) * Vehicle.distance


print('Exercise 1.')
vehicles = []
with open('measurements.txt') as file:
    for line in file:
        vehicles.append(Vehicle(line))

print('Exercise 2.')
print(f'{len(vehicles)} vehicles were recorded')

print('Exercise 3.')
number_of_vehicles_before_9 = sum(1 for v in vehicles if v.exit < dt.timedelta(hours=9))
print(f'{number_of_vehicles_before_9} vehicles passed the exit before 9.')

print('Exercise 4.')
# time = input('Specify a time (HH:MM): ')
# hours, minutes = map(int, time.split(':'))
hours, minutes = 8, 20

vehicles_entering_at_time = [v for v in vehicles if
                             v.entry_datetime.hour == hours and v.entry_datetime.minute == minutes]
vehicles_present_at_time = [v for v in vehicles if
                            (v.entry_datetime.hour <= hours and v.entry_datetime.minute <= minutes)
                            and
                            (v.exit_datetime.hour >= hours and v.exit_datetime.minute >= minutes)]
print(f'At {hours}:{minutes} {len(vehicles_entering_at_time)} vehicles passed the entry gate.')
print(f'Traffic density: {len(vehicles_present_at_time) / 10}')

print('Exercise 5.')
fastest_vehicle = max(vehicles, key=lambda v: v.speed)
number_of_cars_overtaken = sum(1 for v in vehicles if v.entry < fastest_vehicle.entry and v.exit > fastest_vehicle.exit)
print(
    f'Fastest car: {fastest_vehicle.license_plate}, {int(fastest_vehicle.speed)} km/h, {number_of_cars_overtaken} vehicles overtaken')

print('Exercise 6.')
exceeding_limit = sum(1 for v in vehicles if v.speed > 90)
print(f'{exceeding_limit / len(vehicles) * 100:.2f}% vehicles exceeded the speed limit.')

print('Exercise 7.')
with open('fines.txt', 'w') as file:
    speeding_vehicles = [v for v in vehicles if v.speed > 104]
    for v in speeding_vehicles:
        fine = 0
        if v.speed < 121:
            fine = 30_000
        elif v.speed < 136:
            fine = 45_000
        elif v.speed < 151:
            fine = 60_000
        else:
            fine = 200_000
        # Since the police works with integers
        file.write(f'{v.license_plate}\t{int(v.speed)} km/h\t{fine} Ft\n')
