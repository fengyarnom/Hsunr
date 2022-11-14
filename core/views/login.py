import random

from flask import Blueprint, render_template, request, session, redirect, url_for
from ..lib.Db.Db import select_table
from ..lib.Db.UserModle import UserModle
from ..lib.ResultBody import res2json,ResultCode
bp = Blueprint('login', __name__, url_prefix='/login')

@bp.route("/")
def login():
    if 'username' in session:
        return redirect(url_for('admin.article'))
    return render_template("login.html")

@bp.route("/login-check", methods=['POST'])
def login_check():
    if request.method == "POST":
        request_data = request.json
        user = select_table(
            modle=UserModle(),
            condition="username='{}'".format(request_data['username']),
            limit=1
        )
        if not len(user):
            print(request_data['username'])
            return res2json(ResultCode.USER_NOT_EXIST, "")
        else:
            if user['password'] == request_data['password']:
                session_id = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba', 20))
                session['username'] = session_id
                return res2json(ResultCode.LOGIN_SUCESS,"")
            else:
                return res2json(ResultCode.PASSWORD_ERROR,"")


