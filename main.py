import uvicorn
from fastapi import FastAPI
from api.settings import API_HOST, DEBUG, PORT, RELOAD
from api.router import router


app = FastAPI(
    debug=DEBUG,
    title='API CTI',
    version='0.0.1',
    description='API em Desenvolvimento',
    docs_url='/api/v1/docs'
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host=API_HOST, port=PORT, reload=RELOAD)
