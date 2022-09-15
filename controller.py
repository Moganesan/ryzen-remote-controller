from pynput.mouse import Controller

mouse = Controller()
mouse.position = [10,200]
print(mouse.position)

