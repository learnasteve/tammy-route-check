import gradio as gr
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()



@app.get('/tammy/test')
async def test(request: Request):
    return JSONResponse(content={"message": "Test Endpoint"})

# @app.get('/tammy/routes')
# def get_mounted_apps():
#     routes = []
#     for route in app.routes:
#         methods = ', '.join(route.methods) if hasattr(route, 'methods') else 'No methods'
#         routes.append({"path": route.path, "name": getattr(route, 'name', 'No name'), "methods": methods})

#         if isinstance(route, Mount):
#                 routes.append({"path": route.path, "name": route.name, "app": str(route.app)})

#     return {"mounted_routes": routes}

# @app.get('/')
# async def test(request: Request):
#     return JSONResponse(content={"message": "Root Endpoint"}) # should conflict with main demo

# @app.get('/tammy/sub')
# async def test(request: Request):
#     return JSONResponse(content={"message": "Sub Endpoint"})

with gr.Blocks() as main_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Main demo Gradio app started here!"))


with gr.Blocks() as sub_demo:
    with gr.Row():
        gr.Markdown("""# <center><font size=8>{}</center>""".format("Sub demo Gradio app started!"))

app = gr.mount_gradio_app(app, main_demo, path="/tammy/main")

app = gr.mount_gradio_app(app, sub_demo, path="/tammy/sub")

if __name__ == '__main__':
    uvicorn.run(app) # root_path seems to have no effect