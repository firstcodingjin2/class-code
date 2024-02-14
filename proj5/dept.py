import db


#print(db.DeptDao().get_depts())

def main() :
    
    while True :
        select_num = display_menu()
        print(select_num)
        
        match select_num :
            case 1:
                print(111)
            case 2:
                print(222)
            case 3:
                print(333)
            case 4:
                print(444)
            case 5:
                break
            case _:
                print('메뉴의 번호를 정확히 입력하세요.')
        
    print('프로그램 종료')
    

def display_menu() :
    print('부서 관리 프로그램')
    print('1. 전체 리스트 출력')
    print('2. 부서 정보 입력')
    print('3. 부서 정보 수정')
    print('4. 부서 삭제')
    print('5. Exit')
    print('메뉴 번호를 선택하세요')
    return input('선택 >>>')


if __name__ == '__main__':
    main()