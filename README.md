# Python_project_Task1
# 🛒 Q3 - Shopping Cart with Default & Mutable Pitfall (Python Project)

This project demonstrates an important Python concept:  
**mutable default arguments, immutability, and a real-world shopping cart system using functions and data structures.**

---

## 📌 Objective

To understand:
- Why using mutable default arguments like `cart=[]` is dangerous
- How to fix it using `None`
- Difference between mutable and immutable objects
- Building a simple shopping cart system using Python

---

## 🧠 Concepts Covered

- Default function arguments
- Mutable vs Immutable objects
- Lists, Dictionaries, Tuples
- Function design and modular programming
- Looping through data structures
- Exception handling (`TypeError`)
- Basic billing system logic

---

## ⚠️ Part A - Bug (Wrong Approach)

```python
def add_item(item, cart=[]):
    cart.append(item)
    return cart
