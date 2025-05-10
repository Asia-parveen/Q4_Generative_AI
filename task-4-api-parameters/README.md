# 📘 FastAPI Parameters:

## FastAPI provides several powerful ways to handle user input in APIs. These are mainly categorized into four types:

# 🔹 1. Path Parameters:

**Definition:** Parameters that are part of the URL path.

**Syntax Example:** /items/{item_id}

**Use Case:** Useful when accessing a specific item by ID or name.

## Characteristics:

*Required by default.*

*Can include validation like min/max values, regex, etc.*

*Type-checked and auto-converted.*

## 🔹 2. Query Parameters

**Definition:** Parameters passed in the URL after the ?.

**Syntax Example:** /items?skip=10&limit=5

**Use Case**: Common for filtering, sorting, pagination, etc.

## Characteristics:

*Optional or required (depending on how you define them).*

*Default values can be assigned.*

*Multiple values for the same key supported.*

# 🔹 3. Request Body:

**Definition:** Data sent in the body of the request, typically as JSON.

**Use Case:** Used for sending complex objects like user details, products, etc.

**Characteristics:**

Defined using Pydantic models for data validation and type checking.

Ideal for POST, PUT, or PATCH methods.

# 🔹 4. Header Parameters

**Definition:** Values sent in the HTTP headers of a request.

**Use Case:** Used for metadata like authentication tokens, user-agent, language, etc.

**Characteristics:**

Can be optional or required.

Often used for secure or contextual information.

FastAPI automatically maps common headers like User-Agent.

# 🔸 Combination Usage:

we can combine any of these parameters in a single route handler:

Path + Query: Useful when targeting a specific resource and applying filters.

Query + Body: Helpful when sending filters along with complex body data.

Path + Header: Good for APIs needing secure contextual data for a specific reso
