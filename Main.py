from fastapi import FastAPI, HTTPException,APIRouter
from pydantic import BaseModel,EmailStr,Field
from Models import insertstudent,get_all_students,get_student_by_Id,delete_student,Update_student
import uvicorn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from loguru import logger
import sys



class Student(BaseModel):
    name: str = Field(examples=["Ganesh Gaitonde"])
    email: EmailStr = Field(examples=["Gopalmat@gmail.com"])
    age: int = Field(examples=[22])
    phone: int = Field(examples=[1234567890])

    class Config:
        extra = "forbid"



app = FastAPI()

version_v1 = APIRouter()
version_v2 = APIRouter()


logger.add(sys.stdout, format="{time} {level} {message}", filter="my_module",backtrace=True)



@version_v1.post("/AddStudent",status_code=200)
async def create_student(student: Student) -> Student:
    try:
        logger.info("Create student process Started...")
        res = jsonable_encoder(insertstudent(data=student))
        if res['status'] == "success":
            logger.info("Create student process Completed...")
            return JSONResponse(content={"message": "Student data added", "student_id": res["student_id"]})  
        else:
            logger.error("Create student process InComplete...")
            return HTTPException(status_code=400, detail=res['message'])
    except Exception as e:
        logger.error(f"Error while completing the get student process...{e}")
        return JSONResponse(status_code=400, content=e)


@version_v1.get("/GetAllStudents",status_code=200)
async def get_students()  -> dict:
    try:
        logger.info("Get all student process Started...")
        res = jsonable_encoder(get_all_students())
        if res['status'] == "success":
            logger.info("Get all student process Completed...")
            return JSONResponse(content=res['students'])
        else:
            logger.error("Get all student process InComplete...")
            return HTTPException(status_code=400, detail=res['message'])
    except Exception as e:
        logger.error(f"Error while completing the get all student process...{e}")
        return JSONResponse(status_code=400, content=e)
    

@version_v1.get("/GetStudent",status_code=200)
async def get_student(id:int) -> dict:
    try:
        logger.info("Get student process Started...")
        res = get_student_by_Id(id)
        if res['status'] == "success":
            logger.info("Get student process Completed...")
            return JSONResponse(content=res['students'])
        else:
            logger.error("Get student process InComplete...")
            return HTTPException(status_code=400, detail=res['message'])
    except Exception as e:
        logger.error(f"Error while completing the get student process...{e}")
        return JSONResponse(status_code=400, content=e)
    

@version_v2.patch("/UpdateStudent",status_code=200)
async def Update(id:int,student:Student) -> dict:
    try:
        logger.info("Update student process Started...")
        res = Update_student(id, student)
        if res['status'] == "success":
            logger.info("Update student process Completed...")
            return JSONResponse(content=res['students'])
        else:
            logger.error("Update student process InComplete...")
            raise HTTPException(status_code=400, detail=res['message'])
    except Exception as e:
        logger.error(f"Error while completing the update student process...{e}")
        return JSONResponse(status_code=400, content=e)
        
@version_v2.delete("/DeleteStudent",status_code=200)
async def delete(id:int) -> dict:
    try:
        logger.info("Delete student process Started...")
        res = delete_student(id)
        if res['status'] == "success":
            logger.info("Delete student process Completed...")
            return {"Students":res}
        else:
            logger.error("Delete student process InComplete...")
            raise HTTPException(status_code=400, detail=res['message'])    
    except Exception as e:
        logger.error(f"Error while completing the Delete student process...{e}")
        return JSONResponse(status_code=400, content=e)
    

@version_v1.get("/HealthCheck",status_code=200)
async def HealthCheck() -> dict:
    message = "All services is Up"
    return {"message":message}   


app.include_router(version_v1,tags=['Version 1 Api Endpoints'])
app.include_router(version_v2,prefix='/v2',tags=['Version 2 Api Endpoints'])

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
    
   
