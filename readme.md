# 🧠 Pydantic Models – Beginner to Advanced Concepts

This repository contains structured examples demonstrating **Pydantic (Python Data Validation Library)** concepts from basic models to advanced validation and serialization techniques.

The project is designed for learning and understanding:

- Data validation
- Nested models
- Field constraints
- Computed fields
- Custom validators
- Self-referencing models
- Serialization techniques

---

## 📂 Project Structure

```
01-first_model.py              → Basic Pydantic model
02-product_model.py            → Product model with types
03-field_example.py            → Field constraints and metadata
04-employee_model.py           → Employee structured model
05-fieldValidation.py          → Field-level validation
06-ComputedField.py            → Computed properties
07-AdvanceValidators.py        → Advanced custom validators
08-Nested_model.py             → Nested model example
09-Self-reference.py           → Self-referencing models
10-AdvanceNestedModel.py       → Complex nested models
11-PydanticSerialization.py    → Model serialization (JSON, dict)
```

---

# 📘 Concepts Covered

## 1️⃣ Basic Model
- Creating simple Pydantic models
- Type enforcement
- Automatic validation

## 2️⃣ Field Customization
- Using `Field()`
- Default values
- Constraints (min_length, max_length, gt, lt)

## 3️⃣ Field Validation
- Custom field validators
- Input sanitization
- Raising validation errors

## 4️⃣ Computed Fields
- Creating derived properties
- Business logic inside models

## 5️⃣ Advanced Validators
- Model-level validation
- Cross-field validation
- Complex input handling

## 6️⃣ Nested Models
- Embedding models inside other models
- Structured API request/response modeling

## 7️⃣ Self Referencing Models
- Recursive structures
- Tree-like data handling

## 8️⃣ Serialization
- Convert model to dictionary
- Convert model to JSON
- Custom serialization logic

---

# 🚀 How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/pydantic-models.git
cd pydantic-models
```

### 2️⃣ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install pydantic
```

### 4️⃣ Run any file

```bash
python 01-first_model.py
```

---

# 🎯 Why This Project is Useful

✔ Helps understand backend data validation  
✔ Useful for FastAPI development  
✔ Important for API request/response modeling  
✔ Common interview topic  
✔ Required for production-grade backend systems  

---

# 🛠 Technologies Used

- Python 3.9+
- Pydantic

---

# 📌 Learning Outcome

After completing this project, you should be able to:

- Design structured data models
- Validate API inputs safely
- Handle nested and recursive data
- Serialize and transform data cleanly
- Prevent invalid data in backend systems

---

⭐ If you found this helpful, feel free to star the repository!
