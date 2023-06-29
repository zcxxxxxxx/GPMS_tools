import pandas as pd
from sqlalchemy import create_engine


def import_csv_to_mysql(file_path, table_name):
    # 连接 MySQL 数据库
    SQLALCHEMY_DATABASE_URL = "mysql://root:password@localhost:3306/gpms"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # 读取 csv 文件
    df = pd.read_csv(file_path)
    df.index += 1
    df = df.rename_axis("id")
    # print(df)
    df.to_sql(table_name, engine, if_exists="append", index=True)
    print(f"{table_name}表导入成功")


if __name__ == "__main__":
    path = [
        "result.csv",
        "selection.csv",
        "status.csv",
        "students.csv",
        "teacher.csv",
        "topic.csv",
        "users.csv",
    ]
    table_name = [
        "result",
        "selection",
        "status",
        "students",
        "teachers",
        "topic",
        "users",
    ]

    for i in range(len(path)):
        import_csv_to_mysql(path[i], table_name[i])
