import pymysql

# db 연결한 Connection 객체를 반환하는 함수
def db_conn():

    db = pymysql.connect(
        host='localhost',
        user='bit',
        password='bit',
        db='project',
        charset='utf8',
        autocommit=True
    )

    return db

# DAO : 데이터베이스 처리를 위한 함수
# select, select 검색, insert, update, delete

# select List : select의 결과를 [{},{},{}...]
def selectDept() :

    result = []
    try:
        con = db_conn()

        cursor = con.cursor(cursor=pymysql.cursors.DictCursor)

        sql_select = 'select * from dept;'
        cursor.execute(sql_select)

        result = cursor.fetchall()

        cursor.close()
        con.close()
    except Exception as e:
        pass
          
    return result

# 부서 검색 : 부서 번호
def selectDeptbyDeptno(deptno):
    # Connection
    con = db_conn()

    # Cursor
    cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
    sql_select = 'select * from dept where deptno=%s'    
    cursor.execute(sql_select, deptno)
    result  = cursor.fetchone()

    cursor.close()
    con.close

    return result

# 입력 : list, dict, class Product
def insertDept(dname, loc):
    con = db_conn()
    cursor = con.cursor()

    sql_insert = 'insert into dept (dname, loc) values (%s, %s)'
    result_num = cursor.execute(sql_insert,(dname, loc))

    cursor.close()
    con.close()

    return result_num

# 부서 정보 수정 : 
def uupdateDept(deptno, dname, loc):
    con = db_conn()
    cursor = con.cursor()

    sql_update = 'update dept set dname=%s, loc=%s where deptno=%s'
    result_num = cursor.execute(sql_update, (dname, loc, deptno))

    cursor.close()
    con.close()

    return result_num

# 부서 정보 삭제 : 부서번호
def deleteDeptbydeptno(deptno) :
    con = db_conn()
    cursor = con.cursor()

    sql_delete = 'delete from dept where deptno=%s'
    result_num = cursor.execute(sql_delete, deptno)

    cursor.close()
    con.close()

    return result_num




if __name__ == '__main__':
    #conn = db_conn()
    #print(conn)
    #conn.close()
    result = selectDept()
    print(result)
    # result= selectDeptbyDeptno(80)
    # print(result)

    # if result :
    #     print('회원 인증: 로그인')
    # else :
    #     print('아이디 또는 비번을 확인해주세요')
    # result = insertDept('개발팀', '서울')
    # if result :
    #     print('성공')
    # else :
    #     print('실패')

    # result = uupdateDept(52, 'QA', '판교')
    # print(result)

    #print(deleteDeptbydeptno(55))
