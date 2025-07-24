from fastapi import FastAPI
from fastapi.responses import FileResponse
from db_lite import SessionDep, create_db, sqlite_file_name, refresh
from model import Payload, Data
import json 

app = FastAPI()

@app.on_event('startup')
def on_startup():
    create_db()

@app.trace('/')
def isAlive():
    return {'isAlive': True}

@app.post('/create')
def test(body: Payload, session: SessionDep):
    
    request_str = json.dumps(body.request)
    response_str = json.dumps(body.request)

    data = Data(url=body.url, 
                method=body.method, 
                request=request_str, 
                response=response_str)
    session.add(data)
    session.commit()
    session.refresh(data)

    return {'saved'}

@app.get('/file')
def getFile():
    return FileResponse(sqlite_file_name, 
                        filename = 'data.bd', 
                        media_type='application/octet-stream')

@app.delete('/file')
def refreshFile():
    refresh()
    return {'refresh'}
