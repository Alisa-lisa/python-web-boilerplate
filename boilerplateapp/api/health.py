""" endpoint that always returns 200, string. Can be used for k8s healthcheck """
from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/health")
async def health_check():
    return "Healthy!"

