import re

text = """
1) Slide Header 1: 
1. ChatGPT is a modern software communication tool designed for seamless conversation between individuals or teams.
2. It offers easy-to-use features for instant messaging, file sharing, video conferencing, and more.
3. With ChatGPT, users can stay connected and collaborate efficiently without any geographical limitations.

2) Slide Header 2:
1. ChatGPT comes with a user-friendly interface, making it easy for anyone to install and use.
2. It offers customization options with themes, emojis, and other in-app add-ons.
3. The software ensures security and privacy, with end-to-end encryption and other safety features.

3) Slide Header 3:
1. ChatGPT is an affordable communication tool, designed for businesses of any size.
2. The software offers flexible pricing options, making it accessible to all users.
3. With ChatGPT, organizations can streamline their communication, leading to increased productivity and efficiency.

4) Slide Header 4:
1. ChatGPT offers a wide range of integrations with other productivity tools, including project management apps, calendar tools, and more.
2. This integration enhances the overall communication experience, ensuring quick and easy collaboration.
3. Users can access ChatGPT on any device, making it easy to stay connected on the go.

5) Slide Header 5:
1. ChatGPT allows teams to work together in real-time, providing a platform for seamless collaboration.
2. The software provides features that allow users to share screens, whiteboarding, and co-creation of documents.
3. These features ensure the effective flow of communication, which leads to better, faster decision making."""

pattern = r"\d+\)\s"

text = re.sub(pattern, "", text)
print(text)

# Define the regex pattern to extract the slide headers
# pattern = r' Slide Header (\d+): (.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n'
# pattern = r'Slide Header (\d+): (.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n'
pattern = r'Slide Header (\d+): \n\d+\.\s(.+)\n\d+\.\s(.+)\n\d+\.\s(.+)\n'


# Compile the regex pattern
regex = re.compile(pattern)

# Extract the slide headers and their corresponding content
headers_and_content = regex.findall(text)
print(headers_and_content)

headers_and_content_dict = {}
for header_and_content in headers_and_content:
    headers_and_content_dict[header_and_content[1]] = header_and_content[2:]

print(headers_and_content_dict)

import re

text = "1) First line\n2) Second line\n\n3) Third line\n4) Fourth line"

# Clean 1) and 2) from the text
pattern = r"\d+\)\s"

clean_text = re.sub(pattern, "", text)

print(clean_text)