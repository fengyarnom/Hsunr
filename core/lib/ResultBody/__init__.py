from enum import Enum
from flask import jsonify

class ResultCode(Enum):
    SUCCESS = {"code": 200, "message": "Success"}
    SUCCESS_POST_CREATED = {"code": 201, "message": "文章创建成功"}
    SUCCESS_POST_MODIFIED = {"code": 202, "message": "文章修改成功"}
    SUCCESS_POST_DELETE = {"code": 203, "message": "文章删除成功"}

    LOGIN_SUCESS = {"code": 301, "message": "Successfully Login ,Relocation to admin"}

    PARAMETER_ERROR= {"code": 401, "message": "Parameter passing error"}
    USER_NOT_EXIST = {"code": 410, "message": "User does not exist"}
    PASSWORD_ERROR = {"code": 411, "message": "Password error"}
    AUTHORIZATION_FAILED = {"code": 420, "message": "Authorization failed"}



def res2json(result_code, data):
    return jsonify({
        'code': result_code.value['code'],
        'data': data,
        'message': result_code.value['message']
    })