import platform
from turtle import *
from datetime import *
from time import sleep

from getpass import getuser

title('Ready to Code')
print('You did it!')

ht()
setup(200 * 4, 100 * 4)

color('blue')


up()
goto(-100, 150)
down()

py_version = platform.python_version()
write('Python Version: ' + py_version, font=('Arial 20'), align="right")


write('\n\n ' + platform.platform(), font=("times 15"), align="Left")

up()
home()
down()

color('black')

user = getuser().capitalize()
greeting = 'Hi ' + user + '! You did it!\nNow you are ready for class!'

write(greeting, font="Times 30", align="Center")

color('red')

up()
goto(300, -150)
down()

duration = 0

try:
    while True:
        if duration > 10:
            break

        now = datetime.now()

        time_str = now.strftime("%Y-%m-%d\n    %H:%M:%S")
        write(time_str, align="right", font='Times 15')

        undo()
        sleep(1)
        duration += 1

except Exception:
    pass
