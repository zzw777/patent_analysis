cd apps/stanford-corenlp-full-2017-06-09/
sudo java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 150000 &
cd ../../server/
python3 manage.py runserver 127.0.0.1:8000 &
