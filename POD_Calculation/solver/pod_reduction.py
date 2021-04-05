import numpy as np


class PODReduction:
    def __init__(self, snapshots):
        self.snapshots = snapshots
        self.correlation_matrix = self.calculate_correlation_matrix()

    def calculate_correlation_matrix(self):
        """ Creates the correlation matrix needed to obtain the POD basis.

        Returns:
            C correlation matrix based on the used snapshots
        """
        corr_mat = np.zeros(shape=(len(self.snapshots), len(self.snapshots)))

        for i in range(0, len(corr_mat)):
            for j in range(0, len(corr_mat)):
                dot_prod = 0
                for k in range(0, len(self.snapshots[0])):
                    dot_prod = dot_prod + (self.snapshots[i][k][0] * self.snapshots[j][k][0] +
                                           self.snapshots[i][k][1] * self.snapshots[j][k][
                                               1]) * 0.000015  # need to know the mesh cell size

                corr_mat[i][j] = dot_prod / len(self.snapshots)
        return corr_mat

    def l2norm(self, u1):
        # take square of differences and sum them
        return np.sqrt(np.sum(np.power(u1, 2)))

    @property
    def eigenvalue_pairs(self, matrix):
        """ Calculates the eigenvalues

        Parameters:
            matrix: matrix used for the eigenvalue calculations

        Returns:
            eigenvalues of the given matrix
        """
        return np.linalg.eig(matrix)
