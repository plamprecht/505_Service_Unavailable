# 505_Service_Unavailable

# Contemporary Topics in CS, 2021/2022

## Literature

[1] is the work presented in the kick-off session. While centered around GPU memory benchmarking, it serves as a useful work to introduce the reader into the general topic of benchmarking and comparing multiple systems. In [2], a slightly older work, Simon Pennycook briefly discusses possible definitions of performance portability. Similarly, it's an overview of the topic and highlights some issues we face with it. [3] is quite short and old, doesn't take itself too seriously, and gives bad examples of how NOT to deal with benchmarking and data reporting in the 1990s. [4] is a much more comprehensive work that builds upon that and tries to give both a meta-study on performance reports as well as guidelines on how to do benchmarking and reporting properly. [5] represents another work on performance portability, introducing several benchmarks, classifying them and reporting their performance on several architectures. [6] describes a modern C++-based implementation of the NAS Parallel benchmarks (originally written in Fortran at NASA, https://www.nas.nasa.gov/software/npb.html).

- [1] Tom Deakin, James Price, Matt Martineau, Simon McIntosh-Smith: GPU-STREAM v2.0: Benchmarking the Achievable Memory Bandwidth of Many-Core Processors Across Diverse Parallel Programming Models, ISC High Performance 2016, Springer.
- [2] Pennycook, Simon J., Jason D. Sewall, and Victor W. Lee. "A metric for performance portability." arXiv preprint arXiv:1611.07409 (2016).
- [3] David H. Bailey. "Twelve Ways to Fool the Masses When Giving Performance Results on Parallel Computers", Supercomputing Review, Aug. 1991, pg. 54--55
- [4] Hoefler, Torsten, and Roberto Belli. "Scientific benchmarking of parallel computing systems: twelve ways to tell the masses when reporting performance results." Proceedings of the international conference for high performance computing, networking, storage and analysis. 2015.
- [5] T. Deakin et al., "Performance Portability across Diverse Computer Architectures," 2019 IEEE/ACM International Workshop on Performance, Portability and Productivity in HPC (P3HPC), 2019, pp. 1-13, doi: 10.1109/P3HPC49587.2019.00006.
- [6] Júnior Löff, Dalvan Griebler, Gabriele Mencagli, Gabriell Araujo, Massimo Torquati, Marco Danelutto, Luiz Gustavo Fernandes. "The NAS Parallel Benchmarks for evaluating C++ parallel programming frameworks on shared-memory architectures", Future Generation Computer Systems, Volume 125, 2021.

## Benchmarks

- Memory-intensive
    - `Stream`: https://github.com/jeffhammond/STREAM (mirrored from https://www.cs.virginia.edu/stream/); the original Stream memory benchmark, well-known in the community.
    - `BabelStream`: https://github.com/UoB-HPC/BabelStream ; an updated version of Stream mainly aimed at GPU architectures, but also provides e.g. an OpenMP implementation for CPUs.

- Compute-intensive
    - NAS Parallel Benchmarks: https://github.com/GMAP/NPB-CPP (adapted from https://www.nas.nasa.gov/software/npb.html); well-known in the community and provides several kernels and micro-applications that represent classes of larger HPC applications.

## Tools

- `perf`: A performance counter analysis tool that can report various hardware metrics, depending on the CPU type
- `/usr/bin/time -v`: A time measurement tool that also reports some statistics tracked by the operating system
