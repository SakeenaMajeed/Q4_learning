# 🧠 Agent & Runner Architecture - Python AI System

This README explains the core logic and structure behind the `Agent` and `Runner` classes, and the use of generics in Python for handling flexible types such as `TContext`.

---

## 1. Why is the Agent class defined as a `@dataclass`?

The `Agent` class is defined using Python’s `@dataclass` decorator to simplify class creation. With `@dataclass`, boilerplate code such as `__init__`, `__repr__`, and `__eq__` is automatically generated.

### ✅ Benefits:
- Auto-generates constructors and common methods
- Reduces repetitive code
- Improves readability and structure

---

## 2a. Why does the Agent class contain the system prompt as instructions? Why is the Agent callable?

The **system prompt** defines the Agent's personality or role. Making the `Agent` callable allows cleaner and more natural syntax.

### ✅ Benefits:
- Keeps system instructions stored inside the Agent
- Allows direct interaction like: `agent("What's the weather today?")`

---

## 2b. Why is the user prompt passed to `run()` in Runner? Why is it a `@classmethod`?

The user prompt is passed to `run()` because it's different every time. Using `@classmethod` allows calling `run()` without creating a `Runner` object.

### ✅ Benefits:
- Simpler interface: `Runner.run("Hi there")`
- Centralized AI execution logic
- Reduces object creation overhead

---

## 3. What is the purpose of the Runner class?

The `Runner` class acts as a **controller** between the user and the Agent. It initializes the Agent, passes input, and returns the result.

### ✅ Responsibilities:
- Accepts user input
- Initializes Agent
- Handles flow between input and AI output

---

## 4. What are Generics in Python? Why use it for `TContext`?

Generics are a way to make classes and functions flexible with different types. `TContext` is a generic type variable for representing different forms of context in an Agent.

### ✅ Benefits:
- Type-safe and reusable
- Adapts to any kind of context (string, dict, object)
- Promotes scalable and flexible agent design

---

## 📌 Summary Table

| Concept           | Explanation                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `@dataclass`      | Reduces boilerplate, auto-generates init and helpers                        |
| `system prompt`   | Defines Agent behavior or personality                                       |
| `__call__`        | Makes Agent instances callable with user input                              |
| `Runner.run()`    | Class method that triggers Agent logic without object creation              |
| `user prompt`     | Passed at runtime since it changes every time                               |
| `Runner` class    | Connects user input with Agent logic; simplifies user interaction           |
| `Generic[TContext]`| Allows Agent to work with any context type (flexible and reusable)         |

---

## 💡 Final Note

This structure enables scalable and modular AI system design. It ensures reusability, separation of concerns, and clean interaction patterns between the Agent and user input — perfect for production-ready AI assistants or chatbots.

