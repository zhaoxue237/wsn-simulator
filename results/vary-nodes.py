import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools


# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')


framesize = 1500
time=2400
protocol = "GALTIER"
nodes = [5, 10, 20, 30, 40, 50, 70, 100]
scheme = "optimal"
file = "./{0}-{1}-nodes-{2}-framesize.csv".format(protocol, scheme, framesize)

if (os.path.isfile(file)):
    os.remove(file)

for i in nodes:
    print "SIMULATING WITH {0} NODES".format(str(i))
    cmd = "java -Dscheme=\"{0}\" -Dframesize={1} -Dnodes=\"{2}\" -Dtime={3} -Doutput={4} -Dprotocol=\"{5}\" -jar wsn-simulator.jar ".format(
        scheme, str(framesize), str(i), str(time), file, protocol)
    os.system(cmd)


#
# df = pd.read_csv(file, sep=';')
# nodecounts = df['nodecount'].unique()
#
# fig = plt.figure()
# for i,ms in zip(nodecounts, itertools.cycle('s^+*>')):
#     subdf = df[df['nodecount'] == i]
#     fsize = subdf['framesize']
#     delay = subdf['delay']
#     throughput = subdf['throughput']
#     plt.plot(fsize, delay, label="n = " + str(i), marker=ms)
#
# plt.xlabel("Framesize [bytes]")
# plt.ylabel("Delay [ms]")
# plt.xticks(fsize)
# plt.legend()
# plt.show()

# fig = plt.figure()
# for i,ms in zip(nodecounts, itertools.cycle('s^+*>')):
#     subdf = df[df['nodecount'] == i]
#     fsize = subdf['framesize']
#     delay = subdf['delay']
#     throughput = subdf['throughput']
#     plt.plot(fsize, throughput, label="n = " + str(i), marker=ms)
#
# plt.xlabel("Framesize [bytes]")
# plt.ylabel("Normalized throughput")
# plt.xticks(fsize)
# plt.legend()
# plt.show()