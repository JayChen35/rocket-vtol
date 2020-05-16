from pidhandler import PDHandler

dt = 0.01
x = 0
v = 0
a = 0
target = 10
pd = PDHandler(2, 2, dt)

for i in range(2000):
    if i % 100 == 0:
        print(x, v, a)
    p, d, a = pd.calculate(target - x)
    v += a * dt
    x += v * dt

print("Simulation over")