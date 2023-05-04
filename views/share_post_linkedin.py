from app import app
from flask import render_template, request, redirect, url_for
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.environ.get('API_KEY')
import requests
import json
@app.route('/linkedin_post')
def linkedin_post():
    return render_template('linkedin_share.html')


@app.route('/create_linkedin_post', methods=['POST'])
def create_linkedin_post():
    print("I am in")
    messages = [
        {"role": "system", "content": "You’re a kind helpful assistant"}
    ]
    request_text = request.form['post-content']
    create_linkedin_post = f"Please write a LinkedIn post on {request_text}"

    messages.append({"role": "user", "content": create_linkedin_post})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    result_from_gpt = completion.choices[0].message.content
    print(result_from_gpt)

    # Set your access token
    # A is removed from the tocken for security reasons QV is the first two letters of the token, i also removed
    ACCESS_TOKEN = 'AQVTyBEx9iMB1mxu9wsqo5UBWNCcXsNDZIWHjZ3h2KGRlN_wSWgADIKebeV65aXWTVUVeNC8dtDWPtBNtobqou8eYWIZCgham2j7hoQoaxXdDy_0eKi2hkqxF8btclfgpTScerywPvX77OsTsLpr88SjJ1AKcTsK5AoLWw5-Wu8H3fkT6sBm9z7UxyTbPTeKslQ1xAH6Ma3cuFmAq0X-X5SqJla8KujRuEYMDNuwfnRC34nVbXN30xFlaovueGqm5J2b3_e8i5xphp0g4hQQa29_D0CwnJjQkto0Hxy3h-z9oaqG5gFpFwkPGDRJ0dLymZH__EqrgJapr90cvjaXlLt1TfWtw'

    # Set the API endpoint URL
    API_URL_User = 'https://api.linkedin.com/v2/me'
    API_URL_Share = 'https://api.linkedin.com/v2/ugcPosts'

    # Set the headers
    headers = {
        'Authorization': 'Bearer ' + ACCESS_TOKEN,
        'Content-Type': 'application/json'
    }

    # Make the GET request to fetch data about myself on LinkedIn
    response_user = requests.get(API_URL_User, headers=headers)
    user_id = ""
    if response_user.status_code == 200:
        # Get the JSON data from the response
        json_data = response_user.json()
        
        # Access the profile information
        print('ID:', json_data['id'])
        user_id = json_data['id']

    
    # Set the post content
    post_content = {
        "author": "urn:li:person:" + user_id,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": result_from_gpt
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    # # Make the POST request to share the post
    response = requests.post(API_URL_Share, headers=headers, data=json.dumps(post_content))

    # Check the response status code
    if response.status_code == 201:
        print('Post shared successfully!')
    else:
        print('Error sharing post: ' + response.text)
    return redirect(url_for('linkedin_post'))