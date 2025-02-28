# main.py
import module_a as a
import module_b as b

# Original outputs
print(a.compute())  # Output: Result from module A with Data from module A
print(b.compute())  # Output: Result from module B with Data from module B

# Reassign module_a's variable x
a.x = "CHANGES FROM MAIN.PY FILE"

# After updating a.x, compute() uses the new value
print(a.compute())  # Output: Result from module A with 10
