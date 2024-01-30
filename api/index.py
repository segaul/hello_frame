from flask import Flask, request, jsonify
import requests
import cloudinary.uploader


app = Flask(__name__)

display_number = 0
HTML_CONTENT_TEMPLATE = '''<!DOCTYPE html>
        <html>
            <head>
                <meta property="og:title" content="Incrementer"/>
                <meta name="fc:frame:post_url" content="TODO - host in vercel"/>
                <meta property="og:image" content="{0}" />
                <meta property="fc:frame" content="vNext" />
                <meta property="fc:frame:image" content="{0}" />
                <meta property="fc:frame:button:1" content="Increment?" />
            </head>
            <body>
                Press button to increment the number
            </body>
        </html>
    '''

def get_new_image_url():




@app.route('/')
def render():
    image_url = get_new_image_url()
    html_content = HTML_CONTENT_TEMPLATE.format(image_url)
    return html_content

@app.route('/api', methods=['POST'])
def increment():
    display_number += 1
    render()

if __name__ == '__main__':
    app.run(debug=True)