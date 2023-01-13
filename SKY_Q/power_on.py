import socket

# Set the IP address of the Sky Q box
sky_q_ip = 'your_sky_q_ip'

# Create a socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sky_q_ip, 49160))

# Send the "power on" command
s.sendall(b'\x64\x00\x10\x00\x00\x00\x08\x01\x00\x00\x00\x00\x00\x00\x00\x00')

# Close the socket connection
s.close()
