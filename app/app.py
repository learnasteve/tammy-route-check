import gradio as gr
import uvicorn
import fastapi # to get version
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
# from fastapi.routing import APIRouter


print("### Gradio: ", gr.__version__)
print("### FastAPI: ", fastapi.__version__)
print("### Uvicorn: ", uvicorn.__version__)

# router = APIRouter()

app = FastAPI()
#app = FastAPI(path="/tammy")

@app.get('/tammy/test')
async def test(request: Request):
    root_path = request.scope.get('root_path', 'No root path')
    return JSONResponse(content={"message": "Test Endpoint", "root_path": root_path})

@app.get('/tammy/routes')
def get_mounted_apps():
    routes = []
    for route in app.routes:
        methods = ', '.join(route.methods) if hasattr(route, 'methods') else 'No methods'
        routes.append({"path": route.path, "name": getattr(route, 'name', 'No name'), "methods": methods})

        # if isinstance(route, Mount):
        #         routes.append({"path": route.path, "name": route.name, "app": str(route.app)})

    return {"routes": routes}

# @app.get('/')
# async def test(request: Request):
#     return JSONResponse(content={"message": "Root Endpoint"}) # should conflict with main demo

# @app.get('/tammy/sub')
# async def test(request: Request):
#     return JSONResponse(content={"message": "Sub Endpoint"})

with gr.Blocks() as main_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Main demo Gradio app started here!"))


def echo(message, history):
    return message

with gr.Blocks() as chat_demo:
    with gr.Row():
        demo = gr.ChatInterface(fn=echo, examples=["hello", "hola", "kia ora"], title="Echo Bot")
        
with gr.Blocks() as sub_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Sub demo Gradio app started!"))

app = gr.mount_gradio_app(app, main_demo, path="/tammy/main", root_path="/tammy/main")

app = gr.mount_gradio_app(app, sub_demo, path="/tammy/dir/sub", root_path="/tammy/dir/sub")

app = gr.mount_gradio_app(app, chat_demo, path="/tammy/chat", root_path="/tammy/chat")

if __name__ == '__main__':
    uvicorn.run(app, root_path="/tammy")