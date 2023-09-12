from interpreter import *

# # Step 1: Set up a Python code snippet
# python_code = """
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# result = factorial(5)
# print("Factorial of 5 is:", result)
# """

# # Step 2: Create a CodeBlock instance
# code_block = CodeBlock()
# code_block.update_from_message({
#     "function_call": {
#         "parsed_arguments": {
#             "language": "python",
#             "code": python_code
#         }
#     }
# })

# # Step 3: Create a CodeInterpreter instance for Python
# debug_mode = True  # Let's enable debug mode for demonstration
# interpreter = CodeInterpreter(language="python", debug_mode=debug_mode)
# interpreter.active_block = code_block
# # Step 4: Execute the code
# res = interpreter.run()


# 1. Create a message block for displaying content
message_block = MessageBlock()
message_block.update_from_message({
"content" : """
Here, we're simply using a Python code to print "Hello, World!".
```python
x = 10
y = 20
sum = x + y
sum
```
"""})

res = message_block.code


# 2. Initialize the CodeInterpreter for Python
interpreter = CodeInterpreter(language="python", debug_mode=True)

# 3. Assign a Python code snippet to the active block of the interpreter
interpreter.active_block = message_block

# 3. Execute the code.
res = interpreter.run()


with open('res.txt','w') as f:
    f.write(res)