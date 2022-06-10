from fastapi import FastAPI
from lib_c.lib_c.utils import utils
from lib_d.lib_d.foo import foo_helper

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Service A using {foo_helper()} and {utils()}"}
