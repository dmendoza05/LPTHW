cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are onlu", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carppool today."
print "We need to put about", average_passengers_per_car, "in each car."

# STUDY DRILLS
# car_pool_capacity is not defined. It should be carpool_capacity.

# 1. It is not necessary in this case because we are just using whole numbers without decimals(integers). 

x = 10
y = 20
z = 30
xx = x + x
yy = y + y
zz = z + z
xy = x + y
yz = y + z
xz = x + z

print "x + x is equals to", xx
print "y + y is equals to", yy
print "z + z is equals to", zz
print "x + y is equals to", xy
print "y + z is equals to", yz
print "x + z is equals to", xz