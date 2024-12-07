---
title: Reverse Engineering Math Equations from Binaries: Symbolic and Neural Approaches
date: 2023-03-23
category: Research
tag: PhD Project
summary: Reverse engineering math equations from binaries of embedded systems is immensely useful to analyze the implemented mathematical models for security purposes. I have developed two frameworks for reverse engineering math equations: REMaQE, an automated dynamic analysis framework utilizing symbolic execution; and REMEND, a neural decompilation framework with enhanced disassembler for extracting math equations using single pass static analysis.
image: remaqe.png
image_size: full
---

### REMaQE

REMaQE is a symbolic approach for reverse engineering math equations, based on the `angr` symbolic execution framework.

![REMaQE overview](/images/remaqe.png)

Cybersecurity attacks on embedded devices for industrial control systems and cyber-physical systems may cause catastrophic physical damage as well as economic loss.
This could be achieved by infecting device binaries with malware that modifies the physical characteristics of the system operation.
Mitigating such attacks benefits from reverse engineering tools that recover sufficient semantic knowledge in terms of mathematical equations of the implemented algorithm.
Conventional reverse engineering tools can decompile binaries to low-level code, but offer little semantic insight.
We propose the REMaQE automated framework for reverse engineering of math equations from binary executables.

![REMaQE pipeline with tmon](/images/remaqe_flow.png)

The figure above shows the three stages of the REMaQE pipeline operating on the tmon binary: parameter analysis, symbolic execution, and algebraic simplification.
Each stage processes the binary further to extract the equations.

**Key Results**

 - Improving over state-of-the-art, REMaQE handles equation parameters accessed via registers, the stack, global memory, or pointers, and can reverse engineer equations from object-oriented implementations such as C++ classes.
 - Using REMaQE, we discovered a bug in the Linux kernel thermal monitoring tool [tmon](https://github.com/torvalds/linux/blob/v6.3/tools/thermal/tmon/pid.c).
 - To evaluate REMaQE, we generate a dataset of 25,096 binaries with math equations implemented in C and Simulink. REMaQE successfully recovers a semantically matching equation for all 25,096 binaries.
 - REMaQE executes in 0.48 seconds on average and in up to 2 seconds for complex equations.

### REMEND

REMEND is an alternate neural approach to REMaQE, using Transformers for neural decompilation of binaries to extract math equations.

Analysis of binary executables implementing mathematical equations can benefit from the reverse engineering
of semantic information about the implementation. Traditional algorithmic reverse engineering tools either
do not recover semantic information or rely on dynamic analysis and symbolic execution with high reverse
engineering time. Recently, neural methods for decompilation have been developed to recover human-like
source code, but they do not extract semantic information explicitly. We develop a neural decompilation
framework called REMEND to extract semantic information from binaries in the form of math equations to
explicitly recover program semantics like data flow and order of operations. REMEND is the first work to apply
neural decompilation techniques to reverse engineer math equations. We train REMEND on a synthetically
generated dataset and we obtain an accuracy of 89.8% to 92.4% across three Instruction Set Architectures (ISAs),
three optimization levels, and two programming languages, extending the capability of state-of-the-art neural
decompilers. We achieve high accuracy with a small model of upto 12 million parameters and an average
execution time of 0.132 seconds per function. On a real-world dataset collected from open-source programs,
REMEND achieves 13.4% higher accuracy than state-of-the-art neural decompilers.
