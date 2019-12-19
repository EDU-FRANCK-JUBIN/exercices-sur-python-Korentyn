import turtle as tu

def carre(long):
    for i in range(2):
        tu.fd(long)
        tu.left(90)
        tu.fd(long)
        tu.left(90)

def triangle(long):
    tu.color('green')
    for i in range(1):
        tu.left(120)
        tu.fd(long)
        tu.left(120)
        tu.fd(long)
        tu.left(120)
        tu.fd(long)


tu.color('red')
carre(40)

tu.color('black')
tu.fd(60)
tu.left(90)
carre(80)

tu.fd(80)
tu.right(90)
triangle(80)
