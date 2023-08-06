from typing import Any
from typing import Text, Union


def get(url: Union[Text, bytes],
        params: Any = ...,
        headers: Any = ...,
        **kwargs, ) -> Any: ...


def post(url: Union[Text, bytes],
         data: Any = ...,
         json=...,
         **kwargs) -> Any: ...


def session_get(url: Union[Text, bytes],
                params: Union[Text, bytes],
                **kwargs, ) -> Any: ...


def session_post(url: Union[Text, bytes],
                 data: Any = ...,
                 json=...,
                 **kwargs) -> Any: ...
