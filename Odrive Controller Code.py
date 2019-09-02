import odrive
from odrive.enums import *
import time
import matplotlib.pyplot as plt

print("using lib at",odrive.__file__)
odrv0 = odrive.find_any()
