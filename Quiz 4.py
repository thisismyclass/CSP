speed = int(input("how fast is the plane in MPH: "))
wind_speed = int(input("how fast is the wind traveling?: "))
wind = input("is the wind traveling with or against the plane?: ")
destination = input("what is the planes destination?: ")
distance = int(input("how far away is the destination in miles?: "))


if wind == "with":
    speed2 = (speed + wind_speed)
else:
    speed2 = (speed - wind_speed)


time = (distance / speed2)

time2 = round(time, 2)

print("the plane will travel to", destination ,"in", float(time2) ,"hours")
