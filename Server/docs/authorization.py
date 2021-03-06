from . import param

LOGIN_POST = {
    'tags': ['Authorization'],
    'parameters': [
        param('userId', "user's ID"),
        param('password', "비밀번호")
    ],
    'responses': {
        '201': {
            'description': "JWT 반환 성공",
            "example": {
                "access_token": "dkAhffkDkanxmsJWTzhemdla",
                "refresh_token": "flvmfptlxhzms"
            }
        },
        '401': {
            'description': "없는 ID이거나 비밀번호가 틀렸습니다."
        }
    }
}

SIGN_UP_POST = {
    'tags': ['Authorization'],
    'description': '어드민 계정 회원가입',
    'parameters': [
        param('userId', "user's ID"),
        param('password', "비밀번호")
    ],
    'responses': {
        '201': {
            'description': "회원가입 성공"
        },
        '401': {
            'description': "회원가입 도중 문제 발생"
        },
        '409': {
            'description': "중복된 계정 감지"
        }
    }

}