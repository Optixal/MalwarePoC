import sys


network_portion = sys.argv[1]
third_octet_range = tuple(sys.argv[2].split("-"))
fourth_octet_range = tuple(sys.argv[3].split("-"))

hostfile = open(sys.argv[4], 'a')
for third in range(int(third_octet_range[0]), int(third_octet_range[1]) + 1):
    for fourth in range(int(fourth_octet_range[0]), int(fourth_octet_range[1])):
        hostfile.write(network_portion + "." + str(third) + "." + str(fourth) + "\n")
hostfile.close()


