import pymysql

class db_connection : 
  def __init__(self):
    pass
  
  @classmethod
  def get_db(self):
    return pymysql.connect(
      host='localhost', 
      user='bit', 
      password='bit', 
      db='project', 
      charset='utf8',
      autocommit=True
      )
   

class DeptDao:
  def __init__(self):
    pass
    
  def get_depts(self):
    ret = []     
    #db = get_db()
    print()
    curs = db_connection.get_db().cursor()
        
    sql = "select * from dept";
    curs.execute(sql)
        
    rows = curs.fetchall()
    for e in rows:
      temp = {'deptno':e[0],'dname':e[1],'loc':e[2] }
      ret.append(temp)
        
    db_connection.get_db().commit()
    db_connection.get_db().close()
    return ret
    
  def insert_dept(self, deptno, dname, loc):       
    curs = db_connection.get_db().cursor()    
    sql = 'insert into dept values(%s, %s, %s)'
    insert_num = curs.execute(sql,(deptno, dname, loc))
    #db_connection.get_db().commit()
    db_connection.get_db().close()
    return 'insert ok {0}'.format(insert_num)
    
  def update_dept(self, deptno, dname, loc):     
    curs = db_connection.get_db().cursor()    
    sql = "update dept set dname=%s, loc=%s where deptno=%s"
    curs.execute(sql,(dname, loc, deptno))
    #db_connection.get_db().commit()
    db_connection.get_db().close()
    
  def delete_dept(self, deptno):    
    curs = db_connection.get_db().cursor()    
    sql = "delete from dept where deptno=%s"
    curs.execute(sql, deptno)
    #db_connection.get_db().commit()
    db_connection.get_db().close()

if __name__ == '__main__':
  #print(DeptDao().insert_dept(11, 'test1', 'loc1'))
  #print(DeptDao().update_dept(11, 'test333', 'loc444'))
  #print(DeptDao().delete_dept(11))
  emplist = DeptDao().get_depts()
  print(emplist)