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

def get_plot_duval_1(methane, ethylene, acetylene):
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
    PD = mplPath.Path(np.array(region_PD[:,0:2]))
    T1 = mplPath.Path(np.array(region_T1[:,0:2]))
    T2 = mplPath.Path(np.array(region_T2[:,0:2]))
    T3 = mplPath.Path(np.array(region_T3[:,0:2]))
    D1 = mplPath.Path(np.array(region_D1[:,0:2]))
    D2 = mplPath.Path(np.array(region_D2[:,0:2]))
    DT = mplPath.Path(np.array(region_DT[:,0:2]))

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

def get_plot_duval_4(methane, hydrogen, ethane):
    methane_percentage = (methane/(methane + hydrogen + ethane))*100
    hydrogen_percentage = (hydrogen/(methane + hydrogen + ethane))*100
    ethane_percentage = (ethane/(methane + hydrogen + ethane))*100

    # Define the transformation matrix
    A = np.array([[5, 2.5, 50], [0, 5 * np.sqrt(3)/2, 50], [0, 0, 1]])

    # Define a set of points for Duval triangle regions
    p = np.array([
        [0, 0, 1],          #0-p1
        [0, 100, 1],        #1-p2
        [100, 0, 1],        #2-p3
        [0, 9, 1],         #3-p4
        [0, 54, 1],         #4-p5
        [2,98, 1],         #5-p6
        [15,85, 1],         #6-p7
        [48, 9, 1],         #7-p8
        [36, 39, 1],        #8-p9
        [36, 64, 1],        #9-p10
        [70, 0, 1],        #10-p11
        [60, 9, 1],        #11-p12
        [52, 16, 1],        #12-p13
        [60, 16, 1],        #13-p14
        [2, 96, 1],        #14-p15
        [15, 83, 1]])       #15-p16])

    # Apply the coordinates transformation to all points
    v = p @ np.transpose(A)

    # Set one more sample point
    sample_point = np.array([methane_percentage, hydrogen_percentage, 1]) @ np.transpose(A)

    # Define each of the regions by the coordinates of its angle points
    region_PD = v[[14,5,6,15], :]
    region_S = v[[4,1,5,14,15,6,9,8,13,12,11,7], :]
    region_O = v[[0,3,7,11,10], :]
    region_C = v[[9,8,13,12,11,10,2], :]
    region_ND = v[[3,7,4], :]

    # Plot the results
    fig, ax1 = plt.subplots()
    ax1.fill(region_PD[:, 0], region_PD[:, 1], '#2e962d')
    ax1.fill(region_S[:, 0], region_S[:, 1], '#bebe12')
    ax1.fill(region_O[:, 0], region_O[:, 1], '#ff642b')
    ax1.fill(region_C[:, 0], region_C[:, 1], '#b46414')
    ax1.fill(region_ND[:, 0], region_ND[:, 1], '#10b4a7')
    ax1.scatter(sample_point[0], sample_point[1], marker='x', c='r', zorder=2)
    ax1.grid(linestyle='--', alpha=0.4, axis='both')

    # Also place axes captions
    label1 = np.array([45, -5, 1]) @ np.transpose(A)
    ax1.text(label1[0], label1[1], '%C2H6')
    label11 = np.array([95, -5, 1]) @ np.transpose(A)
    ax1.text(label11[0], label11[1], '0')
    label12 = np.array([5, -5, 1]) @ np.transpose(A)
    ax1.text(label12[0], label12[1], '100')
    label2 = np.array([-10, 55, 1]) @ np.transpose(A)
    ax1.text(label2[0], label2[1], '%H2')
    label21 = np.array([-7, 5, 1]) @ np.transpose(A)
    ax1.text(label21[0], label21[1], '0')
    label22 = np.array([-7, 95, 1]) @ np.transpose(A)
    ax1.text(label22[0], label22[1], '100')
    label3 = np.array([45, 55, 1]) @ np.transpose(A)
    ax1.text(label3[0], label3[1], '%CH4')
    label31 = np.array([5, 95, 1]) @ np.transpose(A)
    ax1.text(label31[0], label31[1], '0')
    label22 = np.array([95, 5, 1]) @ np.transpose(A)
    ax1.text(label22[0], label22[1], '100')


    # decision based on location
    PD = mplPath.Path(np.array(region_PD[:,0:2]))
    S = mplPath.Path(np.array(region_S[:,0:2]))
    O = mplPath.Path(np.array(region_O[:,0:2]))
    C = mplPath.Path(np.array(region_C[:,0:2]))
    ND = mplPath.Path(np.array(region_ND[:,0:2]))

    sample = (sample_point[0], sample_point[1])

    duval_4_area =  'Not applicable'

    if PD.contains_point(sample):
        duval_4_area = "PD"
    elif S.contains_point(sample):
        duval_4_area = "S"
    elif O.contains_point(sample):
        duval_4_area = "O"
    elif C.contains_point(sample):
        duval_4_area = "C"
    elif ND.contains_point(sample):
        duval_4_area = "ND"

    # Show the final plot
    ax1.set_xlim(0, 600)
    ax1.set_ylim(0, 550)
    
    # plt.switch_backend('AGG')
    # plt.title('Duval Triangle 1')
    # plt.plot()
    duval_graph = get_graph()
    
    return duval_graph, duval_4_area


def get_plot_duval_5(ethylene, methane, ethane):
    methane_percentage = (methane/(ethylene+ methane+ ethane))*100
    ethylene_percentage = (ethylene/(ethylene+ methane+ethane))*100
    ethane_percentage = (ethane/(ethylene+ methane+ ethane))*100

    # Define the transformation matrix
    A = np.array([[5, 2.5, 50], [0, 5 * np.sqrt(3)/2, 50], [0, 0, 1]])

    # Define a set of points for Duval triangle regions
    p = np.array([
        [0, 0, 1],          #0-p1
        [0, 100, 1],        #1-p2
        [100, 0, 1],        #2-p3
        [0, 45, 1],         #3-p4
        [0, 84, 1],         #4-p5
        [2, 82, 1],         #5-p6
        [0, 98, 1],         #6-p7
        [2,96, 1],         #7-p8
        [10,0, 1],        #8-p9
        [10,36, 1],        #9-p10
        [10,60, 1],        #10-p11
        [10,75, 1],        #11-p12
        [10,78, 1],        #12-p13
        [10,90, 1],        #13-p14
        [35,0, 1],        #14-p15
        [35,35, 1],        #15-p16
        [35, 54, 1],        #16-p17
        [35, 65, 1],        #17-p18
        [50, 38, 1],        #18-p19
        [50, 40, 1],        #19-p20
        [70, 0, 1],        #20-p21
        [70, 18, 1]])      #21-p22


    # Apply the coordinates transformation to all points
    v = p @ np.transpose(A)

    # Set one more sample point
    sample_point = np.array([ethylene_percentage, methane_percentage, 1]) @ np.transpose(A)

    # Define each of the regions by the coordinates of its angle points
    region_PD = v[[4,6,7,5], :]
    region_S = v[[3,4,11,9], :]
    region_O_1 = v[[0,3,9,8], :]
    region_O_2 = v[[4,11,12,13,1,6,7,5], :]
    region_C = v[[10,12,19,18,21,20], :]
    region_ND = v[[8,10,15,14], :]
    region_T2 = v[[12,13,17,16], :]
    region_T3_1 = v[[14,15,20], :]
    region_T3_2 = v[[16,17,2,20,21,18,19], :]

    # Plot the results
    fig, ax1 = plt.subplots()
    ax1.fill(region_PD[:, 0], region_PD[:, 1], '#2e962d')
    ax1.fill(region_S[:, 0], region_S[:, 1], '#bebe12')
    ax1.fill(region_O_1[:, 0], region_O_1[:, 1], '#ff642b')
    ax1.fill(region_O_2[:, 0], region_O_2[:, 1], '#ff642b')
    ax1.fill(region_C[:, 0], region_C[:, 1], '#f217d0')
    ax1.fill(region_ND[:, 0], region_ND[:, 1], '#10b4a7')
    ax1.fill(region_T2[:, 0], region_T2[:, 1], '#ff642b')
    ax1.fill(region_T3_1[:, 0], region_T3_1[:, 1], '#b46414')
    ax1.fill(region_T3_2[:, 0], region_T3_2[:, 1], '#b46414')
    ax1.scatter(sample_point[0], sample_point[1], marker='x', c='r', zorder=2)
    ax1.grid(linestyle='--', alpha=0.4, axis='both')

    # Also place axes captions
    label1 = np.array([45, -5, 1]) @ np.transpose(A)
    ax1.text(label1[0], label1[1], '%C2H6')
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
    PD = mplPath.Path(np.array(region_PD[:,0:2]))
    S = mplPath.Path(np.array(region_S[:,0:2]))
    O_1 = mplPath.Path(np.array(region_O_1[:,0:2]))
    O_2 = mplPath.Path(np.array(region_O_2[:,0:2]))
    C = mplPath.Path(np.array(region_C[:,0:2]))
    ND = mplPath.Path(np.array(region_ND[:,0:2]))
    T2 = mplPath.Path(np.array(region_T2[:,0:2]))
    T3_1 = mplPath.Path(np.array(region_T3_1[:,0:2]))
    T3_2 = mplPath.Path(np.array(region_T3_2[:,0:2]))

    sample = (sample_point[0], sample_point[1])

    duval_5_area =  'Not applicable'

    if PD.contains_point(sample):
        duval_5_area = "PD"
    elif S.contains_point(sample):
        duval_5_area = "S"
    elif O_1.contains_point(sample):
        duval_5_area = "O"
    elif O_2.contains_point(sample):
        duval_5_area = "O"
    elif ND.contains_point(sample):
        duval_5_area = "ND"
    elif C.contains_point(sample):
        duval_5_area = "C"
    elif T2.contains_point(sample):
        duval_5_area = "T2"
    elif T3_1.contains_point(sample):
        duval_5_area = "T3"
    elif T3_2.contains_point(sample):
        duval_5_area = "T3"

    # Show the final plot
    ax1.set_xlim(0, 600)
    ax1.set_ylim(0, 550)
    
    # plt.switch_backend('AGG')
    # plt.title('Duval Triangle 1')
    # plt.plot()
    duval_graph = get_graph()
    
    return duval_graph, duval_5_area