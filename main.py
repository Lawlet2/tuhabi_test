from functools import lru_cache
from typing import Optional

from fastapi import Depends, FastAPI, HTTPException

from database.manager import MySQLConnectionManager

from config import Settings
from serializers import property_serializer
from filters import property_filter


app = FastAPI(
    title="tuhabiAPI",
    description="API with high performance "
                "to filter properties by city, "
                "address and year",
    version="1.0.0"
)


@lru_cache()
def get_settings():
    """ function to return cached app settings"""
    return Settings()


@app.get("/properties")
def get_properties(
        settings: Settings() = Depends(get_settings),
        year: Optional[str] = None,
        city: Optional[str] = None,
        state: Optional[str] = None
):
    """get properties endpoint"""
    if state:
        raise HTTPException(
            status_code=400,
            detail="The state field does "
                   "not exist in db thus "
                   "this parameter is not valid"
        )

    with MySQLConnectionManager(
            user=settings.db_user,
            password=settings.db_password,
            host=settings.db_host,
            port=settings.db_port,
            database=settings.db_name
    ) as Connection:

        query = property_filter(
            allowed_statuses=settings.allowed_statuses,
            year=year,
            city=city
        )

        executed_query = Connection.execute_query(query)
        data = property_serializer(executed_query)
    return data
