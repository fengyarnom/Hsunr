import random

from flask import Blueprint, render_template, request, session, redirect, url_for
from ..lib.Db.Db import select_table
from ..lib.Db.UserModle import UserModle
from ..lib.ResultBody import res2json,ResultCode
bp = Blueprint('login', __name__, url_prefix='/admin/login')




