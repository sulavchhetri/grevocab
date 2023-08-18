"""
    This method provides utils function to the fastapi app
"""
import json
import typing
from starlette.responses import Response


class PrettyJSONResponse(Response):
    """
        This class is used to pretiffy the json response
    """
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        """
            This function is used to render the json response with
            appropriate settings
        """
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")
