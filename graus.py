
print("Fahreinheit | Celsius")
for fahrenheit in range(45, 80+1, 1):
    celsius = 5/9 * (fahrenheit-32)
    print(f"{fahrenheit} | {celsius:.3}")