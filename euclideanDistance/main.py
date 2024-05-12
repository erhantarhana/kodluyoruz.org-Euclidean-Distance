import math

points = [(2,3), (4,6), (4,1), (3,4), (4,7), (5,9)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

distances = list()

for i in range(0,len(points)):
    for j in range(i+1,len(points)):
        #print(f"points: {points[i],points[j]}, distance: {euclideanDistance(points[i],points[j])}")
        distances.append(euclideanDistance(points[i],points[j]))

print(distances)
print(min(distances))