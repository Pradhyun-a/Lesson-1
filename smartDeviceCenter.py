from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def show_device(self):
        print("Device activated.")

    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):
    def turn_on(self):
        print("Light is now ON.")

class SmartFan(SmartDevice):
    def turn_on(self):
        print("Fan is now spinning.")

class SmartSpeaker(SmartDevice):
    def turn_on(self):
        print("Speaker says hello.")

print("=== Abstraction & Inheritance ===")
light = SmartLight()
fan = SmartFan()

light.show_device()
light.turn_on()

fan.show_device()
fan.turn_on()

class SecurityCamera:
    def check_status(self):
        print("Camera: Clear.")

class DoorLock:
    def check_status(self):
        print("Lock: Secured.")

print("\n=== Polymorphism ===")
devices = [SecurityCamera(), DoorLock()]

for d in devices:
    d.check_status()
