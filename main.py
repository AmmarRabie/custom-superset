

from tkinter.constants import NONE
from typing import Iterable
from copy import deepcopy
BASE_URL = "https://superset.sigmaproit.com/superset/explore/?form_data="

# DEFAULT_FORM_DATA = {
#     "viz_type": "table",
#     "datasource": "2__table",
#     "slice_id": 1,
#     "url_params": {},
#     "time_range_endpoints": [
#         "inclusive",
#         "exclusive"
#     ],
#     "granularity_sqla": "CreatedAt",
#     "time_grain_sqla": "P1W",
#     "time_range": "No+filter",
#     "query_mode": "aggregate",
#     "groupby": [
#         "CreatedAt"
#     ],
#     "metrics": [
#         {
#             "aggregate": "SUM",
#             "column": {
#                 "column_name": "GrandPrice",
#                 "description": None,
#                 "expression": None,
#                 "filterable": True,
#                 "groupby": True,
#                 # "id": 65,
#                 "is_dttm": False,
#                 "python_date_format": None,
#                 "type": "DOUBLE+PRECISION",
#                 "type_generic": 0,
#                 "verbose_name": None
#             },
#             "expressionType": "SIMPLE",
#             "hasCustomLabel": False,
#             "isNew": False,
#             "label": "SUM(GrandPrice)",
#             "optionName": "metric_mo8fyt7psn_p8p4qe6fcog",
#             "sqlExpression": None
#         }
#     ],
#     "all_columns": [],
#     "percent_metrics": [
#         {
#             "aggregate": "SUM",
#             "column": {
#                 "column_name": "GrandPrice",
#                 "description": None,
#                 "expression": None,
#                 "filterable": True,
#                 "groupby": True,
#                 "id": 65,
#                 "is_dttm": False,
#                 "python_date_format": None,
#                 "type": "DOUBLE+PRECISION",
#                 "type_generic": 0,
#                 "verbose_name": None
#             },
#             "expressionType": "SIMPLE",
#             "hasCustomLabel": False,
#             "isNew": False,
#             "label": "SUM(GrandPrice)",
#             "optionName": "metric_xj0o4ozjzql_f94di6n5abe",
#             "sqlExpression": None
#         }
#     ],
#     "timeseries_limit_metric": {
#         "aggregate": "MAX",
#         "column": {
#             "column_name": "CreatedAt",
#             "description": None,
#             "expression": None,
#             "filterable": True,
#             "groupby": True,
#             "id": 60,
#             "is_dttm": True,
#             "python_date_format": None,
#             "type": "TIMESTAMP+WITH+TIME+ZONE",
#             "type_generic": 2,
#             "verbose_name": None
#         },
#         "expressionType": "SIMPLE",
#         "hasCustomLabel": False,
#         "isNew": False,
#         "label": "MAX(CreatedAt)",
#         "optionName": "metric_5b6oe4j3gh_ryge9yhtsc",
#         "sqlExpression": None
#     },
#     "order_by_cols": [],
#     "row_limit": 10000,
#     "server_page_length": 10,
#     "order_desc": True,
#     "adhoc_filters": [
#         {
#             "clause": "WHERE",
#             "comparator": "pending",
#             "expressionType": "SIMPLE",
#             "filterOptionName": "filter_bb9rky0uz1_n7fifkdfgq",
#             "isExtra": False,
#             "isNew": False,
#             "operator": "==",
#             "operatorId": "NOT_EQUALS",
#             "sqlExpression": None,
#             "subject": "Status"
#         }
#     ],
#     "table_timestamp_format": "smart_date",
#     "show_cell_bars": True,
#     "color_pn": True,
#     "extra_form_data": {}
# }
DEFAULT_FORM_DATA = {
    "viz_type": "table",
    "datasource": "2__table",
    "url_params": {},
    "time_range_endpoints": ["inclusive", "exclusive"],
    "granularity_sqla": "CreatedAt",
    "time_grain_sqla": "P1D",
    "time_range": "No filter",
    "query_mode": "aggregate",
    "groupby": ["Merchant_Name", "Status"],
    "all_columns": [],
    "percent_metrics": [],
    "order_by_cols": [],
    "row_limit": 10,
    "server_page_length": 10,
    "order_desc": True,
    "adhoc_filters": [
        {
            "expressionType": "SIMPLE",
            "subject": "Status",
            "operator": "==",
            "operatorId": "NOT_EQUALS",
            "comparator": "pending",
            "clause": "WHERE",
            "sqlExpression": None,
            "isExtra": False,
            "isNew": False,
            "filterOptionName": "filter_yvcybgymx0d_c6s7xwdpmm"
        },
    ],
    "table_timestamp_format": "smart_date",
    "show_cell_bars": True,
    "color_pn": True,
    "extra_form_data": {}
}


VALUE_TO_VALUE_ITERABLE_UPDATE = ["metrics", b"adhoc_filters", "percent_metrics"]


def nestedMerge(original, updates):
    originalCloned = deepcopy(original)
    if(type(updates) in [str, int, float]):
        return updates
    for key, value in updates.items():
        if(originalCloned.get(key) == None):
            # if there is a new key just append it
            originalCloned[key] = value
            continue
        # key exists
        if(type(originalCloned[key]) is dict):
            voriginal, vupdate = original[key], updates[key]
            originalCloned[key] = nestedMerge(voriginal, vupdate)
        elif(type(originalCloned[key]) in [list, slice] and key in VALUE_TO_VALUE_ITERABLE_UPDATE):
            originalCloned[key].clear()
            for voriginal, vupdate in zip(original[key], updates[key]):
                originalCloned[key].append(nestedMerge(voriginal, vupdate))
        else:
            # any other types will be replaced without nesting
            originalCloned[key] = updates[key]
    return originalCloned


newFormData = nestedMerge(DEFAULT_FORM_DATA, {
    "not existing": "added successfully",
    "groupby": ["ammar", "mohammed"],
    "metrics": [
        {
            "column": {
                "description": "A new description"
            }
        }
    ]
})

print(newFormData)


d = {
    'viz_type': 'table',
    'datasource': '2__table',
    'slice_id': 1,
    'url_params': {},
    'time_range_endpoints': ['inclusive', 'exclusive'],
    'granularity_sqla': 'CreatedAt',
    'time_grain_sqla': 'P1W',
    'time_range': 'No+filter',
    'query_mode': 'aggregate',
    'groupby': ['ammar', 'mohammed'],
    'metrics': [{'column': {'description': 'A new description'}}],
    'all_columns': [],
    'percent_metrics': [{'aggregate': 'SUM',
                         'column': {'column_name': 'GrandPrice',
                                    'description': None,
                                    'expression': None,
                                    'filterable': True,
                                    'groupby': True,
                                    'id': 65,
                                    'is_dttm': False,
                                    'python_date_format': None,
                                    'type': 'DOUBLE+PRECISION',
                                    'type_generic': 0,
                                    'verbose_name': None},
                         'expressionType': 'SIMPLE',
                         'hasCustomLabel': False,
                         'isNew': False,
                         'label': 'SUM(GrandPrice)',
                         'optionName': 'metric_xj0o4ozjzql_f94di6n5abe',
                         'sqlExpression': None}],
    'timeseries_limit_metric': {'aggregate': 'MAX',
                                'column': {
                                    'column_name': 'CreatedAt',
                                    'description': None,
                                    'expression': None,
                                    'filterable': True,
                                    'groupby': True,
                                    'id': 60,
                                    'is_dttm': True,
                                    'python_date_format': None,
                                    'type': 'TIMESTAMP+WITH+TIME+ZONE',
                                    'type_generic': 2,
                                    'verbose_name': None},
                                'expressionType': 'SIMPLE',
                                'hasCustomLabel': False,
                                'isNew': False,
                                'label': 'MAX(CreatedAt)',
                                'optionName': 'metric_5b6oe4j3gh_ryge9yhtsc',
                                'sqlExpression': None},
    'order_by_cols': [],
    'row_limit': 10000,
    'server_page_length': 10,
    'order_desc': True,
    'adhoc_filters': [{'clause': 'WHERE',
                       'comparator': 'pending',
                       'expressionType': 'SIMPLE',
                       'filterOptionName': 'filter_bb9rky0uz1_n7fifkdfgq', 'isExtra': False, 'isNew': False, 'operator': '!=', 'operatorId': 'NOT_EQUALS', 'sqlExpression': None, 'subject': 'Status'}], 'table_timestamp_format': 'smart_date', 'show_cell_bars': True, 'color_pn': True, 'extra_form_data': {}, 'not existing': 'added successfully'}




# TODO: try to edit
# - Time range --> time_range
# - Time Granuality --> granularity_sqla
# - adhoc filter --> adhoc_filters
# - groupby --> groupby
# - viz type that matches the same properties --> viz_type
# - change the metric or add one more --> metrics
# - change the datasource, and also change corresponding columns --> datasource



# in the showcase demo we may need an access to superset database using the API
# For example to get the dataset id from its name
