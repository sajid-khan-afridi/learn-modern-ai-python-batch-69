# module_b.py
# Global variable in module_b
x = "Data from module B"

def compute():
    # Uses the global variable x from module_b's namespace
    return "Result from module B with " + str(x)
