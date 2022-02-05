
from _init import kbd,mouse
from common.tool import FIX_Waiting, stringTokey
from linuxCMD.loginThing import loopPi

# stringTokey(kbd,"ubuntu\r",FIX_Waiting,0.03)
# time.sleep(1)
# stringTokey(kbd,"d52180362\r",FIX_Waiting,0.02)
# time.sleep(1)
# stringTokey(kbd,"ifconfig\r",FIX_Waiting,0.01)
# time.sleep(1)

loopPi()

# loopSec = 1
# finishSec = 0.2

# while True:
#     time.sleep(loopSec)
#     if not bt1.value:
#         led.value = 0
#         time.sleep(mouseMove1())
#     if not bt2.value:
#         led.value = 1
#         time.sleep(mouseMove2())
#     if not bt3.value:
#         led.value = 0
#         time.sleep(ZED_R_with_escape())
#     if not bt4.value:
#         time.sleep(ZED_escape())


# print(bt1.value,bt2.value,bt3.value,bt4.value)


