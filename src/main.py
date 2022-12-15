from fastapi import FastAPI, Request, Form
from typing import Optional
from pydantic import BaseModel
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

#Commande pour exécuter le serveur:
#uvicorn main:app --reload

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class Twot(BaseModel):
    id: int
    content: str
    media: str

@app.get('/')
async def homepage(request: Request) :
    return templates.TemplateResponse(
        'homepage.html', {'request': request})

@app.get('/{username}')
def userpage(request: Request, username: str, twots: list = []): #Après il faudra enlever le paramètre "twots" et les récupérer directement dans la BdD
    return templates.TemplateResponse('user.html', {'request' : request, "username":username, "displayname":username, "twots": twots})

@app.post('/{username}')
def post_tweet(request: Request, username: str, content: str = Form()):
    return userpage(request, username, [{"username": username, "content": content}])

"""@app.get('/{user}/tweet')
def tweet(user: str, limit: int = 10, sort: Optional[str] = None):
    return {'tweet': f'{limit} tweets depuis la BdD'}"""