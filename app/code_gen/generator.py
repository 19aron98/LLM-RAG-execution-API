# Code generation logic

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Load the model
model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    model="qwen/qwen-2.5-coder-32b-instruct:free"
)

# Generate code function
def generate_code(output):
    """Generate Python script for the retrieved function"""
    
    template = """ Generate a structured Python script with the following constraints:
    Function Details:
    - Module Name: {Module}
    - Function Name: {Function Name}
    
    ### **Code Requirements**
    1. Import the function from the specified module {Module}.
    2. Use a `main()` function to execute the function.
    3. Implement error handling with `try-except`.
    4. Print a success message if execution is successful.
    5. Ensure the script is executable as a standalone module.
    6. No additional text, explanations, or markdown formatting (dont use --> ```python `, etc.).
    
    Now, generate only the clean Python script:
    """
    
    template = PromptTemplate(template = template, input_variables = ['Module', 'Function Name'])

    prompt = template.invoke({
    "Module" : output.get('Module')[0],
    'Function Name' : output.get('Function Name')[0]
    })
    
    return output.get('Function Name')[0], model.invoke(prompt)