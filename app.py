from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/")
async def main():
    return "server is up:)"


items = {"foo": "this is foo", "voo": "this is voo"}


@app.get("/items/{item_id}")
async def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="item not found")
    return items[item_id]
