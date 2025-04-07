import os
from langchain.prompts import PromptTemplate
from langchain_together import Together  # Corrected import

# Set your correct Together AI API key
os.environ["TOGETHER_API_KEY"] = "43dee022a48d22c9b1652790927c306e26009b9e59b96fd8d977cbf88d241152"  # Replace with your actual API key

# Define a prompt template
template = PromptTemplate(
    input_variables=["name", "product"],
    template="Write a friendly email to {name} introducing our new product, {product}, and its benefits."
)

# Format the template with actual values
formatted_prompt = template.format(name="John", product="AI Chatbot")

# Use a supported Together AI model
llm = Together(model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free", temperature=0.7, max_tokens=200)

# Generate response
try:
    response = llm.invoke(formatted_prompt)
    print("\nGenerated Email:\n", response)
except Exception as e:
    print("\nError generating response:", e)
    