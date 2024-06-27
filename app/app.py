import gradio as gr
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/tammy/test')
async def test(request: Request):
    return JSONResponse(content={"message": "Test Endpoint"})

@app.get('/')
async def test(request: Request):
    return JSONResponse(content={"message": "Root Endpoint"}) # should conflict with main demo

# @app.get('/tammy/sub')
# async def test(request: Request):
#     return JSONResponse(content={"message": "Sub Endpoint"})

@app.get('/')
async def test(request: Request):
    return JSONResponse(content={"message": "Root Endpoint"}) # should conflict with main demo

with gr.Blocks() as main_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Main demo Gradio app started!"))


with gr.Blocks() as sub_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Sub demo Gradio app started!"))

gr.mount_gradio_app(app, main_demo, path="/tammy", root_path="/tammy")

gr.mount_gradio_app(app, sub_demo, path="/tammy/sub", root_path="/tammy")

if __name__ == '__main__':
    uvicorn.run(app, root_path="/tammy") # root_path seems to have no effect