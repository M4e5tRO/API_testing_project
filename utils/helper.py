import allure
import json
from allure_commons.types import AttachmentType


class Helper:


    def attach_payload(self, payload):
        """
        Attach a payload to the Allure report in JSON format.

        :param payload: dict or object
            The payload to be attached. It should be a serializable object (e.g., dict).
        :return: None
            This method does not return a value.
        """
        payload = json.dumps(payload, indent=4)
        allure.attach(body=payload, name="API Payload", attachment_type=AttachmentType.JSON)


    def attach_response(self, response):
        """
        Attach an API response to the Allure report in JSON format.

        :param response: dict or object
            The API response to be attached. It should be a serializable object (e.g., dict).
        :return: None
            This method does not return a value.
        """
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)


    def attach_html(self, html_content):
        """
        Attach HTML content to the Allure report.

        :param html_content: str
            The HTML content to be attached.
        :return: None
            This method does not return a value.
        """
        allure.attach(html_content, name='HTML page', attachment_type=allure.attachment_type.TEXT)


    def is_subset(self, subset, superset):
        """
        Recursively checks if `subset` is a subset of `superset`.

        :param subset: dict, list, or another value
            The subset to check.
        :param superset: dict, list, or another value
            The "superset" where we search for the data.
        :return: True if `subset` is part of `superset`, otherwise False.
        """
        if isinstance(subset, dict):
            return all(
                key in superset and self.is_subset(value, superset[key])
                for key, value in subset.items()
            )
        elif isinstance(subset, list):
            return all(item in superset for item in subset)
        else:
            return subset == superset
