from typing import Text, Union, Dict


class Response:
    @property
    def status(self): pass

    @property
    def headers(self): pass

    @property
    def content(self): pass

    @property
    def json(self): pass

    @property
    def text(self): pass


def get(url: Text,
        params=Union[Dict, Text],
        headers=Union[Dict, Text],
        **kwargs) -> Response: ...


def post(url: Text,
         data=Union[Dict, Text],
         headers=Union[Dict, Text],
         **kwargs) -> Response: ...


def session_get(url: Text,
                params=Union[Dict, Text],
                headers=Union[Dict, Text],
                **kwargs) -> Response: ...


def session_post(url: Text,
                 data=Union[Dict, Text],
                 headers=Union[Dict, Text],
                 **kwargs) -> Response: ...
