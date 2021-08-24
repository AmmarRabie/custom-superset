from inspect import formatannotationrelativeto
from os import stat_result
from appJar import gui
from urllib.parse import urlencode
import json
from appJar.lib.png import group
from main import DEFAULT_FORM_DATA, nestedMerge, BASE_URL
import pyperclip

app = gui()
app.setTitle("superset form builder")

def generateUrl(key):
    datasource = app.getEntry("datasource")

    metricCol = app.getEntry("Metric Column")
    metricLabel = app.getEntry("Metric Label")

    filterClause = app.getOptionBox("Addhoc filter -- clause")
    filterOperator = app.getEntry("Addhoc filter -- operator")
    filterSubject = app.getEntry("Addhoc filter -- subject")
    filterComparator = app.getEntry("Addhoc filter -- comparator")

    timeGranuality = app.getOptionBox("time granuality")
    timeRange = app.getEntry("Time range")

    groupBy = app.getEntry("groupby")
    limit = app.getEntry("limit")
    isStandalone = app.getCheckBox("standalone")

    formData = nestedMerge(DEFAULT_FORM_DATA, {
        "datasource": datasource,
        "metrics": [
            {
                "aggregate": "SUM",
                "column": {
                    "column_name": metricCol,
                },
                "expressionType": "SIMPLE",
                "label": metricLabel
            }
        ],
        # "adhoc_filters": {
        #     "clause": filterClause,
        #     "comparator": filterComparator,
        #     "expressionType": "SIMPLE",
        #     "operatorId": filterOperator,
        #     "subject": filterSubject
        # },
        "time_grain_sqla": timeGranuality,
        "time_range": timeRange,
        "row_limit": limit,
        "groupby": groupBy,
    })

    formData = nestedMerge(DEFAULT_FORM_DATA, formData)
    with open("last_form_data_program.json", 'w') as f:
        f.write(json.dumps(formData))
    formData = BASE_URL + json.dumps(formData, separators=(',', ":")) + ("&standalone=1" if isStandalone else "")
    pyperclip.copy(formData)


app.addLabelEntry("datasource",)
app.setEntry("datasource", "2__table")

app.addLabelEntry("Metric Column")
app.setEntry("Metric Column", "GrandPrice")

app.addLabelEntry("Metric Label")
app.setEntry("Metric Label", "Sum(GrandPrice)")

app.addLabelOptionBox("Addhoc filter -- clause", ['WHERE', 'HAVING'])

app.addLabelEntry("Addhoc filter -- operator")
app.setEntry("Addhoc filter -- operator", "NOT_EQUALS")

app.addLabelEntry("Addhoc filter -- subject")
app.setEntry("Addhoc filter -- subject", "Status")

app.addLabelEntry("Addhoc filter -- comparator")
app.setEntry("Addhoc filter -- comparator", "pending")

app.addLabelOptionBox("time granuality", ['PT1S', 'PT1M', 'PT1H', 'P1D', 'P1W', 'P1M', 'P0.25Y', 'P1Y'])
app.setOptionBox("time granuality", "P1D")

app.addLabelEntry("Time range")
app.setEntry("Time range", "No+filter")

app.addLabelEntry("groupby")
app.setEntry("groupby", "CreatedAt")

app.addLabelEntry("limit")
app.setEntry("limit", 15)

app.addCheckBox("standalone")
app.setCheckBox("standalone", True)

app.addButton("Copy url", generateUrl)



app.go()
