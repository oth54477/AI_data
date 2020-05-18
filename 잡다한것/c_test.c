#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>
 
struct connection_details {
 
    char *server;
    char *user;
    char *password;
    char *database;
 
};
 
MYSQL* mysql_connection_setup(struct connection_details mysql_details) {
 
    MYSQL *connection = mysql_init(NULL);
 
    if(!mysql_real_connect(connection, mysql_details.server, mysql_details.user, mysql_details.password, mysql_details.database, 0, NULL, 0)) {
 
        printf("Connection error : %s\n", mysql_error(connection));
        exit(1);
 
    }
    return connection;
}
 
MYSQL_RES* mysql_perform_query(MYSQL *connection, char *sql_query) {
 
    if(mysql_query(connection, sql_query)) {
 
        printf("MYSQL query error : %s\n", mysql_error(connection));
        exit(1);
 
    }
    return mysql_use_result(connection);
}
 
 
int main() {
 
    MYSQL *conn;
    MYSQL_RES *res;
    MYSQL_ROW row;
 
    struct connection_details mysqlD;
    mysqlD.server = "IP주소 or localhost";
    mysqlD.user = "아이디";
    mysqlD.password = "패스워드";
    mysqlD.database = "DB 이름";
 
    conn = mysql_connection_setup(mysqlD);
 
    res = mysql_perform_query(conn, "show tables");
 
    printf("MySQL Tables in mysql database:\n");
    while((row = mysql_fetch_row(res)) != NULL)
        printf("%s\n", row[0]);
 
    mysql_free_result(res);
    mysql_close(conn);
    return 0;
 
}