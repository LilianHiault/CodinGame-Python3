# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
x = initial_tx
y = initial_ty
# print(light_x, light_y, initial_tx, initial_ty)
# game loop
while True:
    # The remaining amount of turns Thor can move. Do not remove this line.
    remaining_turns = int(input())
    while (x != light_x) or (y != light_y):
        direction = ""
        if y > light_y and y > 0:
            direction += "N"
            y -= 1
        if y < light_y and y < 17:
            direction += "S"
            y += 1
        if x > light_x and x > 0:
            direction += "W"
            x -= 1
        if x < light_x and x < 39:
            direction += "E"
            x += 1
        print(direction)
