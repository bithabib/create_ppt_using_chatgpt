# Flask app for generating PowerPoint presentations using ChatGPT
This Flask app uses the ChatGPT language model to generate a PowerPoint presentation on a given topic. The app takes a topic as input from the user and generates a PowerPoint presentation with relevant images and text.

# Prerequisites
Before running the app, you will need to:

 - Sign up for an OpenAI API key here.
 - Install the required Python packages by running pip install -r requirements.txt.
 - Place your OpenAI API key in a file named .env in the root directory of the app. The file should contain the following line: OPENAI_API_KEY=<your_api_key_here>. Replace <your_api_key_here> with your actual API key.
# Usage
To start the app, run python app.py. The app will start running on http://localhost:5000/.

To generate a PowerPoint presentation:

 - Enter a topic in the input field on the home page and click on the "Generate PPT" button.
 - Wait for the app to generate the PowerPoint presentation. This may take a few minutes depending on the length and complexity of the topic.
 - Once the presentation is generated, you will be redirected to a page where you can download the presentation as a PowerPoint file.
# Technical details
The app is built using Flask, a Python web framework, and the python-pptx library, which allows us to generate PowerPoint presentations programmatically.

The app uses the openai Python package to interact with the ChatGPT language model. The openai package requires an OpenAI API key, which is stored as an environment variable.

The app generates the PowerPoint presentation in three steps:

 - Retrieve information on the given topic using the ChatGPT language model.
 - Retrieve relevant images using the Google Custom Search API.
 - Generate the PowerPoint presentation using the python-pptx library, and save it to disk.
# Credits
This app was developed by [Habibur Rahman] as a project for [Big Data Lab]. The app uses the ChatGPT language model developed by OpenAI and the Google Custom Search API.