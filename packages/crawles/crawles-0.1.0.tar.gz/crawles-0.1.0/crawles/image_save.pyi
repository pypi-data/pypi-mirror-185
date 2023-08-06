from typing import Text, Union, Iterable, Optional


def image_save(image_url: Union[Text, bytes],
               image_path: Union[Text, bytes],
               astrict: Optional = 100): ...


def images_save(image_iteration: Iterable[Iterable[Text, Text]],
                astrict: Optional = 100): ...
