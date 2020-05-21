import socket
import sys


def query_ports(lower, upper):
    """
    Print the port with it's service, and return a list of all ports with their service.
    """
    ports_data = []
    for port in range(lower, upper + 1):
        try:
            port_data = "port: {0}, service: {1}".format(port, socket.getservbyport(port))
            print (port_data)
            ports_data.append(port_data)
        except OSError:
            pass
    return ports_data


if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage = '\nusage: ports.py upper_bound lower_bound\n'
        print(usage)
        sys.exit(1)

    if int(sys.argv[1]) < 0 or int(sys.argv[2]) > 65535:
        usage = '\nvalid only for 0-65535\n'
        print(usage)
        sys.exit(1)

    query_ports(int(sys.argv[1]), int(sys.argv[2]))
