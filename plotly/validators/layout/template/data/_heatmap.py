import _plotly_utils.basevalidators


class HeatmapsValidator(_plotly_utils.basevalidators.CompoundArrayValidator):

    def __init__(
        self,
        plotly_name='heatmap',
        parent_name='layout.template.data',
        **kwargs
    ):
        super(HeatmapsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Heatmap'),
            data_docs=kwargs.pop('data_docs', """
"""),
            **kwargs
        )