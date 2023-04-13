FROM mysql:latest

# 環境変数を設定する
ENV MYSQL_DATABASE chatapp
ENV MYSQL_USER testuser
ENV MYSQL_PASSWORD testuser
ENV MYSQL_ROOT_PASSWORD rootpassword

# データベースの初期化スクリプトを追加する
COPY init.sql /docker-entrypoint-initdb.d/

# my.cnfファイルを追加
COPY my.cnf /etc/mysql/conf.d/my.cnf

# MySQLがUNIXドメインソケットで通信するように設定
RUN mkdir -p /var/run/mysqld && \
    chown -R mysql:mysql /var/run/mysqld && \
    ln -s /var/run/mysqld/mysqld.sock /tmp/mysql.sock


WORKDIR /var/log/mysql/
RUN touch error.txt && chmod 777 error.txt
WORKDIR /

# ポートを公開する
EXPOSE 3306

# MySQL設定を変更する
# RUN sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
#    echo '[mysqld]\nskip-host-cache\nskip-name-resolve' > /etc/mysql/conf.d/docker.cnf

# pymysqlライブラリをインストールする
# RUN pip install pymysql
CMD ["sh", "-c", "exec /usr/local/bin/docker-entrypoint.sh mysqld"]
