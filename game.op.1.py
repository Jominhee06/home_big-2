from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# 데이터베이스 연결 함수
def get_db_connection():
    conn = sqlite3.connect('rpg_game_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# 접속 데이터 추가 엔드포인트 (예시)
@app.route('/add_activity', methods=['POST'])
def add_activity():
    user_id = request.json['user_id']
    login_time = datetime.strptime(request.json['login_time'], '%Y-%m-%d %H:%M:%S')
    logout_time = datetime.strptime(request.json['logout_time'], '%Y-%m-%d %H:%M:%S')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO user_activity (user_id, login_time, logout_time)
    VALUES (?, ?, ?)
    ''', (user_id, login_time, logout_time))
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success'}), 201

# 접속률 조회 엔드포인트
@app.route('/get_activity_rate', methods=['GET'])
def get_activity_rate():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    
    start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT COUNT(DISTINCT user_id) AS active_users
    FROM user_activity
    WHERE login_time BETWEEN ? AND ?
    ''', (start_time, end_time))
    result = cursor.fetchone()
    active_users = result['active_users']
    conn.close()
    
    return jsonify({'active_users': active_users})

if __name__ == '__main__':
    app.run(debug=True)
