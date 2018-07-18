# Multi dimensional lists are lists within lists, or lists within lists within lists.

x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])
print(x[2][1])

#2D
y = [[5,2],
     [6,2],
     [3,1],
     [12,6]
    ]
print(y)

#3D
z = [
        [[2,3], [6,3]],
        [[1,6], [5,2]],
        [8,2],
        [5,12]
    ]
print(z[1][1][0])
