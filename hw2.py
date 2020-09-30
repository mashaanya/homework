# homework
import math


def rotate1(vec, angle):
    mat = [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
    newvec = [vec[0] * mat[0][0] + vec[1] * mat[0][1], vec[0] * mat[1][0] + vec[1] * mat[1][1]]
    return newvec


def scale1(vec, c):
    return [vec[0] * c, vec[1] * c]


def scale2(vec, c):
    return [vec[0] * c, vec[1] * c, vec[2] * c]


def rotate2(vec, angle, axis):
    if axis == 'Y':
        mat = [[math.cos(angle), 0, -math.sin(angle)], [0, 1, 0], [math.sin(angle), 0, math.cos(angle)]]
    if axis == 'X':
        mat = [[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]]
    if axis == 'Z':
        mat = [[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]
    newvec = [vec[0] * mat[0][0] + vec[1] * mat[0][1] + vec[2] * mat[0][2],
              vec[0] * mat[1][0] + vec[1] * mat[1][1] + vec[2] * mat[1][2],
              vec[0] * mat[2][0] + vec[1] * mat[2][1] + vec[2] * mat[2][2]]

    return newvec


dimension = input()
if dimension == '2D':
    vec = list(map(float, input().split()))
    length = math.sqrt(vec[0] ** 2 + vec[1] ** 2)
    print('length', length)
    constant = float(input())
    new = scale1(vec, constant)
    print('scaled', *new)
    angle = float(input()) * math.pi / 180
    print('initial', *rotate1(vec, angle))
    print('scaled', *rotate1(new, angle))
elif dimension == '3D':
    vec = list(map(float, input().split()))
    length = math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)
    print('length', length)
    constant = float(input())
    new = scale2(vec, constant)
    print('scaled', *new)
    angle = float(input()) * math.pi / 180
    axis = input()
    print('initial', *rotate2(vec, angle, axis))
    print('scaled', *rotate2(new, angle, axis))
else:
    print('please try againg and input demension')

