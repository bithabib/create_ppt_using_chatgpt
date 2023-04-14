#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
from app import app
from flask import render_template, request, redirect, url_for
from pptx import Presentation
from pptx.util import Inches
import openai
import os
import re
import ast
openai.api_key = "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"
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/create_ppt', methods=['POST'])
def create_ppt():

    def generate_text(prompt):
        messages = [
                {"role": "system", "content" : "You’re a kind helpful assistant"}
            ]
        messages.append({"role": "user", "content": "Please give me two short main point on" + prompt + " to add as slide header. Please return as a python list."})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        return completion.choices[0].message.content
    # Creating powerpoint presentations using the python-pptx package
    # get the text from the form
    text = request.form['topic']
    slide_header = generate_text(text)
    print(slide_header)
    slide_header = re.finditer(r'\[.*?\]', slide_header) 
    print(slide_header)
    exact_string = ""
    for match in slide_header:
        if match:
            print(match.group(0))
            exact_string = match.group(0)
        else:
            print("No match")
    res = ast.literal_eval(exact_string)
    print(type(res))
    print((res))
    X = Presentation()

    Layout = X.slide_layouts[0]
    first_slide = X.slides.add_slide(Layout)

    first_slide.shapes.title.text = text
    first_slide.placeholders[1].text = "Created by Big Data Lab"

    X.save("First_presentation.pptx")

    Second_Layout = X.slide_layouts[5]
    second_slide = X.slides.add_slide(Second_Layout)
    second_slide.shapes.title.text = res[0]

    textbox = second_slide.shapes.add_textbox(Inches(3), Inches(1.5),Inches(3), Inches(1)) 
    textframe = textbox.text_frame
    paragraph = textframe.add_paragraph()
    paragraph.text = "This is a paragraph in the second slide!"
    X.save("First_presentation.pptx")

    Third_Layout = X.slide_layouts[5]
    third_slide = X.slides.add_slide(Third_Layout)
    third_slide.shapes.title.text = res[1]

    textbox = third_slide.shapes.add_textbox(Inches(3), Inches(1.5),Inches(3), Inches(1))
    textframe = textbox.text_frame
    paragraph = textframe.add_paragraph()
    paragraph.text = "This is a paragraph in the third slide!"
    X.save("First_presentation.pptx")


    return redirect(url_for('index'))