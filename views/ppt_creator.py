from app import app
from flask import render_template, request, redirect, url_for
from pptx import Presentation
from pptx.util import Inches
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('API_KEY')
@app.route('/')
def index():

    return render_template('index.html')

@app.route('/create_ppt', methods=['POST'])
def create_ppt():

    def generate_content(prompt):
        messages = [
                {"role": "system", "content" : "You’re a kind helpful assistant"}
            ]
        messages.append({"role": "user", "content": prompt})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        return completion.choices[0].message.content

    def generate_header(prompt, number_of_slides):
        messages = [
                {"role": "system", "content" : "You’re a kind helpful assistant"}
            ]
        messages.append({"role": "user", "content": "Please give me " + number_of_slides + " short main point on" + prompt + " to add as slide header. Please return as a python list."})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        return completion.choices[0].message.content
    
    def generate_ppt(prompt):
        messages = [
                {"role": "system", "content" : "You’re a kind helpful assistant"}
            ]
        messages.append({"role": "user", "content": "Write a ppt on " + prompt + " in given format Slide Number, Header and Content"})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
            )
        return completion.choices[0].message.content
    
    topic = request.form['topic']
    generated_ppt = generate_ppt(topic)
    # print(generated_ppt)
    split_backslash_n = generated_ppt.split("\n")
    # print(split_backslash_n)
    if "Header: " in generated_ppt:
        i = 0
        header_content = []
        header_content_dict = {}
        while i< len(split_backslash_n):
            
            if 'Header:' in split_backslash_n[i]:
                if header_content_dict:
                    header_content.append(header_content_dict)
                    header_content_dict = {}
                    header_content_dict['header'] = split_backslash_n[i].replace("Header: ","")
                    i = i+1
                else:
                    header_content_dict['header'] = split_backslash_n[i].replace("Header: ","")
                    i = i+1
            else:
                if 'Content:' in split_backslash_n[i]:
                    if 'content' in header_content_dict:
                        header_content_dict['content'] = header_content_dict['content'] + split_backslash_n[i].replace("Content:","")
                    else:
                        header_content_dict['content'] = split_backslash_n[i].replace("Content:","")
                        
                    i = i+1
                    
                else:
                    if 'content' in header_content_dict:
                        header_content_dict['content'] = header_content_dict['content'] + '\n' + split_backslash_n[i]
                    else:
                        header_content_dict['content'] = split_backslash_n[i]
                    i = i+1
        print(header_content)
    else:
        i = 0
        header_content = []
        while i< len(split_backslash_n):
            if 'Slide' in split_backslash_n[i]:
                header_content.append(split_backslash_n[i+1])
                # header_content.append(split_backslash_n[i+2])
                i = i+2
            else:
                header_content.append(split_backslash_n[i])
                i = i+1
        print(header_content)
    
    X = Presentation()

    Layout = X.slide_layouts[0]
    first_slide = X.slides.add_slide(Layout)

    first_slide.shapes.title.text = topic
    first_slide.placeholders[1].text = "Created by Big Data Lab"

    X.save("First_presentation.pptx")
    for i in header_content:
        if 'header' in i:
            Layout = X.slide_layouts[5]
            slide = X.slides.add_slide(Layout)
            slide.shapes.title.text = i['header']
            textbox = slide.shapes.add_textbox(Inches(3), Inches(1.5),Inches(3), Inches(1)) 
            textframe = textbox.text_frame
            paragraph = textframe.add_paragraph()
            paragraph.text = i['content']
            X.save("First_presentation.pptx")


    return redirect(url_for('index'))