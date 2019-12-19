import turtle as tu

def triangle(long):
    tu.fd(long)
    tu.right(120)
    tu.fd(long)
    tu.right(120)
    tu.fd(long)
    tu.right(120)

def exagone(long):
        triangle(long)
        tu.fd(long)
        tu.right(60)
        triangle(long)
        for i in range(4):
            tu.left(60)
            triangle(long)
        tu.fd(long)




def velo(long):
    tu.color('yellow')
    exagone(long/2)
    tu.backward(long/2)
    tu.left(150)
    tu.color('orange')
    tu.fd(long)
    tu.color('red')
    tu.right(20)
    tu.fd(long/2)
    tu.backward(long/2)
    tu.color('orange')
    tu.right(40)
    triangle(long)
    tu.fd(long)
    tu.right(60)
    triangle(long)
    tu.fd(long)
    tu.color('yellow')
    tu.backward(long/2)
    exagone(long/2)
    tu.fd(long/2)
    tu.right(90)
    tu.color('red')
    tu.fd(long/3)
    tu.left(100)
    tu.fd(long / 3)



def base(size):
    tu.setx(1)
    tu.sety(1)
    tu.color('grey')
    tu.fd(size)
    tu.backward(size)
    tu.fd(size/5)
    tu.left(90)
    velo(size/4)
    tu.up()
    tu.setx(1)
    tu.sety(1)
    tu.down()
    tu.color('grey')
    tu.right(130)
    tu.fd(size*2)
    tu.backward(size/5)
    tu.left(90)

#tronc d'arbre
    tu.color('brown')
    tu.fd(size/1.5)
    tu.color('green')
    exagone(size/5)
#branche 1
    tu.color('brown')
    tu.fd(size/10)
    tu.right(100)
    tu.fd(size / 10)
    tu.color('green')
    exagone(size/8)
    tu.color('brown')
    tu.fd(size / 10)
    tu.right(80)
#branche 2
    tu.fd(size/4)
    tu.color('brown')
    tu.right(100)
    tu.fd(size / 10)
    tu.color('green')
    exagone(size/8)
    tu.color('brown')
    tu.fd(size / 10)
    tu.right(80)

#Nuages
    tu.up()
    tu.setx(20)
    tu.sety(180)
    tu.down()
    tu.color('blue')
    exagone(size/10)

#Nuages
    tu.up()
    tu.setx(80)
    tu.sety(200)
    tu.down()
    tu.color('blue')
    exagone(size/10)

#Nuages
    tu.up()
    tu.setx(150)
    tu.sety(220)
    tu.down()
    tu.color('blue')
    exagone(size/10)

base(200)
tu.penup()
