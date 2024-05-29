def within_triangle(point1, point2, point3, test_point):
  def sign(p1, p2, p3):
      return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

  b1 = sign(test_point, point1, point2) < 0.0
  b2 = sign(test_point, point2, point3) < 0.0
  b3 = sign(test_point, point3, point1) < 0.0

  return ((b1 == b2) and (b2 == b3))
print(within_triangle((1, 4), (5, 6), (6, 1), (4, 5)))

print(within_triangle((1, 4), (5, 6), (6, 1), (3, 2)))

print(within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)))