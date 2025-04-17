# langchain_env\Scripts\activate
from flask import Flask, render_template, request, jsonify
import os
from langchain_together import Together
from dotenv import load_dotenv  # Add this import

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get API key from environment variables
together_api_key = os.getenv("TOGETHER_API_KEY")
if not together_api_key:
    raise ValueError("TOGETHER_API_KEY not found in environment variables")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_email():
    data = request.get_json()
    user_input = data.get("purpose", "").strip()

    if not user_input:
        return jsonify({"error": "Please enter the purpose of the email."}), 400

    prompt = f"""
    Generate two different professional emails for the request:  
    "{user_input}"  

    **Format:**  
    - Start each response with "### Response 1:" and "### Response 2:"
    - Each email should have a subject line, greeting, body, and closing.

    Example format:
    ### Response 1:
    [First email here]
    ### Response 2:
    [Second email here]
    """

    try:
        llm = Together(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            temperature=0.7,
            max_tokens=1000,
            together_api_key=together_api_key  # Pass the API key here
        )
        response = llm.invoke(prompt)

        # Split response using "### Response 2:" as delimiter
        parts = response.split("### Response 2:")
        email_1 = parts[0].replace("### Response 1:", "").strip() if len(parts) > 0 else "Error generating response 1"
        email_2 = parts[1].strip() if len(parts) > 1 else "Error generating response 2"

        return jsonify({"email1": email_1, "email2": email_2})

    except Exception as e:
        return jsonify({"error": f"Failed to generate email. {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)