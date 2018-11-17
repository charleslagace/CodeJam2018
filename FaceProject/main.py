import numpy as np
from argparse import ArgumentParser
import glob

def read_pgm(pgmf):
    """Return a raster of integers from a PGM as a list of lists."""
    pgmf.readline()
    pgmf.readline()
    line3 = pgmf.readline()
    (width, height) = [int(i) for i in line3.split()]
    #(width, height) = [int(i) for i in pgmf.readline().split()]
    depth = int(pgmf.readline())
    assert depth <= 255

    raster = []
    for y in range(height):
        row = []
        for y in range(width):
            row.append(ord(pgmf.read(1)))
        raster.append(row)
    return raster

if __name__ == "__main__":
    images = []
    dir_name = './assets/'

    for filename in glob.glob(dir_name + "*.pgm"):
        print(filename)
        f = open(filename, 'rb')
        raster = read_pgm(f)
        raster = np.array(raster)
        print(raster.shape)
        images.append(raster)

    print(len(images))

    np.save('dataset.npy', images)