import socket
import sys
import traceback


def client(log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    # sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.
    sock.connect(('127.0.0.1', 10000))

    # you can use this variable to accumulate the entire message received back
    # from the server

    received_messages = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    keep_sending = True
    try:
        while keep_sending is True:
            msg = input("input your message to send > ")
            print('sending "{0}"'.format(msg), file=log_buffer)

            # TODO: send your message to the server here.
            sock.sendall(msg.encode('utf-8'))

            # TODO: the server should be sending you back your message as a series
            #       of 16-byte chunks. Accumulate the chunks you get to build the
            #       entire reply from the server. Make sure that you have received
            #       the entire message and then you can break the loop.
            #
            #       Log each chunk you receive.  Use the print statement below to
            #       do it. This will help in debugging problems

            # chunk = ''
            # print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
            received_message = ''
            while True:
                buffer_size = 16
                data = sock.recv(buffer_size)
                chunk = data.decode('utf8')
                print('received "{0}"'.format(chunk), file=log_buffer)
                received_message += chunk

                if len(data) < 16:
                    break

            print('the full message was: {}'.format(received_message))
            received_messages += received_message + '\n'
            exit_question = ''
            while exit_question != 'y' and exit_question != 'n':
                exit_question = input("send another? (y/n) > ")
            if exit_question == 'y':
                keep_sending = True
            if exit_question == 'n':
                keep_sending = False

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.

        sock.close()

        print('closing socket', file=log_buffer)

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.
        print('the full message log was:\n{}'.format(received_messages))
        return received_messages


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     usage = '\nusage: python echo_client.py "this is my message"\n'
    #     print(usage, file=sys.stderr)
    #     sys.exit(1)

    # msg = sys.argv[1]
    client()
