# 🔍 Network Scanner

## 📌 Overview
This is a **Python-based network scanner** that detects devices on a given subnet by sending ARP (Address Resolution Protocol) requests. It helps **ethical hackers, cybersecurity professionals, and network administrators** to identify connected devices along with their **IP and MAC addresses**.

## 🚀 Features
- Scans a target IP range using ARP requests.
- Displays **IP and MAC addresses** of all connected devices.
- Uses **Scapy** for network packet crafting and analysis.
- Works on both **Linux and Windows** (requires admin privileges on Windows).

## 🛠️ Installation & Setup
### 🔹 **Prerequisites**
Ensure you have installed Python and the required libraries.

#### **Step 1: Install Python**
🔗 [Download Python](https://www.python.org/downloads/) if not installed.

#### **Step 2: Install Dependencies**
Open a terminal (Linux/macOS) or Command Prompt (Windows) and run:
```bash
pip install scapy


💻 Usage:
To run the network scanner, open a terminal and execute:
python network_scanner.py -t 192.168.1.1/24

Important Notes:
Run as Administrator: The script needs root/admin privileges to send ARP requests.
Linux/macOS: Use sudo before the command.
Windows: Open Command Prompt as Administrator.
Windows requires Npcap to be installed (Download Npcap).

📷 Example Output:
IP Address         MAC Address
-----------------------------------------
192.168.1.1       00:1A:2B:3C:4D:5E
192.168.1.2       11:22:33:44:55:66
