x, y, z = int(input("x: ")), int(input("y: ")), int(input("z: "))
print('Equilateral triangle' if x == y == z else 'Isosceles triangle' if x ==
      y or y == z or z == x else 'Scalene triangle')
