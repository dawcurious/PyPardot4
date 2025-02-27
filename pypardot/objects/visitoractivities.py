class VisitorActivities(object):
    """
    A class to query and use Pardot visitor activities.
    Visitor Activity field reference: http://developer.pardot.com/kb/object-field-references
    """

    def __init__(self, client):
        self.client = client

    def query(self, **kwargs):
        """
        Returns the visitor activities matching the specified criteria parameters.
        Supported search criteria: http://developer.pardot.com/kb/api-version-4/visitor-activities/#supported-search-criteria
        """
        response = self._get(path='/do/query?format=json', params=kwargs)

        # Ensure result['visitor_activity'] is a list, no matter what.
        result = response.get('result')
        if 'output' not in kwargs.keys() and 'bulk' not in kwargs.values():
            if result['total_results'] == 0:
                result['visitor_activity'] = []
            elif result['total_results'] == 1:
                result['visitor_activity'] = [result['visitor_activity']]

        return result

    def read(self, id=None, **kwargs):
        """
        Returns the data for the visitor activity specified by <id>. <id> is the Pardot ID for the target visitor activity.
        """
        response = self._post(path='/do/read/id/{id}'.format(id=id), params=kwargs)
        return response

    def _get(self, object_name='visitorActivity', path=None, params=None):
        """GET requests for the Visitor Activity object."""
        if params is None:
            params = {}
        response = self.client.get(object_name=object_name, path=path, params=params)
        return response

    def _post(self, object_name='visitorActivity', path=None, params=None):
        """POST requests for the Visitor Activity object."""
        if params is None:
            params = {}
        response = self.client.post(object_name=object_name, path=path, params=params)
        return response
