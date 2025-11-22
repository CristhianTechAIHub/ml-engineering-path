# Machine Learning Engineering Path 🚀

![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/license-MIT-green?style=flat)
![Status](https://img.shields.io/badge/status-active_learning-orange?style=flat)

> **"What I cannot create, I do not understand."** — Richard Feynman

## 📖 About This Repository

This repository documents my comprehensive journey from Mechatronics Engineering to **Senior Machine Learning Engineering**. 

Unlike typical tutorial repositories, this project focuses on **First Principles**:
1.  **Mathematical Rigor:** Deriving algorithms from scratch (Linear Algebra, Calculus, Statistics) before using libraries.
2.  **Production Standards:** Writing clean, modular, and documented code consistent with Big Tech standards.
3.  **Modern Implementation:** Mastering the current state-of-the-art stack (Scikit-Learn, PyTorch, Transformers, LLMs).

It serves as a companion to Aurélien Géron's *"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow"* (3rd Edition), enriched with deep-dives into the underlying mathematics and system design.

---

## 📂 Repository Structure

The project is organized to simulate a production environment while maintaining educational clarity:

```text
ml-engineering-path/
├── 00-math-foundations/       # 🧮 The Engine: Linear Algebra & Calculus from scratch.
│   ├── vectorization_simd.ipynb    # Benchmarking NumPy vs Python Loops (SIMD)
│   └── ...
│
├── 01-handson-ml-book/        # 📘 The Guide: Applied ML using Scikit-Learn/TensorFlow.
│   ├── cap02-housing/              # End-to-end ML project (Data Cleaning -> Evaluation)
│   └── ...
│
├── 02-algorithms-scratch/     # ⚙️ The Core: Manual implementation of ML algorithms.
│   ├── linear_regression.py        # Custom class implementing Gradient Descent
│   └── ...
│
└── src/                       # 📦 Utilities: Reusable production-grade modules.
