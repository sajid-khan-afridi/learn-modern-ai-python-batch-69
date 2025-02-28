# module_a.py
# Global variable in module_a
x = "Data from module A"

def compute():
    # Uses the global variable x from module_a's namespace
    return "Result from module A with " + str(x)
