from flask import request, Blueprint
import json, traceback, os, time
from App.utils import b64decode_

file_blue = Blueprint('file_blue', __name__)

@file_blue.route('/files', methods=['GET'])
def GetFiles():
    try:
        path = request.args.get('path') or '/'
        Files =  sorted(os.listdir(path)) 
        dir_=[]
        file_=[]
        fileQuantity = len(Files)
        for f in Files:
            try:
                f = os.path.join(path, f)
                f_obj = {
                    'fileName': f,
                    'power': oct(os.stat(f).st_mode)[-3:],
                    'fileMODTime':time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(f).st_mtime)),
                }
                if not os.path.isdir(f):
                    if os.path.islink(f):
                        fileLinkPath = os.readlink(f)
                        f_obj['fileOnlyName'] = os.path.split(f)[1] +'-->'+ fileLinkPath
                        f_obj['fileSize'] = ('%.2f' % (os.stat(f).st_size/1024))+'k'
                        f_obj['fileType'] = 'file'
                    else:
                        f_obj['fileOnlyName'] = os.path.split(f)[1]
                        f_obj['fileSize'] = ('%.2f' % (os.path.getsize(f)/1024 ))+'k'
                        f_obj['fileType'] = 'file'
                else:
                    f_obj['fileOnlyName'] = os.path.split(f)[1]
                    f_obj['fileSize'] = ('%.2f' % (os.path.getsize(f)/1024 ))+'k'
                    f_obj['fileType'] = 'dir'
                    dir_.append(f_obj)
            except Exception as e:
                print(e)
                continue
        returnJson = {
            'path': path,
            'fileQuantity': fileQuantity,
            'files':dir_ + file_
        }        
    except Exception as e:
        return json.dumps({'resultCode':1,'result':str(traceback.format_exc())})
    else:
        return json.dumps({'resultCode':0,'result':returnJson})