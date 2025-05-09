from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/batman", response_class=HTMLResponse)
async def get_batman():
    html_content = """
    <html>
        <head>
            <title>I am Batman</title>
            <style>
                body {
                    background-color: black;
                    color: yellow;
                    font-family: 'Arial', sans-serif;
                    text-align: center;
                    padding-top: 100px;
                }
                h1 {
                    font-size: 3em;
                    text-shadow: 2px 2px 10px #FFD700;
                }
            </style>
        </head>
        <body>
            <h1>HELLO I am Batman!</h1>
        </body>
    </html>
    """
    return html_content
