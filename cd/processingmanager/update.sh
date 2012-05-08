cp ../qgis/python/plugins/processingmanager/*.py .
cp ../qgis/python/plugins/processingmanager/processing*.png .
cp ../qgis/python/processing/*.py processing
GIT_DIR=../qgis/.git git log -n 10 > GitLog
