# For unit-testing purposes, I've included a version of the function that passes
# all three sides in as arguments.
def triangle_auto(a,b,c):
  sides = [a,b,c]
  for x in sides:
    if isinstance(x, int) == False:
      return "All inputs must be integers. Please try again."
    elif x < 1:
      return "Zero or negative numbers are invalid. Try again."
  print "\nSides [{}, {}, {}]".format(sides[0],sides[1],sides[2])
  sides = sorted(sides)
  if sides[0] + sides[1] <= sides[2]: return "Not a valid triangle. Largest side bigger than or equal to two smaller sides."
  if all(x == sides[0] for x in sides): return "Equilateral"
  if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]: return "Isosceles"
  if sides[0] != sides[1] and sides[1] != sides[2]: return "Scalene"

print triangle_auto(10,20,29) # Scalene
print triangle_auto(10,10,10) # Equilateral
print triangle_auto(5,6,20) # Not a triangle
print triangle_auto(10,10,5) # Isosceles
print triangle_auto("10","20","29") # All inputs must be integers