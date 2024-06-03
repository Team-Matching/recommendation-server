import mysql.connector
import pandas as pd

def get_data_from_db():
    # MySQL 데이터베이스 연결 설정
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0000',
        database='teammatchingdb'
    )

    try:
        # SQL 쿼리 작성
        query = """
        SELECT 
            m.member_id,
            m.email,
            m.name,
            m.nickname,
            m.birthdate,
            m.phone_number,
            GROUP_CONCAT(DISTINCT c.company ORDER BY c.start_date SEPARATOR '; ') AS careers,
            GROUP_CONCAT(DISTINCT cert.certification_name ORDER BY cert.date_obtained SEPARATOR '; ') AS certifications,
            GROUP_CONCAT(DISTINCT e.institution ORDER BY e.start_year SEPARATOR '; ') AS educations,
            GROUP_CONCAT(DISTINCT s.skill ORDER BY s.skill SEPARATOR '; ') AS skills,
            GROUP_CONCAT(DISTINCT i.interest ORDER BY i.interest SEPARATOR '; ') AS interests
        FROM 
            member m
        LEFT JOIN 
            career c ON m.member_id = c.member_id
        LEFT JOIN 
            certification cert ON m.member_id = cert.member_id
        LEFT JOIN 
            education e ON m.member_id = e.member_id
        LEFT JOIN 
            member_skill ms ON m.member_id = ms.member_id
        LEFT JOIN 
            skill s ON ms.skill_id = s.skill_id
        LEFT JOIN 
            member_interest mi ON m.member_id = mi.member_id
        LEFT JOIN 
            interest i ON mi.interest_id = i.interest_id
        GROUP BY 
            m.member_id, m.email, m.name, m.nickname, m.birthdate, m.phone_number;
        """

        # 데이터베이스에서 데이터 가져오기
        df = pd.read_sql(query, connection)
        
        return df

    finally:
        # 연결 종료
        connection.close()


def get_post_data_db():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0000',
        database='teammatchingdb'
    )
    try:
        # SQL 쿼리 작성
        query = """
        SELECT 
            p.post_id,
            p.title,
            p.detail,
            p.summary,
            c.name as category
        FROM post p
        LEFT JOIN 
            category c ON c.category_id = p.category_id

        """

        # 데이터베이스에서 데이터 가져오기
        df = pd.read_sql(query, connection)
        
        return df

    finally:
        # 연결 종료
        connection.close()


