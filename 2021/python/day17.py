"""
input:
target area: x=150..171, y=-129..-70
"""


p1_answer = 0
p2_answer = 0

for DX in range(180):
    for DY in range(-150, 150):

        ok = False

        x = 0
        y = 0
        max_y = 0

        dx = DX
        dy = DY

        for t in range(750):
            x += dx
            y += dy

            if 150 <= x <= 171 and -129 <= y <= -70:
                ok = True

            max_y = max([max_y, y])

            dx -= 1 if dx != 0 else 0
            dy -= 1

        if ok:
            p2_answer += 1

            if max_y > p1_answer:
                p1_answer = max_y

print(p1_answer)
print(p2_answer)
