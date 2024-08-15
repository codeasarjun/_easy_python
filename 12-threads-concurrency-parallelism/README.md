## Overview

This Python script demonstrates basic usage of threading by running multiple threads concurrently.

Each thread performs a simple task: printing a sequence of numbers with a delay between each print. 

This example is designed to illustrate how threading can be used to perform concurrent operations in Python.

## Files
### 1. `threading.py`

- **Definition**: The `threading` module provides a way to run multiple threads (smaller units of a process) within a single process. Threads share the same memory space, which makes it easier to share data but also requires careful synchronization to avoid conflicts.

- **Use Case**: Ideal for I/O-bound tasks where tasks spend time waiting for external resources (e.g., file I/O, network operations). Threads can help in performing multiple tasks concurrently in a single process.

- **Key Features**:
  - **Thread Class**: Create and manage threads.
  - **Locks, Semaphores**: Synchronize access to shared resources.

- **Example**: Printing numbers with a delay using multiple threads.

### 2. `multiprocessing.py`

- **Definition**: The `multiprocessing` module allows the creation of multiple processes, each with its own Python interpreter and memory space. This helps bypass the Global Interpreter Lock (GIL) and is suitable for CPU-bound tasks.

- **Use Case**: Ideal for tasks that require heavy computation and can benefit from parallel execution across multiple CPU cores. Each process operates independently with its own memory space, which avoids conflicts but requires inter-process communication (IPC).

- **Key Features**:
  - **Process Class**: Create and manage processes.
  - **Pipes, Queues**: Facilitate communication between processes.

- **Example**: Performing computational tasks like processing large datasets in parallel.

### 3. `asyncio.py`

- **Definition**: The `asyncio` module provides a framework for writing asynchronous code using coroutines, event loops, and tasks. It allows for non-blocking operations and efficient management of multiple tasks within a single thread.

- **Use Case**: Best for I/O-bound and high-level structured network code where you need to handle many tasks concurrently without blocking. Suitable for tasks that involve waiting for I/O operations to complete.

- **Key Features**:
  - **Event Loop**: Manages and dispatches events.
  - **Coroutines**: Define asynchronous functions that can be paused and resumed.
  - **Tasks**: Represent coroutines scheduled for execution.

- **Example**: Fetching web pages concurrently without blocking the execution.



## Comparison of Concurrency Models

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>threading</th>
      <th>multiprocessing</th>
      <th>asyncio</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Definition</strong></td>
      <td>Provides a way to run multiple threads within a single process. Threads share the same memory space.</td>
      <td>Allows the creation of multiple processes, each with its own memory space and Python interpreter.</td>
      <td>Provides a framework for writing asynchronous code using coroutines, event loops, and tasks.</td>
    </tr>
    <tr>
      <td><strong>Concurrency Model</strong></td>
      <td>Thread-based concurrency.</td>
      <td>Process-based concurrency.</td>
      <td>Asynchronous I/O with coroutines.</td>
    </tr>
    <tr>
      <td><strong>Best Suited For</strong></td>
      <td>I/O-bound tasks where threads spend time waiting for external resources.</td>
      <td>CPU-bound tasks that require parallel execution and can benefit from multiple CPU cores.</td>
      <td>I/O-bound tasks where you need to handle many operations concurrently without blocking.</td>
    </tr>
    <tr>
      <td><strong>Memory Space</strong></td>
      <td>Threads share the same memory space.</td>
      <td>Each process has its own memory space.</td>
      <td>All operations run within a single thread's memory space.</td>
    </tr>
    <tr>
      <td><strong>Global Interpreter Lock (GIL)</strong></td>
      <td>Threads are limited by the GIL, which can restrict performance for CPU-bound tasks.</td>
      <td>Processes do not share the GIL, allowing full parallelism for CPU-bound tasks.</td>
      <td>Asyncio operates in a single thread, so GIL is not a limitation for I/O-bound tasks.</td>
    </tr>
    <tr>
      <td><strong>Data Sharing</strong></td>
      <td>Easy to share data between threads, but requires synchronization mechanisms to avoid conflicts.</td>
      <td>More complex data sharing using IPC mechanisms like Pipes and Queues.</td>
      <td>No shared state between tasks; uses non-blocking I/O operations for concurrency.</td>
    </tr>
    <tr>
      <td><strong>Overhead</strong></td>
      <td>Lower overhead compared to processes.</td>
      <td>Higher overhead due to process creation and management.</td>
      <td>Minimal overhead; only involves single-threaded execution.</td>
    </tr>
    <tr>
      <td><strong>Task Scheduling</strong></td>
      <td>Managed by the operating system; threads are scheduled for execution concurrently.</td>
      <td>Managed by the operating system; processes are scheduled for parallel execution.</td>
      <td>Managed by the event loop; coroutines are scheduled and executed asynchronously.</td>
    </tr>
    <tr>
      <td><strong>Example Use Case</strong></td>
      <td>Running multiple I/O operations concurrently, such as downloading files.</td>
      <td>Performing heavy computations in parallel, such as processing large datasets.</td>
      <td>Fetching multiple web pages concurrently without blocking.</td>
    </tr>
  </tbody>
</table>


