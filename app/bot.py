import lackey
from lackey import *
from keyboard import mouse

# как проверить введина ли позиция комбо? ( надпись комбо-обед )

# при запуске скрипта
# делаем фокус на iikoFront
# забиваем комбо-обед
# перешли в роежим ожидания

# делаем фокус на ikkoFront
path = '"C:\\Program Files\\Krita (x64)\\bin\\krita.exe"'
e = lackey.App(path)

# делаем фокус на ikkoFront
lackey.App('krita').focus()
while True:
# (1) забиваем комбо-обед
# экраны - комбо
# добавить проверки
# уменьшить зону поиска
    click("img/add.png")
    click("img/add.png")
    click("img/add.png")
    click("img/add.png")

# (2) перешли в режим ожидания, ждем запрос по api
    click("img/pay1.png")
    click("img/pay2.png")
    click("img/pay3.png")
    click("img/pay4.png")

# после того как оплата прошла преходим на шаг (1)

