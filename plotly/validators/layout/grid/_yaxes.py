import _plotly_utils.basevalidators


class YaxesValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='yaxes', parent_name='layout.grid', **kwargs
    ):
        super(YaxesValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            free_length=True,
            items={
                'valType': 'enumerated',
                'values': ['/^y([2-9]|[1-9][0-9]+)?$/', ''],
                'editType': 'plot'
            },
            role='info',
            **kwargs
        )
