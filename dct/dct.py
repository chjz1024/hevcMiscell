import numpy as np
from scipy.fftpack import dct, idct


class MatTransform:
    def __init__(self, highPrec=False):
        if highPrec:
            self._dst4 = self._dst4matrix(7424, 14081, 18893, 21505)
            self._dct4 = self._dct4matrix(16384, 21266, 9224)
            self._dct8 = self._dct8matrix(16384, 21266, 9224, 22813, 19244, 12769, 4563)
            self._dct16 = self._dct16matrix(16384, 21266, 9224, 22813, 19244, 12769, 4563, 23120, 22063, 20450, 17972,
                                            14642, 11109, 6446, 2316)
            self._dct32 = self._dct32matrix(16384, 21266, 9224, 22813, 19244, 12769, 4563, 23120, 22063, 20450, 17972,
                                            14642, 11109, 6446, 2316, 23106, 22852, 22445, 21848, 20995, 19810, 18601,
                                            17143, 15718, 13853, 11749, 9846, 7908, 5573, 3281, 946)
        else:
            self._dst4 = self._dst4matrix(29, 55, 74, 84)
            self._dct4 = self._dct4matrix(64, 83, 36)
            self._dct8 = self._dct8matrix(64, 83, 36, 89, 75, 50, 18)
            self._dct16 = self._dct16matrix(64, 83, 36, 89, 75, 50, 18, 90, 87, 80, 70, 57, 43, 25, 9)
            self._dct32 = self._dct32matrix(64, 83, 36, 89, 75, 50, 18, 90, 87, 80, 70, 57, 43, 25, 9, 90, 90, 88, 85,
                                            82,
                                            78, 73, 67, 61, 54, 46, 38, 31, 22, 13, 4)

    def _dst4matrix(self, a, b, c, d):
        return np.array([
            [a, b, c, d],
            [c, c, 0, -c],
            [d, -a, -c, b],
            [b, -d, c, -a], ], dtype=int)

    def _dct4matrix(self, a, b, c):
        return np.array([
            [a, a, a, a],
            [b, c, -c, -b],
            [a, -a, -a, a],
            [c, -b, b, -c]], dtype=int)

    def _dct8matrix(self, a, b, c, d, e, f, g):
        return np.array([
            [a, a, a, a, a, a, a, a],
            [d, e, f, g, -g, -f, -e, -d],
            [b, c, -c, -b, -b, -c, c, b],
            [e, -g, -d, -f, f, d, g, -e],
            [a, -a, -a, a, a, -a, -a, a],
            [f, -d, g, e, -e, -g, d, -f],
            [c, -b, b, -c, -c, b, -b, c],
            [g, -f, e, -d, d, -e, f, -g]], dtype=int)

    def _dct16matrix(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
        return np.array([
            [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
            [h, i, j, k, l, m, n, o, -o, -n, -m, -l, -k, -j, -i, -h],
            [d, e, f, g, -g, -f, -e, -d, -d, -e, -f, -g, g, f, e, d],
            [i, l, o, -m, -j, -h, -k, -n, n, k, h, j, m, -o, -l, -i],
            [b, c, -c, -b, -b, -c, c, b, b, c, -c, -b, -b, -c, c, b],
            [j, o, -k, -i, -n, l, h, m, -m, -h, -l, n, i, k, -o, -j],
            [e, -g, -d, -f, f, d, g, -e, -e, g, d, f, -f, -d, -g, e],
            [k, -m, -i, o, h, n, -j, -l, l, j, -n, -h, -o, i, m, -k],
            [a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, a],
            [l, -j, -n, h, -o, -i, m, k, -k, -m, i, o, -h, n, j, -l],
            [f, -d, g, e, -e, -g, d, -f, -f, d, -g, -e, e, g, -d, f],
            [m, -h, l, n, -i, k, o, -j, j, -o, -k, i, -n, -l, h, -m],
            [c, -b, b, -c, -c, b, -b, c, c, -b, b, -c, -c, b, -b, c],
            [n, -k, h, -j, m, o, -l, i, -i, l, -o, -m, j, -h, k, -n],
            [g, -f, e, -d, d, -e, f, -g, -g, f, -e, d, -d, e, -f, g],
            [o, -n, m, -l, k, -j, i, -h, h, -i, j, -k, l, -m, n, -o]], dtype=int)

    def _dct32matrix(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E):
        return np.array([
            [a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a],
            [p, q, r, s, t, u, v, w, x, y, z, A, B, C, D, E, -E, -D, -C, -B, -A, -z, -y, -x, -w, -v, -u, -t, -s, -r, -q,
             -p],
            [h, i, j, k, l, m, n, o, -o, -n, -m, -l, -k, -j, -i, -h, -h, -i, -j, -k, -l, -m, -n, -o, o, n, m, l, k, j,
             i, h],
            [q, t, w, z, C, -E, -B, -y, -v, -s, -p, -r, -u, -x, -A, -D, D, A, x, u, r, p, s, v, y, B, E, -C, -z, -w, -t,
             -q],
            [d, e, f, g, -g, -f, -e, -d, -d, -e, -f, -g, g, f, e, d, d, e, f, g, -g, -f, -e, -d, -d, -e, -f, -g, g, f,
             e, d],
            [r, w, B, -D, -y, -t, -p, -u, -z, -E, A, v, q, s, x, C, -C, -x, -s, -q, -v, -A, E, z, u, p, t, y, D, -B, -w,
             -r],
            [i, l, o, -m, -j, -h, -k, -n, n, k, h, j, m, -o, -l, -i, -i, -l, -o, m, j, h, k, n, -n, -k, -h, -j, -m, o,
             l, i],
            [s, z, -D, -w, -p, -v, -C, A, t, r, y, -E, -x, -q, -u, -B, B, u, q, x, E, -y, -r, -t, -A, C, v, p, w, D, -z,
             -s],
            [b, c, -c, -b, -b, -c, c, b, b, c, -c, -b, -b, -c, c, b, b, c, -c, -b, -b, -c, c, b, b, c, -c, -b, -b, -c,
             c, b],
            [t, C, -y, -p, -x, D, u, s, B, -z, -q, -w, E, v, r, A, -A, -r, -v, -E, w, q, z, -B, -s, -u, -D, x, p, y, -C,
             -t],
            [j, o, -k, -i, -n, l, h, m, -m, -h, -l, n, i, k, -o, -j, -j, -o, k, i, n, -l, -h, -m, m, h, l, -n, -i, -k,
             o, j],
            [u, -E, -t, -v, D, s, w, -C, -r, -x, B, q, y, -A, -p, -z, z, p, A, -y, -q, -B, x, r, C, -w, -s, -D, v, t, E,
             -u],
            [e, -g, -d, -f, f, d, g, -e, -e, g, d, f, -f, -d, -g, e, e, -g, -d, -f, f, d, g, -e, -e, g, d, f, -f, -d,
             -g, e],
            [v, -B, -p, -C, u, w, -A, -q, -D, t, x, -z, -r, -E, s, y, -y, -s, E, r, z, -x, -t, D, q, A, -w, -u, C, p, B,
             -v],
            [k, -m, -i, o, h, n, -j, -l, l, j, -n, -h, -o, i, m, -k, -k, m, i, -o, -h, -n, j, l, -l, -j, n, h, o, -i,
             -m, k],
            [w, -y, -u, A, s, -C, -q, E, p, D, -r, -B, t, z, -v, -x, x, v, -z, -t, B, r, -D, -p, -E, q, C, -s, -A, u, y,
             -w],
            [a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a, -a, a, a, -a,
             -a, a],
            [x, -v, -z, t, B, -r, -D, p, -E, -q, C, s, -A, -u, y, w, -w, -y, u, A, -s, -C, q, E, -p, D, r, -B, -t, z, v,
             -x],
            [l, -j, -n, h, -o, -i, m, k, -k, -m, i, o, -h, n, j, -l, -l, j, n, -h, o, i, -m, -k, k, m, -i, -o, h, -n,
             -j, l],
            [y, -s, -E, r, -z, -x, t, D, -q, A, w, -u, -C, p, -B, -v, v, B, -p, C, u, -w, -A, q, -D, -t, x, z, -r, E, s,
             -y],
            [f, -d, g, e, -e, -g, d, -f, -f, d, -g, -e, e, g, -d, f, f, -d, g, e, -e, -g, d, -f, -f, d, -g, -e, e, g,
             -d, f],
            [z, -p, A, y, -q, B, x, -r, C, w, -s, D, v, -t, E, u, -u, -E, t, -v, -D, s, -w, -C, r, -x, -B, q, -y, -A, p,
             -z],
            [m, -h, l, n, -i, k, o, -j, j, -o, -k, i, -n, -l, h, -m, -m, h, -l, -n, i, -k, -o, j, -j, o, k, -i, n, l,
             -h, m],
            [A, -r, v, -E, -w, q, -z, -B, s, -u, D, x, -p, y, C, -t, t, -C, -y, p, -x, -D, u, -s, B, z, -q, w, E, -v, r,
             -A],
            [c, -b, b, -c, -c, b, -b, c, c, -b, b, -c, -c, b, -b, c, c, -b, b, -c, -c, b, -b, c, c, -b, b, -c, -c, b,
             -b, c],
            [B, -u, q, -x, E, y, -r, t, -A, -C, v, -p, w, -D, -z, s, -s, z, D, -w, p, -v, C, A, -t, r, -y, -E, x, -q, u,
             -B],
            [n, -k, h, -j, m, o, -l, i, -i, l, -o, -m, j, -h, k, -n, -n, k, -h, j, -m, -o, l, -i, i, -l, o, m, -j, h,
             -k, n],
            [C, -x, s, -q, v, -A, -E, z, -u, p, -t, y, -D, -B, w, -r, r, -w, B, D, -y, t, -p, u, -z, E, A, -v, q, -s, x,
             -C],
            [g, -f, e, -d, d, -e, f, -g, -g, f, -e, d, -d, e, -f, g, g, -f, e, -d, d, -e, f, -g, -g, f, -e, d, -d, e,
             -f, g],
            [D, -A, x, -u, r, -p, s, -v, y, -B, E, C, -z, w, -t, q, -q, t, -w, z, -C, -E, B, -y, v, -s, p, -r, u, -x, A,
             -D],
            [o, -n, m, -l, k, -j, i, -h, h, -i, j, -k, l, -m, n, -o, -o, n, -m, l, -k, j, -i, h, -h, i, -j, k, -l, m,
             -n, o],
            [E, -D, C, -B, A, -z, y, -x, w, -v, u, -t, s, -r, q, -p, p, -q, r, -s, t, -u, v, -w, x, -y, z, -A, B, -C, D,
             -E]], dtype=int)

    def dct2(self, block):
        return dct(dct(block, axis=1, norm='ortho'), axis=0, norm='ortho')

    def idct2(self, block):
        return idct(idct(block, axis=0, norm="ortho"), axis=1, norm='ortho')

    def dst2i(self, block: np.ndarray):
        if block.shape == (4, 4):
            return self._dst4@block@self._dst4.T/128**2
        else:
            raise NotImplemented

    def idst2i(self, block: np.ndarray):
        if block.shape == (4, 4):
            return self._dst4.T@block@self._dst4/128**2
        else:
            raise NotImplemented


transMat = MatTransform()
