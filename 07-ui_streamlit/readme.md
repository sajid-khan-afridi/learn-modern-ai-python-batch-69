# Building and Running a Basic Streamlit App with uv

This guide explains how to install Streamlit via the uv package manager, run your Streamlit app, and take advantage of its built-in features. It also outlines some best practices and essential commands for development.

---

## 1. Overview

**Streamlit** is a Python library that makes it simple to build interactive web applications and prototypes. It abstracts away the need to write HTML, CSS, or JavaScript for most UI needs by handling the frontend automatically. You can use Streamlit to create dashboards, data visualizations, and quick prototypes.

**uv Package Manager** (an alternative to pip) is used here to manage packages and execute commands. In our examples, we’ll show two ways to run your Streamlit app using uv.

---

## 2. Installation

Before running your app, you need to install Streamlit. Use the following command to install Streamlit via uv:

### Installing uv project

```bash
uv init --package project
```
### Run the project

```bash
uv run project
```

### Essential command: Installs the Streamlit package using uv
```bash
uv pip install streamlit
```

> **Best Practice:** Always ensure your environment is isolated (e.g., using virtual environments) to avoid dependency conflicts.

---

## 3. Running the Streamlit App

Once installed, you have multiple options to run your app. Here are two common methods:

### Option 1: Direct Streamlit Command

If you are comfortable using Streamlit's command directly:

```bash
# Runs the basic Streamlit app located in src/pr1/basic.py
streamlit run src/pr1/basic.py
```

### Option 2: Using uv Run

Alternatively, you can use uv to execute the Streamlit run command:

```bash
# Executes the Streamlit app located in src/pr3/simple_app.py via uv run
uv run streamlit run src/pr3/simple_app.py
```

> **Note:** Choose the option that best integrates with your workflow. Both commands ultimately launch your Streamlit app in your browser.

---

## 4. Essential Streamlit Commands

Here are some useful commands and features provided by Streamlit:

- **Launching the Demo App:**
  ```bash
  # Displays the Streamlit demo showcasing multipage support, various inputs, and more.
  streamlit hello
  ```

- **Magic Commands & Auto-detection:**
  - Streamlit automatically recognizes and renders objects (like charts or data frames) without extra code.
  - It handles backend processes (CSS, queries, JavaScript) so you can focus on Python code.

- **Data Visualization:**
  - Although Streamlit supports interactive widgets, when using libraries like Matplotlib, the plots are rendered as static images.
  - Consider using libraries like Altair or Plotly if you require interactivity.

> **Tip:** Refer to the [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet) for a quick reference of commands and best practices.

---

## 5. Additional Best Practices

- **Project Structure:**
  - Organize your code by separating components (e.g., `src/pr1` for one version and `src/pr3` for another).
  - Maintain a consistent directory structure for easier maintenance and scaling.

- **Documentation & Comments:**
  - Document your code extensively to help future you (and teammates) understand the purpose of each command and module.
  - Use inline comments to explain non-obvious parts of your code.

- **Prototyping vs. Production:**
  - Use Streamlit for rapid prototyping to demonstrate concepts to customers.
  - For professional builds, consider frameworks like Next.js to transition into a more robust JAMstack approach after approval.

---

## 6. Summary

1. **Install Streamlit:**  
   Use `uv pip install streamlit` to install the package.

2. **Run the App:**  
   Launch your app using either:
   - `streamlit run src/pr1/basic.py` (directly via Streamlit), or
   - `uv run streamlit run src/pr3/simple_app.py` (using uv).

3. **Explore Built-in Features:**  
   Use `streamlit hello` to see a demo of Streamlit's capabilities, including multipage support and various input widgets.

4. **Best Practices:**  
   - Keep your project organized.
   - Use virtual environments.
   - Document your code for clarity.
   - Prototype quickly, then scale using more robust frameworks as needed.

Following these steps and best practices will help you build, document, and deploy a basic yet powerful Streamlit application. Enjoy building your next interactive app!