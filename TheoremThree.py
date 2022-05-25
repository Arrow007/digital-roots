from Root import digital_root as DR
import os

# Does DR(w ^ n) = DR(w) ^ DR(n) for w = 1 - 500, n = say like 0

export = open(f"C:\\Users\\{os.getlogin()}\\Desktop\\theorem_three.txt", "w")

for n in range(500):
    export.write("n = " + str(n) + "\n")
    for w in range(500):
        export.write("\tw = " + str(w) + "\n")
        export.write("\t" + str(DR(w ** n)) + " = " + str(DR(DR(w) ** DR(n))) + "\n\n")