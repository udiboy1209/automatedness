---
title: Tamper-Proof Network Traffic Measurements on a NIC for Intrusion Detection
date: 2023-01-01
category: Research
tag: PhD Project
summary: I have developed a framework that leverages the network interface card (NIC) to collect tamper-proof network traffic measurements for intrusion detection systems. Rootkits that compromise the host OS can tamper host-side network measurements but cannot easily touch peripherals that operate outside the host OS domain, such as the NIC. The framework can collect reliably accurate measurements with negligible impact to network performance.
image: /images/nic.png
featured: true
image_size: side
---

Cyber attacks can infect networked devices with
rootkits that provide full-system access of the operating system
to malicious actors. Rootkits can hide malicious network activity
by tampering with network traffic monitoring on the host and
interfere with the functioning of host-based intrusion detection
systems (HIDS). Network interface cards (NICs) operate outside
the host domain, so they cannot be tampered with easily by the
rootkit. We present a framework that leverages the NIC to collect
tamper-proof network traffic measurements for the HIDS. We
provide two efficient implementations to collect measurements
of high speed traffic (10Gbps), the Associative Table and the
Count-Min Sketch. Our framework can collect reliably accurate
measurements with negligible impact to network performance.
The network throughput with measurement collection is within
99.5% of the throughput without collection. The implementation
adds only 12 to 23 microseconds of latency.
