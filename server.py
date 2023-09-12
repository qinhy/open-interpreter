
from interpreter import MessageBlock,CodeBlock,CodeInterpreter
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PythonCodeRequest(BaseModel):
    content: str

@app.post("/run_python_code_block/")
def run_code_block(request: PythonCodeRequest):
    if '```' in request.content and '```python' not in request.content:
        raise HTTPException(status_code=400, detail="Language not supported")
    
    if '```python' in request.content:
        active_block = MessageBlock()
        active_block.update_from_message(request.content)
        # {
        # "content" : """
        # Here, we're simply using a Python code to print "Hello, World!".
        # ```python
        # x = 10
        # y = 20
        # sum = x + y
        # sum
        # ```
        # """}

    else:
        # Create a CodeBlock instance        
        """
        def factorial(n):
            if n == 1:
                return 1
            else:
                return n * factorial(n-1)

        result = factorial(5)
        print("Factorial of 5 is:", result)
        """
        active_block = CodeBlock()
        # Emulate a message to set up the code block with the provided code
        message = {
            "function_call": {
                "parsed_arguments": {
                    "language": 'python',
                    "code": request.content

                }
            }
        }
        active_block.update_from_message(message)

    # Ensure the language provided is supported
    # if request.language != 'python':
    #     raise HTTPException(status_code=400, detail="Language not supported")

    # Create a CodeInterpreter instance for the provided language
    debug_mode = False  # Debug mode is turned off for the API
    interpreter = CodeInterpreter(language='python', debug_mode=debug_mode)
    interpreter.active_block = active_block
    # Execute the code
    output = interpreter.run()
    # Return the output
    return {"output": output}
