from scapy.all import IP, ICMP,TCP, sr1
import sys
def icmp_probe(ip):
    icmp_packet = IP(dst=ip)/ICMP()
    resp_packet = sr1(icmp_packet, timeout=10, verbose=False)
    return resp_packet != None

def syn_scan(ip, port): 
    packet = IP(dst=ip)/TCP(dport=port, flags='S')
    resp_packet = sr1(packet, timeout=1, verbose=False)
    
    if resp_packet.getlayer('TCP').flags == 'SA':
        print('open')
    else:
        print('filtered|closed')


if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])

    if icmp_probe(ip):
        syn_ack_packet = syn_scan(ip, port)
    else:
        print("ICMP Probe Failed")
