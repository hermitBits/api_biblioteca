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
from database.utils import check_db_connected 
if check_db_connected() is False:
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