import asyncio
import os
import sys
import threading

import uvicorn
from starlette.applications import Starlette
from starlette.responses import JSONResponse

from carboniq.emissions import carbon_profiler

app = Starlette(debug=True)


@app.route(f"/home", methods=["GET"])
@carbon_profiler(real_time=True)
async def home(request):
    return JSONResponse({"message": "Welcome to CarbonIQ with Starlette!"})

async def main():
    """
    Entry point for the server.
    """
    port = int(os.environ.get("PORT", 8009))
    server_thread = threading.Thread(
        target=uvicorn.run,
        args=(app,),
        kwargs={"host": "0.0.0.0", "port": port},
    )
    server_thread.start()

    if "serve" in sys.argv:
        production_port = 80
        port = int(os.environ.get("PORT", production_port))
        server_thread = threading.Thread(
            target=uvicorn.run,
            args=(app,),
            kwargs={"host": "0.0.0.0", "port": port},
        )
        server_thread.start()


if __name__ == "__main__":
    asyncio.run(main())