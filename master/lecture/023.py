class Car():
    maxpeople = 5
    maxspeed = 300
    def start(self):
        print('차가 출발할였습니다.')
    def stop(self):
        print('차가 멈췄습니다.')
        
class HybridCar(Car):
    battery = 100
    batteryKM = 300

k3 = Car()
print(k3.maxspeed)
k3.start()
print(type(k3))
print(dir(k3))
hyk3 = HybridCar()
print(hyk3.maxspeed)