def triangle_input():
  sides = []
  while len(sides) != 3:
    try:
      choice = int(input("Length of side {}:\n".format(len(sides)+1)))
      if choice > 0:
        sides.append(choice)
      else:
        print "Zero is not valid. Try again."
    except (NameError, ValueError, SyntaxError):
      print "Must be an integer value greater than zero. Try again."
  print "\nA:{}, B:{}, C:{}".format(sides[0],sides[1],sides[2])
  # Checking if all sides are valid. Then if equilateral, isosceles, or scalene
  sides = sorted(sides)
  if sides[0] + sides[1] <= sides[2]: return "Not a valid triangle. Largest side bigger than or equal to two smaller sides."
  if all(x == sides[0] for x in sides): return "Equilateral"
  if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]: return "Isosceles"
  if sides[0] != sides[1] and sides[1] != sides[2]: return "Scalene"

print triangle_input()