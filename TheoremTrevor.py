# Theorem: DR(x^n + y^n) = DR(z^n)

from Root import digital_root as DR
import os


def theorem_left(x, y, n):
    return DR((x ** n) + (y ** n))


def theorem_right(z, n):
    return DR(z ** n)


n_range = int(input("Enter your range for n: "))
variable_range = int(input("Enter your range for x, y, and z: "))

export_x = open(f"D:\\{os.getlogin()}\\Desktop\\x_{n_range}_{variable_range}_equal.txt", "w")
export_y = open(f"D:\\{os.getlogin()}\\Desktop\\y_{n_range}_{variable_range}_equal.txt", "w")
export_z = open(f"D:\\{os.getlogin()}\\Desktop\\z_{n_range}_{variable_range}_equal.txt", "w")

export_x.write("X\n")
export_y.write("Y\n")
export_z.write("Z\n")

# # X
# for n in range(n_range + 1):
#     export_x.write("n = " + str(n) + "\n")
#     for y in range(variable_range):  # y, z changing for n
#         export_x.write("\ty, z = " + str(y) + "\n")
#         for x in range(variable_range):
#             export_x.write("\t\tx = " + str(x) + "\n")
#             export_x.write("\t\t" + str(theorem_left(x, y, n)) + " = " + str(theorem_right(y, n)) + "\n\n")

# X equal
for n in range(n_range + 1):
    for y in range(variable_range):  # y, z changing for n
        for x in range(variable_range):
            if theorem_left(x, y, n) == theorem_right(y, n):
                export_x.write("n = " + str(n) + "\n")
                export_x.write("\ty, z = " + str(y) + "\n")
                export_x.write("\t\tx = " + str(x) + "\n")
                export_x.write("\t\t" + str(theorem_left(x, y, n)) + " = " + str(theorem_right(y, n)) + "\n\n")

# # Y
# for n in range(n_range + 1):
#     export_y.write("n = " + str(n) + "\n")
#     for x in range(variable_range):  # x, z changing for n
#         export_y.write("\tx, z = " + str(x) + "\n")
#         for y in range(variable_range):
#             export_y.write("\t\ty = " + str(x) + "\n")
#             export_y.write("\t\t" + str(theorem_left(x, y, n)) + " = " + str(theorem_right(x, n)) + "\n\n")

# Y equal
for n in range(n_range + 1):
    for x in range(variable_range):  # x, z changing for n
        for y in range(variable_range):
            if theorem_left(x, y, n) == theorem_right(x, n):
                export_y.write("n = " + str(n) + "\n")
                export_y.write("\tx, z = " + str(x) + "\n")
                export_y.write("\t\ty = " + str(x) + "\n")
                export_y.write("\t\t" + str(theorem_left(x, y, n)) + " = " + str(theorem_right(x, n)) + "\n\n")

# # Z
# for n in range(n_range + 1):
#     export_z.write("n = " + str(n) + "\n")
#     for y in range(variable_range):  # x, y changing for n
#         export_z.write("\tx, y = " + str(y) + "\n")
#         for z in range(variable_range):
#             export_z.write("\t\tz = " + str(z) + "\n")
#             export_z.write("\t\t" + str(theorem_left(y, y, n)) + " = " + str(theorem_right(z, n)) + "\n\n")

# Z equal
for n in range(n_range + 1):
    for y in range(variable_range):  # x, y changing for n
        for z in range(variable_range):
            if theorem_left(y, y, n) == theorem_right(z, n):
                export_z.write("n = " + str(n) + "\n")
                export_z.write("\tx, y = " + str(y) + "\n")
                export_z.write("\t\tz = " + str(z) + "\n")
                export_z.write("\t\t" + str(theorem_left(y, y, n)) + " = " + str(theorem_right(z, n)) + "\n\n")

export_x.close()
export_y.close()
export_z.close()
