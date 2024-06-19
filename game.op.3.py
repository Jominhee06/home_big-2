from flask import Flask, request, jsonify
from flask_expects_json import expects_json
import sqlite3
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# 데이터베이스 연결 함수
def get_db_connection():
    conn = sqlite3.connect('rpg_game_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# 요청 데이터 스키마 정의
class ActivitySchema(Schema):
    user_id = fields.Str(required=True)
    login_time = fields.DateTime(format='%Y-%m-%d %H:%M:%S', required=True)
    logout_time = fields.DateTime(format='%Y-%m-%d %H:%M:%S', required=True)

activity_schema = ActivitySchema()

# 접속 데이터 추가 엔드포인트
@app.route('/add_activity', methods=['POST'])
@expects_json(activity_schema)
def add_activity():
    try:
        data = request.get_json()
        activity_schema.load(data)
        
        user_id = data['user_id']
        login_time = datetime.strptime(data['login_time'], '%Y-%m-%d %H:%M:%S')
        logout_time = datetime.strptime(data['logout_time'], '%Y-%m-%d %H:%M:%S')
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO user_activity (user_id, login_time, logout_time)
        VALUES (?, ?, ?)
        ''', (user_id, login_time, logout_time))
        conn.commit()
        conn.close()
        
        return jsonify({'status': 'success'}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

# 접속률 조회 엔드포인트
@app.route('/get_activity_rate', methods=['GET'])
def get_activity_rate():
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    
    if not start_time or not end_time:
        return jsonify({'error': 'start_time and end_time are required'}), 400

    try:
        start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return jsonify({'error': 'Invalid datetime format'}), 400

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
