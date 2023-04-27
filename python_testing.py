import re

text = """Slide Header 1: ChatGPT Introduction 
1. ChatGPT stands for "Chat Generated Passages Transformer" 
2. It is a state-of-the-art language model designed for generating human-like responses in chatbots 
3. Its AI technology understands context, syntax and semantics for more natural, intelligent and engaging conversations 

Slide Header 2: ChatGPT Applications 
1. ChatGPT can be integrated into different applications such as customer service chatbots, virtual assistants, and chat-based games 
2. It can help businesses cut costs by reducing the need for human operators and improving customer service satisfaction 
3. In healthcare, ChatGPT can be used to simulate conversations and help patients with mental and behavioral issues 

Slide Header 3: ChatGPT Language Support 
1. ChatGPT supports multiple languages such as English, Spanish, Portuguese, Chinese, Japanese, and more 
2. This allows businesses to expand their customer service reach globally 
3. It also provides more opportunities for cross-cultural communication and language learning 

Slide Header 4: ChatGPT Technical Features 
1. ChatGPT uses a transformer architecture that allows it to learn intricate details of language context and syntax 
2. It was trained on a massive amount of text data to ensure accurate and diverse responses 
3. The model can generate long-form passages and responses with consistent and understandable language use 

Slide Header 5: ChatGPT Future Development 
1. ChatGPT is continuously being improved with frequent software updates to enhance its accuracy and efficiency 
2. Developers can access the ChatGPT source code to add custom features or modifications 
3. ChatGPT's potential is vast and the future looks promising for advancing the field of conversational AI."""

# Define the regex pattern to extract the slide headers
# pattern = r'Slide Header (\d+): (.+)\n'
pattern = r'Slide Header (\d+): (.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n'


# Compile the regex pattern
regex = re.compile(pattern)

# Extract the slide headers and their corresponding content
headers_and_content = regex.findall(text)
print(headers_and_content)

headers_and_content_dict = {}
for header_and_content in headers_and_content:
    headers_and_content_dict[header_and_content[1]] = header_and_content[2:]

print(headers_and_content_dict)


text = "Slide 5 header: The Future of Healthcare with ChatGPT"
# h of Headercan be small letter or capital letter
pattern = r'Slide (\d+) header: (.+)'

# pattern = r'Slide (\d+) header: (.+)'