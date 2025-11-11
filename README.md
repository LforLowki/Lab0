# Lab0 - Data Preprocessing CLI

This project implements a set of data preprocessing functionalities for numerical, textual, and structural data, accessible via a command-line interface (CLI). It was developed as part of the MLOps course.

---

## Features

The project provides the following preprocessing functionalities:

### **Cleaning**
- **Remove missing values** (`None`, empty strings, `NaN`)  
- **Fill missing values** with a default or user-specified value  
- **Remove duplicate values** from a list  

### **Numerical Processing**
- **Normalization** (Min-Max scaling)  
- **Standardization** (Z-score)  
- **Clipping** numerical values to a range  
- **Conversion to integers** (non-numeric values are ignored)  
- **Logarithmic transformation** (applied to positive values)  

### **Text Processing**
- **Tokenization** into lowercase alphanumeric words  
- **Remove punctuation** (keeping only letters, digits, and spaces)  
- **Remove stopwords** from text  

### **Structural Operations**
- **Flatten** a list of lists  
- **Shuffle** a list with optional seed for reproducibility  

---

## Installation

1. Clone the repository:

```bash
git clone 
cd Lab0
