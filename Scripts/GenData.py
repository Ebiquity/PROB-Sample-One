out = open("../Data/DataFile.raw", "w")

for i in range(0, 100):
    out.write("%d\t%d\n" % (i, i * 9))

