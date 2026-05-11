# 🌐 Advanced Network Packet Sniffer

A Python-based network packet sniffer developed for the CodeAlpha Cyber Security Internship.

This project captures live network packets, extracts important network information, and logs packet details such as source IP, destination IP, protocol type, ports, and packet size in real time. :contentReference[oaicite:0]{index=0}

---

## 🚀 Features

- Real-time packet sniffing
- TCP and UDP packet detection
- Source & destination IP tracking
- Source & destination port monitoring
- Packet size analysis
- Timestamp logging
- Colored terminal output
- Automatic packet logging to file

---

## 🛠 Technologies Used

- Python
- Scapy
- Colorama

---

## 📂 Project Structure

```bash
CodeAlpha_BasicNetworkSniffer/
│
├── sniffer.py
├── requirements.txt
├── README.md
│
└── logs/
    └── packets.txt
```

---

## ⚙️ Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

Dependencies used: :contentReference[oaicite:1]{index=1}

```txt
scapy
colorama
```

---

## ▶️ Run Project

```bash
python sniffer.py
```

---

## 📄 Logged Information

The sniffer captures and logs:

- Timestamp
- Source IP
- Destination IP
- Protocol Type
- Source Port
- Destination Port
- Packet Size

Example packet logs are stored in:

```bash
logs/packets.txt
```

Sample captured packets include TCP and UDP traffic with IP addresses and packet sizes. :contentReference[oaicite:2]{index=2}

---

## 🧪 Functionality

The project uses Scapy to:
- capture live network packets,
- analyze packet layers,
- identify protocols,
- extract packet metadata,
- display packets in real time,
- save logs automatically.

---

## 👨‍💻 Author

Naveen R  
Cyber Security Intern — CodeAlpha
