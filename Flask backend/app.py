from flask import Flask, request, send_from_directory, Response
import endpoints as ep
from flask_cors import CORS, cross_origin

application = Flask(__name__, static_url_path='')
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route('/<path:path>')
def sends__(path):
    return send_from_directory('static', path)

@cross_origin
@application.route('/api/getsp500')
def api_sp500():
    global Response
    return Response(ep.getAllTickers(), mimetype='application/json')

@cross_origin
@application.route('/api/analystdata/<symbol>')
def api_analysts(symbol):
    global Response
    return Response(ep.getAnalystData(symbol), mimetype='application/json')

@cross_origin
@application.route('/api/companyinfo/<symbol>')
def api_info(symbol):
    global Response
    return Response(ep.companyInfo(symbol), mimetype='application/json')

@cross_origin
@application.route('/api/data/<symbol>/<sdate>/<edate>/<interval>')
def api_tickerdata(symbol = None, sdate = None, edate = None, interval = None):
    global Response
    return Response(ep.getDataForTicker(symbol, sdate.replace("-","/"), edate.replace("-","/"), interval), mimetype='application/json')

@application.route('/')
def _root():
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    application.debug = True
    application.run(port=8000,host='0.0.0.0',debug=True)
