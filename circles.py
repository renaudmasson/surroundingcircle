import math
import sys

class Circle:
  def __init__(self,x,y,r):
    self.x = x
    self.y = y
    self.r = r

  def findDistanceCenters(self,otherCircle):
    # Compute the distance between the center of this circle and of an other circle.
    return math.sqrt((self.x-otherCircle.x)**2 + (self.y-otherCircle.y)**2)

  def findDistanceExtremePoints(self,otherCircle):
    # First we compute the inter center distance
    centerDist = self.findDistanceCenters(otherCircle)
    # then we add the radius
    return centerDist+self.r+otherCircle.r

  def findExtremePointPositions(self,otherCircle):
    # First we compute the direction between the two centers
    xDir = self.x - otherCircle.x
    yDir = self.y - otherCircle.y
    # We normalize
    norme = math.sqrt(xDir**2 + yDir**2)
    xDir /= norme
    yDir /= norme
    return (self.x + xDir*self.r,self.y + yDir*self.r)
  
  def copy(self,otherCircle):
    self.x = otherCircle.x
    self.y = otherCircle.y
    self.r = otherCircle.r


def findLargestCircle(circles):
  largestCircle = Circle(0,0,0)
  for c in circles:
    if c.r > largestCircle.r:
      largestCircle.copy(c)
  return largestCircle

def findSurroundingCircle(circles,largest):
  surrounding = Circle(largest.x,largest.y,largest.r)
  for i in range(len(circles)):
    for j in range(i+1,len(circles),1):
      dist = circles[i].findDistanceExtremePoints(circles[j])
      if dist > 2*surrounding.r:
        surrounding.r = dist/2
        # We compute the position of the extrem point of the circles
        expA = circles[i].findExtremePointPositions(circles[j])
        expB = circles[j].findExtremePointPositions(circles[i])
        surrounding.x = (expA[0] + expB[0])/2
        surrounding.y = (expA[1] + expB[1])/2
  return surrounding

def findSmallerSurroundingCircle(circles):
  largest = findLargestCircle(circles)
  surrounding = findSurroundingCircle(circles,largest)
  return surrounding

def buildCircles(data):
  circles = []
  for i in range(len(data)/3):
    circle = Circle(float(data[i*3]),float(data[i*3+1]),float(data[i*3+2]))
    circles.append(circle)
  return circles

def main():
  # The arguments are the x-position, y-position and radius of each circles, given one after the other
  # so calling the software would be something like : python circles.py x1 y1 r1 x2 y2 r2 x3 y3 r3
  args = sys.argv[1:]
  if len(args) % 3 == 0:
    circles = buildCircles(args)
    surrounding = findSmallerSurroundingCircle(circles)
    print "The surrounding circle is", surrounding.x, surrounding.y, surrounding.r
  else:
    print "Wrong number of arguments"
      
if __name__ == "__main__":
  main()
