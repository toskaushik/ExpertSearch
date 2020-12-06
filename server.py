from flask import Flask
from flask import render_template, request, jsonify
import json
import metapy
import sys
import re


app = Flask(__name__) 
environ = 'development'
dataconfig = json.loads(open("config.json", "r").read())
app.dataenv = dataconfig[environ]
app.rootpath = dataconfig[environ]["rootpath"]
app.datasetpath = dataconfig[environ]['datasetpath']
app.searchconfig = dataconfig[environ]['searchconfig']
index = metapy.index.make_inverted_index(app.searchconfig)
query = metapy.index.Document()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = json.loads(request.data.decode('utf-8'))
    querytext = data['query']
    query = metapy.index.Document()
    query.content(querytext)
    min_score = 0.3
    num_results = 10
    sys.path.append(app.rootpath + "/expertsearch")
    ranker = metapy.index.OkapiBM25()
    results = ranker.score(index, query, 100)
    filtered_results = []
    res_cnt = 0
    for res in results:
        print(res[1])
        if (res[1] > min_score):
            filtered_results.append(res)
            res_cnt += 1
            if res_cnt == num_results:
                break

    document_names = [index.metadata(res[0]).get('document_name') for res in filtered_results]
    doctor_names = [index.metadata(res[0]).get('doctor_name') for res in filtered_results]
    doctor_profile_urls = [index.metadata(res[0]).get('url') for res in filtered_results]
    previews = _get_doc_previews(document_names, querytext)
    docs = list(zip(document_names, previews, doctor_names, doctor_profile_urls))

    return jsonify({
        "docs": docs
    })

def _get_doc_previews(document_names,querytext):
    return list(map(lambda d: _get_preview(d,querytext), document_names))

def format_string(matchobj):
    
    return '<b>'+matchobj.group(0)+'</b>'

def _get_preview(document_names,querytext):
    preview = ""
    num_lines = 0
    preview_length = 2
    fullpath = app.datasetpath + "/" + document_names

    with open(fullpath, 'r') as fp:
        while num_lines < preview_length:
            line = fp.readline()
            found_phrase = False
            if not line:
                break
            formatted_line = str(line.lower())
            for w in querytext.lower().split():

                (sub_str,cnt) = re.subn(re.compile(r"\b{}\b".format(w)),format_string,formatted_line)

                if cnt>0:
                    formatted_line = sub_str
                    found_phrase = True 

            if found_phrase:
                preview += formatted_line

                num_lines += 1
        fp.close()
 
    short_preview = ''
    prev_i = 0
    start = 0
    words = preview.split()
    cnt = 0
    i=0
   
    while i<len(words):
        

        
        if '<b>' in words[i]:
            start = min(i-prev_i,5)
            
            if  i-start>0:
                short_preview += '...'
            short_preview += ' '.join(words[i-start:i+5])
            i+=5
            prev_i = i
            cnt +=1
        else:
            i+=1
        if cnt==3:
            break


    return short_preview



if __name__ == '__main__':
    environ = 'development'
    dataconfig = json.loads(open("config.json", "r").read())
    app.dataenv = dataconfig[environ]
    app.rootpath = dataconfig[environ]["rootpath"]
    app.datasetpath = dataconfig[environ]['datasetpath']
    app.searchconfig = dataconfig[environ]['searchconfig']

    app.run(debug=True,threaded=True,host='localhost',port=8095)
