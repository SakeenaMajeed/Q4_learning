*FastAPI Project*
FastAPI is a modern, high-performance web framework for building APIs in Python. It is built on top of Starlette and Pydantic and comes with automatic documentation features. FastAPI is designed to be fast, easy to use, and scalable, making it an ideal choice for developing APIs.

--------------------------

Features
Fast: FastAPI is optimized for high performance, leveraging asynchronous support.

Easy to Use: The framework uses simple Python syntax, automatic validation, and documentation generation.

Automatic Documentation: FastAPI automatically generates OpenAPI and JSON Schema documentation.

----------------------------

Prerequisites
Python version 3.7 or above is required.

---------------------------

Installation
Follow these steps to set up your FastAPI project:

Step 1: Check Python Version
Before proceeding, ensure you have Python installed on your system. You can check the version by running:

`python --version`

Step 2: Initialize FastAPI Project
Run the following command to create and initialize your FastAPI project:

`uv init fastdca-p1
cd fastdca-p1
`

On Windows:

`uv venv
.venv\Scripts\activate`

Step 4: Add Dependencies
Now, you need to install the necessary dependencies for your project. To install FastAPI and the Uvicorn ASGI server, use the following command:

`uv add "fastapi[standard]"`

This command installs the core FastAPI framework, the Uvicorn server, and essential packages:

fastapi: The web framework.

uvicorn: The ASGI server to run your FastAPI app.

httpx: An HTTP client for testing FastAPI endpoints.

To add development dependencies for unit testing, run the following command:

`uv add --dev pytest pytest-asyncio`


