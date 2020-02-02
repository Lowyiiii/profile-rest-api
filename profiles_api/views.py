from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = ['Uses HTTP ,ethods as function (get,post,patch,put,delete)',
                      'Is similar to a tarditional Django View',
                      'Gives you the most control over you application logic',
                      'IS mapped manually to urls'
                      ]
        return Response({'messages':'Hello','an_apiview':an_apiview})