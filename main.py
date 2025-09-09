from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Define a route for the current user
@app.get("/users/me")
async def read_current_user():
    # Return a fixed response for the current user
    return {"user_id": "The current awesome user"}

# Define a route that takes a user_id as a path parameter
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    # Return the user_id received in the path
    return {"user_id": user_id}
