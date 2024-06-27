import gradio as gr
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/tammy/test')
async def test(request: Request):
    return JSONResponse(content={"message": "Test Endpoint"})

with gr.Blocks() as main_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Main demo Gradio app started!"))


with gr.Blocks() as sub_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Sub demo Gradio app started!"))

app = gr.mount_gradio_app(app, main_demo, path="/tammy", root_path="/tammy")

app = gr.mount_gradio_app(app, sub_demo, path="/tammy/sub", root_path="/tammy")

if __name__ == '__main__':
    uvicorn.run(app, root_path="/tammy")