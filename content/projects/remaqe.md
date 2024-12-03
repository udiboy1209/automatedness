---
title: REMaQE: Reverse Engineering Math Equations from Executables
date: 2023-03-23
category: Research
tag: PhD Project
summary: REMaQE is an automated framework for reverse engineering of math equations from binary executables. Improving over state-of-the-art, REMaQE handles equation parameters accessed via registers, the stack, global memory, or pointers, and can reverse engineer equations from object-oriented implementations such as C++ classes. Using REMaQE, we discovered a bug in the Linux kernel thermal monitoring tool "tmon." Real-time execution of REMaQE enables integration in an interactive math-oriented reverse engineering workflow.
image: remaqe.png
image_size: full
---

```latex
@article{udeshi2024remaqe,
    author = {Udeshi, Meet and Krishnamurthy, Prashanth and Pearce, Hammond and Karri, Ramesh and Khorrami, Farshad},
    title = {REMaQE: Reverse Engineering Math Equations from Executables},
    publisher = {Association for Computing Machinery},
    year = {2024}, volume = {8}, number = {4},
    doi = {10.1145/3699674},
    journal = {ACM Trans. Cyber-Phys. Syst.},
    numpages = {25},
}
```

### Introduction

![REMaQE overview](/images/remaqe.png)

Cybersecurity attacks on embedded devices for industrial control systems and cyber-physical systems may cause catastrophic physical damage as well as economic loss.
This could be achieved by infecting device binaries with malware that modifies the physical characteristics of the system operation.
Mitigating such attacks benefits from reverse engineering tools that recover sufficient semantic knowledge in terms of mathematical equations of the implemented algorithm.
Conventional reverse engineering tools can decompile binaries to low-level code, but offer little semantic insight.
We propose the REMaQE automated framework for reverse engineering of math equations from binary executables.

### Key Results

 - Improving over state-of-the-art, REMaQE handles equation parameters accessed via registers, the stack, global memory, or pointers, and can reverse engineer equations from object-oriented implementations such as C++ classes.
 - Using REMaQE, we discovered a bug in the Linux kernel thermal monitoring tool [tmon](https://github.com/torvalds/linux/blob/v6.3/tools/thermal/tmon/pid.c).
 - To evaluate REMaQE, we generate a dataset of 25,096 binaries with math equations implemented in C and Simulink. REMaQE successfully recovers a semantically matching equation for all 25,096 binaries.
 - REMaQE executes in 0.48 seconds on average and in up to 2 seconds for complex equations.

### Pipeline

![REMaQE pipeline with tmon](/images/remaqe_flow.png)

The figure above shows the three stages of the REMaQE pipeline operating on the tmon binary: parameter analysis, symbolic execution, and algebraic simplification.
Each stage processes the binary further to extract the equations.


