---
title: Disabling Prefetcher to Amplify Side-Channels
date: 2019-06-30
category: Research
tag: Master's Thesis
summary: Cache side channels are well known for being effective in extracting data from modern cryptographic ciphers. Some other hardware accessing the cache, e.g. prefetcher, degrades the quality of the side channel by introducing false positives in the attacker’s data. This project works on a method to disable the prefetcher by preventing it from generating memory accesses and interfering with side channels running in the cache.
image: prefetch_attack.png
image_size: side
---

This is Chapter V of my [Master's thesis](/pdfs/masters_thesis.pdf).
Codes for prefetcher-disabling attack and
cache reverse engineering are present on [github](https://github.com/udiboy1209/hardware-security-cpu-gpu).

#### Thesis abstract

The current trends in computer architecture are increasingly focusing on sharing com-
puting resources among multiple programs and users. Multiple programs can share a
single core using simultaneous multi-threading which is widely supported by most of the
processors and operating systems. Virtual machine technology allows running multiple
OS instances on the same processor. While the software and hardware of VMs or multi-
threaded OS is able to isolate illegal access of data to prevent software vulnerabilities,
it cannot prevent the leakage of sensitive data via side-channels which exist due to de-
sign flaws in shared hardware like caches, branch predictors, prefetchers. Attackers have
successfully been able to extract encryption keys of various cryptographically secure algorithms
like AES and RSA. These leakages are possible and viable because hardware
design does not take care of the security against such side-channels. Moreover, software
trojans can use these leakages to create a covert channel of communication unknown and
undetectable by the OS and any software anti-viruses. Also, software exploits like return
oriented programming and buffer overflow attacks can be thwarted more effectively with
hardware solutions rather than software defenses. It has become increasingly necessary
to consider data security as an important metric for hardware design.
An introduction of side-channel attacks is provided as motivation for including security
as an important aspect of hardware design. We describe how data dependent execution,
which is present in AES and RSA ciphers, can be exploited by different cache side chan-
nels like Prime+Probe and Flush+Reload. As an inital step to cache side channels, we
have introduced a method to reverse engineer cache parameters using microbenchmarking
programs. We propose an attack to disable the prefetcher by preventing it from generating
memory accesses and interfering with side channels running in the cache. The attacker
is designed to work on a Stride Prefetcher, and is implemented and tested with OpenSSL
AES victim program. Results show that it is able to significantly reduce the number of
prefetches generated to almost 0. We also propose a hypothetical side channel which uses
the shared Reorder Buffer (ROB) on SMT cores. This side channel can be used to detect
data-dependent stalls in a victim program.


