import os
import numpy as np

with open('/Users/xingoo/PycharmProjects/keras-yolo3/model_data/label.txt', 'r') as f:
    lines = f.readlines()
print(len(lines))


classes = {}
labels  = {}
for line in lines:
    line = line.strip('\n').split(',')

    if line[-2] not in classes:
        classes[line[-2]] = len(classes)

    line[-2] = classes[line[-2]]
    if line[0] not in labels:
        labels[line[0]] = []

    labels[line[0]].append(','.join(np.array(line[1:-1], dtype='str')))



with open('/Users/xingoo/PycharmProjects/keras-yolo3/model_data/label_yolo.txt','w') as f:
    for label in labels:
        f.write(label+' '+(' '.join(labels[label]))+'\n')