import math

def bin_to_int(bin):
    return math.floor(sum([math.pow(2,i) for i in range(len(bin)-1,-1,-1) if bin[len(bin)-1-i]=='1']))

def hex_to_bin(hex):
    bin=""
    for val in hex:
        if val == "0":
            bin+="0000"
        elif val == "1":
            bin+="0001"
        elif val == "2":
            bin+="0010"
        elif val == "3":
            bin+="0011"
        elif val == "4":
            bin+="0100"
        elif val == "5":
            bin+="0101"
        elif val == "6":
            bin+="0110"
        elif val == "7":
            bin+="0111"
        elif val == "8":
            bin+="1000"
        elif val == "9":
            bin+="1001"
        elif val == "A":
            bin+="1010"
        elif val == "B":
            bin+="1011"
        elif val == "C":
            bin+="1100"
        elif val == "D":
            bin+="1101"
        elif val == "E":
            bin+="1110"
        else: #F
            bin+="1111"
    return bin

def handle_packet_4(packet):
    has_next=True
    while(has_next):
        if packet[0]=='0': has_next=False
        packet=packet[5:]
    return packet

def handle_packet_X_0(packet):
    version=0
    sub_packets_length=bin_to_int(packet[:15]) ; packet = packet[15:]
    sub_packets=packet[:sub_packets_length] ; packet = packet[sub_packets_length:]
    while(len(sub_packets) > 0):
        sub_packets,to_add=identify_packet(sub_packets)
        version+=to_add
    return packet,version

def handle_packet_X_1(packet):
    version=0
    nb_of_direct_sub_packet=bin_to_int(packet[:11]) ; packet = packet[11:]
    while(nb_of_direct_sub_packet > 0):
        nb_of_direct_sub_packet-=1
        packet,to_add = identify_packet(packet)
        version+=to_add
    return packet,version

def identify_packet(packet):
    if not "1" in packet : return 0

    version = bin_to_int(packet[:3]) ; packet = packet[3:]
    type = packet[:3] ; packet = packet[3:]
    if type=="100": #ID4 -> literal number
        packet = handle_packet_4(packet)
    else:
        length_type_id=packet[0] ; packet = packet[1:]
        if length_type_id=="0":
            packet,to_add = handle_packet_X_0(packet)
            version+=to_add
        else:
            packet,to_add = handle_packet_X_1(packet)
            version+=to_add

    return packet,version

if __name__ == "__main__":
    f = open("AdventOfCode2021\\D16\\input.txt")
    input = f.read()
    f.close()
    master_pack = hex_to_bin(input)
    versions = identify_packet(master_pack)[1]
    print(versions)