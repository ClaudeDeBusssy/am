from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3


app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

color = { "id": "",
       "name":"",
       "hexcode": ""
       }


@app.get("/colors", tags=["colors"])
async def get_colors() -> dict:
    return { "data": get_colors_from_database() }


@app.get("/colors/", tags=["search"])
async def get_searched_colors(search: str) -> dict:
    
    return { "data": get_colors_from_database(search) }



def get_colors_from_database(search=""):
    database = sqlite3.connect("colors.db")
    cursor = database.cursor()
    result = ""

    if search:

        search = '"%' + search.replace('"', "") + '%"'

        sql =  """
            select * from colorTable where color_name like {search};
            """.format(search=search)
        print(search)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
    else:
        cursor.execute(
            """
            select * from colorTable;
            """
        )
        result = cursor.fetchmany(10)
    
    colordata = []
    for entry in  result:
        colordata.append({ 
        "id": entry[0],
        "name":entry[1],
        "hexcode": entry[2]
       })
        
    return colordata