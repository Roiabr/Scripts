from pynotificator import DesktopNotification
import psutil


battery = psutil.sensors_battery()
percentage = battery.percent

dn = DesktopNotification("Your Battery Percentage is: " + str(percentage), title='Battery Percentage')
dn.notify()
