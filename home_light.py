# coding=utf-8
import socket


def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 要发送的ip地址和端口（元组的形式）
    send_addr = ('192.168.3.7', 50003)
    print('send_addr = ', send_addr)

    while True:
        string = str(input('weclome please input witch switch:'))
        # 要发送的信息
        b = bytes(string, encoding='utf-8')
        udp_socket.sendto(b, send_addr)


if __name__ == "__main__":
    main()
