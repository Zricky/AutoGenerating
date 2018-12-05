# -*- coding:utf-8 -*-
#  @author       :  zhaojx
#  @date         :  2018/12/5 9:46
#  @description  :  
#  @version      :  V_1.0
#  {\____/}
# ( • . • )
# /    >🐍 人生苦短，我用python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
import re


class Generating():
    def __init__(self):
        engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def __genTable__(self):
        for schema in Config.SCHEMA_CONFIG['SCHEMA']:
            table = self.session.execute(r'SELECT '
                                         r'COLUMN_NAME,COLUMN_TYPE,IS_NULLABLE,COLUMN_KEY,COLUMN_COMMENT '
                                         r'FROM	information_schema. COLUMNS'
                                         r' WHERE	'
                                         r'table_name = "{table_name}"'
                                         r''.format(table_name=schema['table_name'])).fetchall()
            self.__genClass__(table, schema['table_name'], schema['class_name'], schema['class_path'])

    def __genClass__(self, table, tableName, className, classPath):
        templet = []
        templet.append("class {class_name}(Base,Table):".format(class_name=className))
        templet.append("\t__tablename__ = '{table_name}'".format(table_name=tableName))
        for column in table:
            primary_key = 'primary_key=False'
            nullable = 'nullable=False'
            if (column[4] != ''):
                annotation = "\t# ::column {} {}".format(column[0], column[4])
                templet.append(annotation)
            if (column[2] == 'YES'):
                nullable = 'nullable=True'
            if (column[3] == 'PRI'):
                primary_key = 'primary_key=True'
            if (re.match(r'char|bigint', str(column[1])) != None):
                column_type = str(column[1]).upper()
            if (re.match(r'varchar', str(column[1])) != None):
                column_type = 'String'
            if (re.match(r'datetime', str(column[1])) != None):
                column_type = 'DateTime'
            line = '\t{column_name} = Column({column_type},{primary_key},{nullable})'.format(
                column_name=str(column[0]).lower(),
                column_type=column_type,
                primary_key=primary_key,
                nullable=nullable
            )
            templet.append(line)
        self.__genPythonFile__(templet,classPath)

    def __genPythonFile__(self, templet, classPath):
        with open(classPath, 'a+', encoding='utf-8') as file:
            for line in templet:
                file.write(line)
                file.write('\n')


if __name__ == '__main__':
    Generating().__genTable__()
