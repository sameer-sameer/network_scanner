#!/usr/bin/env python3

import argparse
import scapy.all as scapy

def get_arguments():
    parser = argparse.ArgumentParser(description="Network Scanner using ARP requests")
    parser.add_argument('-t', '--target', dest="target", required=True,
                        help="Specify the target IP range (e.g., 192.168.1.1/24)")
    args = parser.parse_args()
    return args.target

def scan(ip):
    # Create ARP request packet
    arp_request = scapy.ARP(pdst=ip)
    # Create Ethernet frame with broadcast destination
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # Combine both
    arp_request_broadcast = broadcast / arp_request

    print(f"\n[+] Scanning Network: {ip}")
    print("[*] Sending ARP requests via interface eth0...")

    try:
        # Send packets and receive responses
        answered_list = scapy.srp(
            arp_request_broadcast,
            timeout=3,
            verbose=True,
            iface="eth0"  # Force interface
        )[0]
    except PermissionError:
        print("[-] Run the script as root or with sudo.")
        return []

    print(f"[+] {len(answered_list)} devices responded.\n")

    client_list = []
    for element in answered_list:
        print(f"[DEBUG] Found: {element[1].psrc} --> {element[1].hwsrc}")
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)

    return client_list

def print_result(results_list):
    print("\nIP Address\t\tMAC Address")
    print("-----------------------------------------")
    for client in results_list:
        print(f"{client['ip']}\t\t{client['mac']}")

if __name__ == "__main__":
    target_ip = get_arguments()
    scan_result = scan(target_ip)
    print_result(scan_result)
