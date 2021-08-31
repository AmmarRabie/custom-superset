from html.entities import html5
from flask import Flask, request, jsonify
from werkzeug.utils import redirect
from main import nestedMerge, DEFAULT_FORM_DATA, BASE_URL
import json
from copy import deepcopy

TEST_URL = "https://superset.sigmaproit.com/superset/explore/?form_data=%7B%22viz_type%22%3A%22table%22%2C%22datasource%22%3A%222__table%22%2C%22url_params%22%3A%7B%7D%2C%22time_range_endpoints%22%3A%5B%22inclusive%22%2C%22exclusive%22%5D%2C%22granularity_sqla%22%3A%22CreatedAt%22%2C%22time_grain_sqla%22%3A%22P1D%22%2C%22time_range%22%3A%22No+filter%22%2C%22query_mode%22%3A%22aggregate%22%2C%22groupby%22%3A%5B%22Status%22%5D%2C%22all_columns%22%3A%5B%5D%2C%22percent_metrics%22%3A%5B%5D%2C%22order_by_cols%22%3A%5B%5D%2C%22row_limit%22%3A100%2C%22server_page_length%22%3A10%2C%22order_desc%22%3Atrue%2C%22adhoc_filters%22%3A%5B%5D%2C%22table_timestamp_format%22%3A%22smart_date%22%2C%22show_cell_bars%22%3Atrue%2C%22color_pn%22%3Atrue%2C%22extra_form_data%22%3A%7B%7D%7D"

app = Flask(__name__)

def renderTemplate(url, width="100%", height='800'):
    return f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=100, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>This is the demo page of sigmapro it apache superset</h1>
    <p>We are about to introduce some thing amazing, here is the IFRAME</p>
    <iframe src='{url}' width="{width}" height="{height}"></iframe>
</body>
</html>
    '''

@app.route("/filter/<status>")
def report(status):
    formData = deepcopy(DEFAULT_FORM_DATA)
    formData['adhoc_filters'][0]['comparator'] = status

    isStandalone = request.args.get('standalone', default="1") == '1'
    url = BASE_URL + json.dumps(formData, separators=(',', ":")) + ("&standalone=1" if isStandalone else "")

    return renderTemplate(url)


@app.route("/redirect/<status>")
def reportredirect(status):
    return redirect(TEST_URL)

if __name__ == '__main__':
    app.run("0.0.0.0")