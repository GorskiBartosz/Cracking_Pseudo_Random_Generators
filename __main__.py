import math
import time

from lcg import LCG, recognize_lgc
from glibc_random import GlibcRandom, recognize_glibc_random


def lcg_test():
    seed = int(round(time.time() * 1000))
    # these parameters are used in ansi C implementation of LGC
    true_a = 1103515245
    true_c = 12345
    true_m = int(math.pow(2, 31))
    lcg = LCG(seed, true_a, true_c, true_m)
    print(recognize_lgc(lcg))


def glib_c_random_test():
    seed = int(round(time.time() * 1000))
    true_a = 16807
    true_m = int(math.pow(2, 31))
    generator = GlibcRandom(seed, true_a, true_m)
    print(recognize_glibc_random(generator))


if __name__ == '__main__':
    lcg_test()
    glib_c_random_test()
