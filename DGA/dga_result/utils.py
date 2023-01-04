import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.path as mplPath

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(methane, ethylene, acetylene):
    methane_percentage = (methane/(methane + ethylene + acetylene))*100
    ethylene_percentage = (ethylene/(methane + ethylene + acetylene))*100
    acetylene_percentage = (acetylene/(methane + ethylene + acetylene))*100

    # Define the transformation matrix
    A = np.array([[5, 2.5, 50], [0, 5 * np.sqrt(3)/2, 50], [0, 0, 1]])

    # Define a set of points for Duval triangle regions
    p = np.array([
        [0, 0, 1],          #0-p1
        [0, 100, 1],        #1-p2
        [100, 0, 1],        #2-p3
        [0, 87, 1],         #3-p4
        [0, 96, 1],         #4-p5
        [0, 98, 1],         #5-p6
        [2, 98, 1],         #6-p7
        [23, 0, 1],         #7-p8
        [23, 64, 1],        #8-p9
        [20, 76, 1],        #9-p10
        [20, 80, 1],        #10-p11
        [40, 31, 1],        #11-p12
        [40, 47, 1],        #12-p13
        [50, 35, 1],        #13-p14
        [50, 46, 1],        #14-p15
        [50, 50, 1],        #15-p16
        [71, 0, 1],         #16-p17
        [85, 0, 1]])        #17-p18

    # Apply the coordinates transformation to all points
    v = p @ np.transpose(A)

    # Set one more sample point
    sample_point = np.array([ethylene_percentage, methane_percentage, 1]) @ np.transpose(A)

    # Define each of the regions by the coordinates of its angle points
    region_PD = v[[5, 1, 6], :]
    region_T1 = v[[4, 5, 6, 10, 9], :]
    region_T2 = v[[9, 10, 15, 14], :]
    region_T3 = v[[13, 15, 2, 17], :]
    region_D1 = v[[0, 3, 8, 7], :]
    region_D2 = v[[7, 8, 12, 11, 16], :]
    region_DT = v[[3, 4, 14, 13, 17, 16, 11, 12], :]

    # Plot the results
    fig, ax1 = plt.subplots()
    ax1.fill(region_PD[:, 0], region_PD[:, 1], '#2e962d')
    ax1.fill(region_T1[:, 0], region_T1[:, 1], '#bebe12')
    ax1.fill(region_T2[:, 0], region_T2[:, 1], '#ff642b')
    ax1.fill(region_T3[:, 0], region_T3[:, 1], '#b46414')
    ax1.fill(region_D1[:, 0], region_D1[:, 1], '#10b4a7')
    ax1.fill(region_D2[:, 0], region_D2[:, 1], '#121eb4')
    ax1.fill(region_DT[:, 0], region_DT[:, 1], '#f217d0')
    ax1.scatter(sample_point[0], sample_point[1], marker='x', c='r', zorder=2)
    ax1.grid(linestyle='--', alpha=0.4, axis='both')

    # Also place axes captions
    label1 = np.array([45, -5, 1]) @ np.transpose(A)
    ax1.text(label1[0], label1[1], '%C2H2')
    label11 = np.array([95, -5, 1]) @ np.transpose(A)
    ax1.text(label11[0], label11[1], '0')
    label12 = np.array([5, -5, 1]) @ np.transpose(A)
    ax1.text(label12[0], label12[1], '100')
    label2 = np.array([-10, 55, 1]) @ np.transpose(A)
    ax1.text(label2[0], label2[1], '%CH4')
    label21 = np.array([-7, 5, 1]) @ np.transpose(A)
    ax1.text(label21[0], label21[1], '0')
    label22 = np.array([-7, 95, 1]) @ np.transpose(A)
    ax1.text(label22[0], label22[1], '100')
    label3 = np.array([45, 55, 1]) @ np.transpose(A)
    ax1.text(label3[0], label3[1], '%C2H4')
    label31 = np.array([5, 95, 1]) @ np.transpose(A)
    ax1.text(label31[0], label31[1], '0')
    label22 = np.array([95, 5, 1]) @ np.transpose(A)
    ax1.text(label22[0], label22[1], '100')

    # decision based on location
    PD = mplPath.Path(np.array([[295, 474.35244785],[300, 483.01270189],[305, 474.35244785]]))
    T1 = mplPath.Path(np.array([[290, 465.69219382],[295, 474.35244785],[305, 474.35244785],[350, 396.41016151],[340, 379.08965344]]))
    T2 = mplPath.Path(np.array([[340, 379.08965344],[350, 396.41016151],[425, 266.50635095],[415, 249.18584287]]))
    T3 = mplPath.Path(np.array([[387.5, 201.55444566],[425, 266.50635095],[550, 50],[475, 50]]))
    D1 = mplPath.Path(np.array([[50, 50],[267.5, 426.72105065],[325, 327.12812921], [165, 50]]))
    D2 = mplPath.Path(np.array([[165,50],[325, 327.12812921],[327.5, 184.23393759],[367.5, 253.51596989],[405, 50]]))
    DT = mplPath.Path(np.array([[267.5, 426.72105065],[290, 465.69219382],[415, 249.18584287],[387.5, 201.55444566],[475, 50],[405, 50],[327.5, 184.23393759],[367.5, 253.51596989],]))

    sample = (sample_point[0], sample_point[1])

    duval_1_area =  'Not applicable'

    if PD.contains_point(sample):
        duval_1_area = "PD"
    elif T1.contains_point(sample):
        duval_1_area = "T1"
    elif T2.contains_point(sample):
        duval_1_area = "T2"
    elif T3.contains_point(sample):
        duval_1_area = "T3"
    elif D1.contains_point(sample):
        duval_1_area = "D1"
    elif D2.contains_point(sample):
        duval_1_area = "D2"
    elif DT.contains_point(sample):
        duval_1_area = "DT"

    # Show the final plot
    ax1.set_xlim(0, 600)
    ax1.set_ylim(0, 550)
    
    # plt.switch_backend('AGG')
    # plt.title('Duval Triangle 1')
    # plt.plot()
    duval_graph = get_graph()
    
    return duval_graph, duval_1_area