cp ../qgis/python/plugins/saga/*.py .
cp ../qgis/python/plugins/saga/saga.png .
patch plugin.py plugin.diff
GIT_DIR=../qgis/.git git log -n 10 > GitLog
