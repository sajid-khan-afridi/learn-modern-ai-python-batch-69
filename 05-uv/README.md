# **UV Documentation and Explanation**

## 1. Checking UV Commands and Version

1. **uv help**

   - Shows a list of all available commands and options in UV.
   - Useful if you’re unsure about a specific command or want to see a quick reference.

2. **uv version**
   - Displays the installed version of UV, so you know if you have the latest release.

---

## 2. Initializing a Basic Project

### **Command:**

```bash
uv init project1
```

- Creates a new project directory called **project1** with essential files, but **does not** create a `src/` folder by default.
- Typical **UV** initialization places project settings (like the `.toml` file) inside **project1**, but keeps the project structure minimal.

> **Why No `src/` Folder?**  
> Many modern Python packaging standards (like [PyPA recommendations](https://packaging.python.org/en/latest/tutorials/packaging-projects/)) prefer a `src/` folder. However, with UV’s default `init`, you can still have a functional project without it. It’s purely a layout choice.

---

## 3. Running a Python Script

### **Command:**

```bash
uv run hellp.py
```

- Executes the Python script named `hellp.py` (typo or example naming).
- **UV** automatically sets up and activates the virtual environment in the background.
- No extra `source venv/bin/activate` step is required.

> **Auto Virtual Environment Activation**  
> When you run `uv run <script.py>`, UV **launches** your script **inside** the environment. Some UI-based editors or terminals may also show a button or prompt to activate the environment manually.

---

## 4. Viewing or Managing Virtual Environments

### **Command:**

```bash
uv env
```

- Shows information about the current UV environment. This might include:
  - The path to the environment.
  - Installed packages.
  - Active Python version.

> **.python-version & TOML**
>
> - UV can use a `.python-version` file and/or your `pyproject.toml` to **pin** a specific Python version.
> - Changing `.python-version` can tell UV which exact Python interpreter to use if you have multiple versions installed.

---

## 5. Creating a Project with a `src/` Folder

### **Command:**

```bash
uv init --package project2
```

- Initializes a **packaged** project called **project2** **with** a `src/` folder structure.
- Inside `project2`, you’ll likely see:
  ```
  project2/
    └─ src/
        └─ project2/  (contains __init__.py)
  ```
- This layout follows common Python packaging practices, placing your code in `src/project2`.

> **Why `--package`?**
>
> - The `--package` option tells UV to create a **package-ready** structure, which is recommended if you plan to distribute or publish your code.
> - It automatically includes an `__init__.py` file in your `src/project2/` folder, making it a **Python package**.

---

## 6. Understanding the `.toml` File

When you run `uv init` (with or without `--package`), UV generates a **TOML** configuration file (often named `pyproject.toml` or something similar). This file includes various sections, for example:

```toml
[project]
name = "project2"
version = "0.1.0"
description = "Your Project Description"

[project.scripts]
piaic = "project2:main"

[tool.uv]
python-version = "3.11"
```

### **Typical Sections**

1. **[project]**

   - Defines the **metadata** for your project (name, version, description).

2. **[project.scripts]**

   - Maps a command (like `piaic`) to a Python function (`"project2:main"`).
   - Allows you to run `uv run piaic` to execute the `main()` function in `project2/__init__.py` or `project2/main.py`.

3. **[tool.uv]** (or similar section)
   - UV-specific configurations, like which Python interpreter version to use.

---

## 7. Using Named Scripts in the TOML

### **Example**

In the `[project.scripts]` section:

```toml
[project.scripts]
piaic = "project2:main"
```

- **piaic** = the **command name** you want to run.
- **"project2:main"** = the **path** to the function you want to execute (`main` in `project2/__init__.py` or in `project2/main.py`).

### **Running the Script**

```bash
uv run piaic
```

- This tells UV, “Run the script named **piaic**, which in turn calls `project2.main()`.”
- Great for **shortcut commands** or CLI tools in your project.

---

## 8. Putting It All Together

1. **Check UV is installed:**
   ```bash
   uv help
   uv version
   ```
2. **Initialize a project without a `src/` folder:**
   ```bash
   uv init project1
   cd project1
   ```
   - You’ll see a basic structure and a `.toml` or `pyproject.toml` file.
3. **Add or modify Python version:**
   - Edit `.python-version` or the `[tool.uv]` section in your TOML file.
4. **Run a Python file:**
   ```bash
   uv run hellp.py
   ```
   - UV sets up a virtual environment automatically.
5. **Create a more standard Python package:**
   ```bash
   uv init --package project2
   ```
   - This includes a `src/` folder with your package structure and an `__init__.py`.
6. **Define scripts in the TOML:**
   - Under `[project.scripts]`, add your command name and the function to call.
7. **Use `uv run <script_name>`** to execute it.

---

# **Conclusion**

With these notes and commands, you can:

- Quickly **initialize** new Python projects using **UV**.
- Decide whether you want a **simple layout** (no `src/` folder) or a **packaged layout** (with `src/`).
- **Manage** and **switch** Python versions effortlessly via `.python-version` or your `.toml` file.
- **Run scripts** either by direct file name or by registering them under `[project.scripts]`.

UV automatically handles **virtual environments**, saving you time and making your workflow simpler. By understanding the structure and the TOML configuration, you can easily tailor each project to your needs—whether it’s a lightweight script or a full-fledged Python package ready for publication.

---

**Happy Coding with UV!** If you need more help, run:

```bash
uv help
```
