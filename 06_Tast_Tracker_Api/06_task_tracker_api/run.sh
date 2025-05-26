#!/bin/bash
uvicorn app.main:app --reload
chmod +x run.sh
./run.sh
# This script starts the FastAPI application using Uvicorn.