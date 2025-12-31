---
title: Execution Migration on HIDC
date: 2018-07-13
category: Research
tag: R&D project
summary: Heterogeneous-ISA Dynamic Core is a reconfigurable composite core which supports runtime migration between multiple ISAs. Runtime migration needs to ensure the consistency of memory image for both ISAs. This project implements a methodology for Exection Migration of HIDC between x86 and ARM ISAs. To harness the benefits of ISA diversity fully, execution migration cost needs to be low enough so that frequent migration can be justified performance-wise.
---

Full report is available [here](/pdfs/hidc_report.pdf).

#### Abstract

Prior research has shown great potential of Heterogeneous-ISA chip multiprocessors in terms of
performance and energy gains. Implementation of such a processor involves one major challenge
which is migrating execution of a process from one ISA to the other. Any implementation of such
a system has to take care of Memory Image consistency for both ISAs and perform necessary
transformations during migration. The other main challenge is determining possible points of
migration, and methods of identifying whether migration is beneficial, dynamically during runtime.
To harness the benefits of ISA diversity fully, execution migration cost needs to be low enough so
that frequent migration can be justified performance-wise.

#### Memory Image Consistency

A program during execution accesses three different types of memory: Global, Stack and Heap.
Global memory is fixed at compile time hence can be maintained same for both ISAs. Heap
memory grows during runtime and is only created according to a few functions like ‘malloc’. If
implementation of these functions are same for both ISAs, then the image formed will be consistent
. The stack memory is arranged by the compiler but it is created during runtime throughout
execution of a function. The stack is very frequently accessed during runtime hence rearranging it
for the purpose of image consistency would hit single threaded performance very hard.
The solution to this is to transform stack memory from layout created by one ISA to the layout
expected by the other ISA. Stack transformation is the part which consumes the most time during
execution migration.

