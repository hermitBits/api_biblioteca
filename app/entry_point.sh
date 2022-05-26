#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# # exits if any of your variables is not set
# set -o nounset

mysql_ready() {
python << END
import sys
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host="mysqlsrv",
                                            database="biblioteca_api",
                                            user="root",
                                            password="c4r410")
except:
    sys.exit(-1)
sys.exit(0)
END
}
until mysql_ready; do
  >&2 echo 'Waiting for Mysql to become available...'
  sleep 1
done
>&2 echo 'Mysql is available'

uvicorn main:app --reload --host 0.0.0.0 --port 8000