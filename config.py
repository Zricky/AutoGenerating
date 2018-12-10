# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/4 11:18
#  @description  :  配置文件


class Config():
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://。。。/dbissmadm?charset=utf8'
    """
    :param table_name 表名
    :param class_name 生成类名
    :param class_path 类文件路径
    """
    SCHEMA_CONFIG = {
        'SCHEMA': [
            {
                'table_name': 'or_task_dispatch',
                'class_name': 'TaskDispatch',
                'class_path':'D:\\PycharmProjects\\AutoGenerating\\model.py'
            }
        ]
    }


class DevelopmentConfig(Config):
    


class TestConfig(Config):
    


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'test': TestConfig,
    'default': DevelopmentConfig
}
