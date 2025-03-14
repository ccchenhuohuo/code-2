"""
routes/__init__.py

这个文件是routes包的初始化文件，负责：
1. 定义各个功能模块的蓝图
2. 导入各个路由模块
3. 提供注册所有路由的函数

routes/
├── __init__.py             # 定义蓝图并提供路由注册函数
├── auth_routes.py          # 认证相关路由
├── user_routes.py          # 用户相关路由
├── admin_routes.py         # 管理员相关路由
└── monte_carlo_routes.py   # 蒙特卡洛模拟API路由
"""
from flask import Blueprint, redirect, url_for

# 创建蓝图
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
user_bp = Blueprint('user', __name__, url_prefix='/user')
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# 创建主路由蓝图
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """将根路径重定向到auth.index"""
    return redirect(url_for('auth.index'))

@main_bp.route('/logout')
def logout():
    """将根路径的登出请求重定向到auth.logout"""
    return redirect(url_for('auth.logout'))

# 移动导入语句到register_routes函数内，防止循环导入
# from . import auth_routes
# from . import user_routes
# from . import admin_routes
# from .monte_carlo_routes import monte_carlo_bp

def register_routes(app):
    """
    注册所有路由到Flask应用
    
    参数:
    app (Flask): Flask应用实例
    """
    # 导入路由模块
    from . import auth_routes
    from . import user_routes
    from . import admin_routes
    from .monte_carlo_routes import monte_carlo_bp
    
    # 注册主路由蓝图
    app.register_blueprint(main_bp)
    
    # 注册其他蓝图
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(monte_carlo_bp) 