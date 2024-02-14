from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config  as db_config

	
# 데이터 베이스와 연동
database = create_engine(db_config.DB_URL, encoding = 'utf-8', max_overflow = 0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_dept(deptno):
    dept = database.execute(str("""
        SELECT 
            deptno,
            dname,
            lod
        FROM dept
        WHERE deptno = :deptno
    """), {
        'deptno' : deptno
    }).fetchone()

    return {
        'deptno' : dept['deptno'],
        'dname'  : dept['dname'],
        'loc'    : dept['loc']
    } 
    
get_dept(10)
