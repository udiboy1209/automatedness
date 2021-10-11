---
title: Research Projects
template: projects
---

<style type="text/css">
  img {
    max-width: 40%;
  }
</style>

##### [Disabling Prefetcher to Amplify Cache Side-Channels](/2019/masters-thesis.html)
Cache side channels are well known for being effective in extracting data from modern
cryptographic ciphers. Some other hardware accessing the cache, e.g. prefetcher, degrades the quality of the
side channel by introducing false positives in the attacker’s data. This project works on
a method to disable the prefetcher by preventing it from generating memory accesses
and interfering with side channels running in the cache.

![prefetch attack](/images/prefetch_attack.png)

##### [Side-channel using Reorder Buffer](/2019/masters-thesis.html)

Reorder buffer is an important component of an Out-of-Order core utilised in the Tomasulo algorithm.
 In an SMT context, this Reorder Buffer may either be shared among
threads or statically partitioned. 
This allows for a side-channel leakage to occur because a shared Reorder Buffer
will lead to interference among the two thread’s IPC. 

![rob side channel](/images/rob_side_channel.png)

##### [Execution Migration in Heterogeneous-ISA Dynamic Core](/2018/hidc.html)

Prior research has shown great potential of Heterogeneous-ISA chip multiprocessors in terms of
performance and energy gains. Implementation of such a processor involves one major challenge
which is migrating execution of a process from one ISA to the other. Any implementation of such
a system has to take care of Memory Image consistency for both ISAs and perform necessary
transformations during migration. The other main challenge is determining possible points of
migration, and methods of identifying whether migration is beneficial, dynamically during runtime.
To harness the benefits of ISA diversity fully, execution migration cost needs to be low enough so
that frequent migration can be justified performance-wise.
