import socket, sys
from struct import *

def findPort():
    ''' since replay poker randomizes the port it uses, we have to find it '''
    #create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    # receive packets
    while True:
        packet = s.recvfrom(65565)
        #packet string from tuple
        packet = packet[0]
        #take first 20 characters for the ip header
        ip_header = packet[0:20]
        #now unpack them
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        s_addr = socket.inet_ntoa(iph[8]);tcp_header = packet[iph_length:iph_length+20]
        #now unpack them :)
        tcph = unpack('!HHLLBBHHH' , tcp_header)
        doff_reserved = tcph[4]
        tcph_length = doff_reserved >> 4
        h_size = iph_length + tcph_length * 4
        data_size = len(packet) - h_size
        #get data from the packet
        data = packet[h_size:]
        dest_port = tcph[1]
        source_port = tcph[0]
        if("playeraction" in data):
            return dest_port

def findIP():
    ''' i might need to find the ip at some point? '''
    #create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    # receive packets
    while True:
        packet = s.recvfrom(65565)
        #packet string from tuple
        packet = packet[0]
        #take first 20 characters for the ip header
        ip_header = packet[0:20]
        #now unpack them
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        s_addr = socket.inet_ntoa(iph[8]);tcp_header = packet[iph_length:iph_length+20]
        #now unpack them :)
        tcph = unpack('!HHLLBBHHH' , tcp_header)
        doff_reserved = tcph[4]
        tcph_length = doff_reserved >> 4
        h_size = iph_length + tcph_length * 4
        data_size = len(packet) - h_size
        #get data from the packet
        data = packet[h_size:]
        dest_port = tcph[1]
        source_port = tcph[0]
        if("playeraction" in data):
            return s_addr

def getPacket(port, ip):
    #create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except socket.error , msg:
        print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    # receive packets
    while True:
        packet = s.recvfrom(port)
        packet = packet[0]
        ip_header = packet[0:20]
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        ttl = iph[5]
        s_addr = socket.inet_ntoa(iph[8]);
        tcp_header = packet[iph_length:iph_length+20]
        tcph = unpack('!HHLLBBHHH' , tcp_header)
        doff_reserved = tcph[4]
        tcph_length = doff_reserved >> 4
        h_size = iph_length + tcph_length * 4
        data_size = len(packet) - h_size
        data = packet[h_size:]
        if("playeraction" in data):
            return data

