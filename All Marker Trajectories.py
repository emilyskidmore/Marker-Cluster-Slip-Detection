marker_data = c3d['data']['points']  # shape: (4, N_markers, N_frames)
labels = c3d['parameters']['POINT']['LABELS']['value']
print(labels)

for i in labels:
    marker_index = labels.index(i)
    x = marker_data[0, marker_index, :]
    y = marker_data[1, marker_index, :]
    z = marker_data[2, marker_index, :]
    fig = plt.figure() 
    ax = fig.add_subplot(111, projection = '3d')
    ax.plot(x, y,z, label = 'Marker Trajectory', color = 'orange')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'3D Marker Trajectory - {i}')
    ax.legend()
    plt.show()


    