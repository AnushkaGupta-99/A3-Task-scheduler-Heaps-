# A3-Task-scheduler-Heaps-

This assignment simulates a scheduling system where m crewmates process n treasure items, each with an arrival time and processing size. The goal is to efficiently manage the scheduling and processing of treasures while adhering to a defined scheduling policy. The solution focuses on using heaps to optimize selection based on current load and priority functions.

Files and Their Purpose
heap.py: Implements a generalized min-heap with a custom comparator.

crewmate.py: Models individual crewmates with their assigned treasures and logic to choose which treasure to process.

treasure.py: Defines the Treasure class with attributes like ID, arrival time, size, and completion time.

straw_hat.py: Manages the overall scheduling, assignment, and computation of completion times.

custom.py: Contains helper functions and custom classes used to keep other files clean.

