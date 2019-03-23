import _plotly_utils.basevalidators


class NameValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='name', parent_name='layout.image', **kwargs
    ):
        super(NameValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'none'),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )