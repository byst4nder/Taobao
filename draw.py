import numpy
import matplotlib.pylab as plt
from matplotlib.font_manager import *

# myfont = FontProperties(fname='/usr/share/fonts/truetype/arphic/ukai.ttc')
plt.rcParams['font.sans-serif'] = ['simhei']
plt.rcParams['axes.unicode_minus'] = False

def pie(data, img_name):
    fig = plt.figure(figsize=(8, 8))

    cities = data.keys()
    values = [x for x in data.values()]
    # print(values)

    ax1 = fig.add_subplot(111)
    ax1.set_title(u'饼图')

    labels = [u'{}:{}'.format(city, value) for city,value in zip(cities,values)]
    print(labels)

    # explode = [0, 0.1]

    ax1.pie(values, labels=labels)

    plt.savefig('%s.png'%img_name)
    plt.show()

# def bar(data, img_name):
#     fig = plt.figure(figsize=(12, 8))
#     cities = data.keys()
#     values = [x for x in data.values()]
#     # print(values)
#     idx = len(data)
#
#     ax1 = fig.add_subplot(111)
#     ax1.set_title(u'直方图')
#
#     labels = [u'{}:{}'.format(city, value) for city, value in zip(cities, values)]
#     # print(labels)
#
#     explode = [0, 0.1]
#     ax1.bar(idx, cities, values)
#
#     plt.savefig('%s.png' % img_name)
#     plt.show()