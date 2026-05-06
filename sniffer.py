from scapy.all import sniff, IP, TCP, UDP
from colorama import Fore, Style, init
from datetime import datetime
import os

init(autoreset=True)

if not os.path.exists("logs"):
    os.makedirs("logs")

log_file = "logs/packets.txt"

print(Fore.CYAN + "=" * 70)
print(Fore.GREEN + "         CODEALPHA - ADVANCED NETWORK SNIFFER")
print(Fore.CYAN + "=" * 70)

def process_packet(packet):
    try:
        if packet.haslayer(IP):

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            packet_size = len(packet)

            protocol_name = "OTHER"
            src_port = "-"
            dst_port = "-"

            if packet.haslayer(TCP):
                protocol_name = "TCP"
                src_port = packet[TCP].sport
                dst_port = packet[TCP].dport

            elif packet.haslayer(UDP):
                protocol_name = "UDP"
                src_port = packet[UDP].sport
                dst_port = packet[UDP].dport

            output = (
                f"\n[{timestamp}]\n"
                f"Source IP        : {src_ip}\n"
                f"Destination IP   : {dst_ip}\n"
                f"Protocol         : {protocol_name}\n"
                f"Source Port      : {src_port}\n"
                f"Destination Port : {dst_port}\n"
                f"Packet Size      : {packet_size} bytes\n"
            )

            print(Fore.YELLOW + output)
            print(Fore.BLUE + "-" * 70)

            with open(log_file, "a") as file:
                file.write(output)
                file.write("-" * 70 + "\n")

    except Exception as e:
        print(Fore.RED + f"Error: {e}")

print(Fore.GREEN + "\n[*] Sniffing Started Successfully...")
print(Fore.GREEN + "[*] Press CTRL + C to Stop\n")

sniff(prn=process_packet, store=False)