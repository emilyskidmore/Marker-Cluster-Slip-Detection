L_Thigh = 'LLTHI'
L_Thigh_data = df[df['Marker']== L_Thigh]
print(L_Thigh_data)

X = L_Thigh_data[['Frame','X']]
Y = L_Thigh_data[['Frame','Y']]
Z = L_Thigh_data[['Frame','Z']]
print(X)
print(Y)
print(Z)

fig, axs = plt.subplots(nrows = 3, ncols=1, figsize=(10, 7.5), layout='constrained')
x_axis = X['Frame']
y_x = X['X']
y_y = Y['Y']
y_z = Z['Z']
axs[0].plot(x_axis, y_x)
axs[0].set_title('x-coordinate trajectory')

axs[1].plot(x_axis, y_y)
axs[1].set_title('y-coordinate trajectory')

axs[2].plot(x_axis, y_z)
axs[2].set_title('z coordinate trajectory')

plt.show()