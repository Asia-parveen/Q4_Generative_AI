# 📌 Dependency Injection in FastAPI

**🔍 What is Dependency Injection?**

Dependency Injection (DI) is a design pattern that allows one part of the application to depend on external components (dependencies) in a clean and maintainable way.
In FastAPI, DI helps in keeping routes clean, managing reusability, and enhancing testability by using the Depends() function.

## 🧩 Why Use Dependency Injection?

**➕ Code Reusability:** Common logic can be reused across routes.

**🧼 Cleaner Code:** Keeps route functions minimal and readable.

**🧪 Easy Testing:** Dependencies can be easily mocked or overridden.

**⚙️ Centralized Logic:** Core operations like authentication, data validation, and fetching resources can be abstracted.

# ✅ Types of Dependency Injection in FastAPI

**1. Simple Function Dependency**

Used for injecting static or reusable data.

Automatically passed into route handler using Depends().

**2. Function with Parameters**
Dependencies can accept parameters like Query, Path, Body, etc.

Useful for extracting and validating user input.

**3. Login or Authentication Dependency**

Handles logic like verifying username/password.

Keeps authentication separate from business logic.

**4. Multiple Dependencies**

More than one dependency can be injected into a single route.

FastAPI resolves them in order and passes the results.

**5. Class-Based Dependencies**

Encapsulates logic inside a class.

Can be reused and initialized with parameters (like a mini service).

__call__ method is used to make the class callable as a dependency.

# 🛠 How FastAPI Handles Dependencies

FastAPI uses Python’s type hints and Depends() internally to analyze and inject dependencies.

Dependencies can return anything: dicts, objects, primitives, etc.

If an exception is raised inside a dependency, FastAPI automatically handles the error response.

# 📄 Real-World Use Cases

**🔐 Authentication & Authorization**

**📥 Input validation & Preprocessing**

**🧾 Database session management**

**🚧 Error handling & access control**

**🧱 Resource loading (like blog or user from DB)**

# 🧠 FastAPI’s dependency injection Summary
FastAPI’s dependency injection system is simple yet powerful. By separating reusable logic into dependencies, it ensures cleaner, modular, and testable code architecture — essential for building modern, scalable APIs.
