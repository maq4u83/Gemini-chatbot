import google.generativeai as genai
API_KEY = "AIzaSyAMY_GFX0QTPNVVppD__rYu1B4j2cx69aY"
genai.configure(api_key=API_KEY)

# Initialize the model

model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

user_input = input("Enter your prompt = ")
output = getResponseFromModel(user_input)
print(output)