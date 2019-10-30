"""Creates three orthagonal vectors using two vectors as input
Parameters
----------
v1 (list, Vector) – XYZ components of the first vector.
v2 (list, Vector) – XYZ components of the second vector.
Returns
-------
[list of three Vector] - three vectors orthagonal to each other

"""
def three_orth_vector(v1, v2):
    from compas.geometry import cross_vectors
    v3 = cross_vectors(v1, v2)
    v4 = cross_vectors(v3, v1)
    v5 = v1
    return v3,v4,v5

"""Returns the area of a polygon
Parameters
----------
polygon [list of points]
Returns
-------
[double] - [Length of polygon]
"""
def polygon_area_xy(polygon):
    from compas.geometry import cross_vectors_xy
    area_running_sum = 0.0
    for index in range(len(polygon)):
        p0 = polygon[index]
        p1 = polygon[(index +1)%len(polygon)]
        #print(cross_vectors_xy(p0,p1)[2])
        area_running_sum += cross_vectors_xy(p0,p1)[2]
    return area_running_sum / 2.0

def cross_multiple_vectors(vectors1, vectors2):
    from compas.geometry import cross_vectors
    results = []
    for v1,v2 in zip(vectors1,vectors2):
        results.append(cross_vectors(v1,v2))
    return results

if __name__ == "__main__":

    "Given two vectors, use the cross product to create a set of three orthonormal vectors."
    print(' ')
    v1 = [1,2,3]
    v2 = [4,5,6]
    print ("v1 = " , v1)
    print ("v2 = " , v2)
    print("Result: three_orth_vector(v1,v2) = ", three_orth_vector(v1,v2))

    print(' ')
    "Use the cross product to compute the area of a convex, 2D polygon."
    closed_polygon = [[1,1],[2,1],[2,3],[1,3]]
    print ("closed_polygon = " , closed_polygon)
    print ("Result: polygon_area_xy(closed_polygon) = ", polygon_area_xy(closed_polygon))

    print(' ')
    "Define a function for computing the cross products of two arrays of vectors."
    vectors1 = [[5,1,1],[2,6,1],[2,3,7],[7,1,3]]
    vectors2 = [[1,5,1],[9,2,1],[2,5,3],[2,1,3]]
    print ("Vectors 1:" , vectors1)
    print ("Vectors 2:" , vectors2)
    print ("Result: cross_multiple_vectors(vectors1,vectors2) = ", cross_multiple_vectors(vectors1,vectors2))

