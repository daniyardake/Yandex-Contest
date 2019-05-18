# -*- coding: utf-8 -*-

#%%

import math

infilename = 'input.txt'
outfilename = 'output.txt'
infile = open(infilename)
outfile = open(outfilename, 'w')



linenum = 0
chips = []
for line in infile:
    input = line.split()
    if linenum == 0:
        N = int(input[0])
        R = float(input[1])
    else:
        x = float(input[0])
        y = float(input[1])
        chips.append([x, y])
        
    if linenum == N:
        break
    linenum += 1

def dot_pr(a, b):
    return a[0] * b[0] + a[1] * b[1]

def norm(a):
    return math.sqrt(dot_pr(a, a))

def cut_segment(C, R, A, B):
    slant_vec = [A[0] - C[0], A[1] - C[1]]
    dir_vec = [A[0] - B[0], A[1] - B[1]]
    norm_dir_vec = norm(dir_vec)
    perp_vec = [- dir_vec[1], dir_vec[0]]
    uni_perp_vec = [perp_vec[0] / norm_dir_vec, perp_vec[1] / norm_dir_vec]
    dist_from_line = abs(dot_pr(slant_vec, uni_perp_vec))
    if dist_from_line > R:
        return 0.0
    theta = 2.0 * math.acos(dist_from_line / R)
    return R * R * (theta - math.sin(theta)) / 2.0

def cut_corner(C, R, D):
    vec = [D[0] - C[0], D[1] - C[1]]
    if norm(vec) > R:
        return 0.0
    addendum = math.sqrt(R * R - vec[1] * vec[1])
    if D[0] < C[0]:
        addendum *= - 1.0
    A = [C[0] + addendum, D[1]]
    addendum = math.sqrt(R * R - vec[0] * vec[0])
    if D[1] < C[1]:
        addendum *= - 1.0
    B = [D[0], C[1] + addendum]
#    segment = cut_segment(C, R, A, B)
    half_base = norm([A[0] - B[0], A[1] - B[1]]) / 2.0
    theta = 2.0 * math.asin(half_base / R)
    segment = R * R * (theta - math.sin(theta)) / 2.0
    leg1 = norm([A[0] - D[0], A[1] - D[1]])
    leg2 = norm([B[0] - D[0], B[1] - D[1]])
    triangle = leg1 * leg2 / 2.0
    return triangle + segment

EV = 0.0
corner1 = [0.0, 0.0]
corner2 = [1.0, 0.0]
corner3 = [1.0, 1.0]
corner4 = [0.0, 1.0]
for dot in chips:
    EV += math.pi * R * R
    EV -= cut_segment(dot, R, corner1, corner2)
    EV -= cut_segment(dot, R, corner2, corner3)
    EV -= cut_segment(dot, R, corner3, corner4)
    EV -= cut_segment(dot, R, corner4, corner1)
    EV += cut_corner(dot, R, corner1)
    EV += cut_corner(dot, R, corner2)
    EV += cut_corner(dot, R, corner3)
    EV += cut_corner(dot, R, corner4)
    
outfile.write(str(EV) + '\n')

outfile.close()
infile.close()

#%%
