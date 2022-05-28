#!/bin/bash
# if any of the commands in your code fails for any reason, the entire script fails
set -o errexit
# fail exit if one of your pipe command fails
set -o pipefail
# # exits if any of your variables is not set
# set -o nounset

mysql_ready() {
python << END
from os import getenv
import sys
import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host=f"{getenv('MYSQL_SERVICE')}",
                                            database=f"{getenv('MYSQL_DATABASE')}",
                                            user=f"{getenv('MYSQL_USER')}",
                                            password=f"{getenv('MYSQL_ROOT_PASSWORD')}")
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