#!/usr/bin/env python

import argparse
import scapy.all as scapy

def get_arguments():
    parser = argparse.ArgumentParser(description="Network Scanner using ARP requests")
    parser.add_argument('-t', '--target', dest="target", required=True,
                        help="Specify the target IP range (e.g., 192.168.1.1/24)")
    args = parser.parse_args()
    return args.target

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(results_list):
    print("\nIP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

target_ip = get_arguments()
scan_result = scan(target_ip)
print_result(scan_result)
