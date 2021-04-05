from os import path
import numpy as np


class OpenFOAMInterface:

    def __init__(self, dest):
        self.dest = dest
        self.num_points = ''

    def read_snapshots(self):
        time_stamps = []
        for i in range(0, 3):
            for j in range(0, 10):
                if not(i == 0 and j == 0):
                    try:
                        if j == 0:
                            filePath = path.join(self.dest, str(i), "U")
                            print(filePath)

                        else:
                            filePath = path.join(self.dest, str(i) + '.' + str(j), "U")
                            print(filePath)

                        with open(filePath, "r") as f:
                            solution = []
                            lines = f.readlines()
                            self.num_points = int(lines[21])

                            for k in range(23, self.num_points + 23):
                                tst = lines[k][1:-2].split(" ")
                                arr = np.array(tst).astype(np.float)
                                solution.append(arr)

                            solution = np.asarray(solution)
                            time_stamps.append(solution)

                    except FileNotFoundError:
                        pass
                        print("Path: " + filePath + "not found!")

        return time_stamps
