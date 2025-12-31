---
title: Cybersecurity LLM Agents for solving CTF Challenges
date: 2024-08-25
category: Research
tag: PhD Project
summary:  Developing LLM cybersecurity capabilities is important as LLMs are very useful in automating cybersecurity analysis with their vast breadth of knowledge. I worked on building the NYU CTF Bench dataset of CTF challenges to test LLM cybersecurity capabilities. I also worked on the EnIGMA agent with interactive agent tools and enhanced agent-computer interface.
image: /images/enigma.png
featured: true
---

### NYU CTF Bench

**Main website:** [nyu-llm-ctf.github.io](https://nyu-llm-ctf.github.io).

LLM capacity to solve Capture the Flag (CTF) challenges in cybersecurity
has not been thoroughly evaluated. To address this, we develop a novel method
to assess LLMs in solving CTF challenges by creating a scalable, open-source
benchmark database specifically designed for these applications. This database
includes metadata for LLM testing and adaptive learning, compiling a diverse range
of CTF challenges from popular competitions. Utilizing the advanced function
calling capabilities of LLMs, we build a fully automated system with an enhanced
workflow and support for external tool calls. Our benchmark dataset and automated
framework allow us to evaluate the performance of five LLMs, encompassing
both black-box and open-source models. This work lays the foundation for future
research into improving the efficiency of LLMs in interactive cybersecurity tasks
and automated task planning. By providing a specialized dataset, our project offers
an ideal platform for developing, testing, and refining LLM-based approaches
to vulnerability detection and resolution. Evaluating LLMs on these challenges
and comparing with human performance yields insights into their potential for
AI-driven cybersecurity solutions to perform real-world threat management.

### EnIGMA: Enhanced Interactive Generative Model Agent for CTF Challenges

![enigma agent](/images/enigma.png)

**Main website:** [enigma-agent.com](https://enigma-agent.com).

Although LM agents are demonstrating
growing potential in many domains, their success in cybersecurity has been limited due to simplistic design and the lack
of fundamental features for this domain. We present EnIGMA,
an LM agent for autonomously solving Capture The Flag
(CTF) challenges. EnIGMA introduces newAgent-Computer
Interfaces (ACIs) to improve the success rate on CTF challenges. We establish the novel Interactive Agent Tool concept,
which enables LM agents to run interactive command-line
utilities essential for these challenges. Empirical analysis of
EnIGMA on over 350 CTF challenges from three different
benchmarks indicates that providing a robust set of new tools
with demonstration of their usage helps the LM solve complex problems and achieves state-of-the-art results on the
NYU CTF and Intercode-CTF benchmarks. Finally, we discuss insights on design and agent behavior on cybersecurity
tasks that highlight the need to adapt real-world tools for LM agents.
