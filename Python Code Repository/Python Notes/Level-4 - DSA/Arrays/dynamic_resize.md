# Design Dynamic Array (Resizable Array)

Note: The following rewritten summary clarifies the requirements and design. A full reference implementation and examples can be added below.

## Clean Summary

- Goal: Implement a resizable array (dynamic array) that separates logical size from physical capacity.
- Trigger resize when pushing into a full array; typically double capacity.
- Provide methods: constructor (with positive capacity), `get`, `set`, `pushback`, `popback`, `resize`, `getSize`, `getCapacity`.
- Complexity: `get/set` O(1), `pushback` amortized O(1), `popback` O(1), `resize` O(n).

## Problem Statement

Design a **Dynamic Array** (also called a resizable array), similar to:

- `ArrayList` in Java
- `vector` in C++

The goal is to **simulate how dynamic arrays work under the hood**, rather than relying on Python’s built-in list resizing.

---

## Requirements

Implement a `DynamicArray` class with the following methods:

### Constructor

```text
DynamicArray(int capacity)

Initializes an empty array with the given initial capacity.

capacity > 0

Methods
- get(i): Return element at index i
- set(i, n): Set value n at index i
- pushback(n): Append element n to the end
- popback(): Remove and return the last element
- resize(): Double the capacity of the array
- getSize(): Return number of elements
- getCapacity(): Return current capacity
Constraints & Guarantees

Index i in get(i) and set(i, n) is always valid.

popback() is called only when the array is non-empty.

If pushback() is called when the array is full, resize() must be triggered first.

Key Design Goals

Separate logical size and physical capacity

pushback() should be amortized O(1)

resize() should:

Allocate a new array of size 2 × capacity

Copy existing elements

Replace the old array

Example
Input
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

Output
[null, null, 1, null, 2]
