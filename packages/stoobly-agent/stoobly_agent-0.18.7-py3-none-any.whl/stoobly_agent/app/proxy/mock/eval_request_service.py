import json
import pdb

from mitmproxy.http import Request as MitmproxyRequest
from requests import Response
from typing import List, TypedDict, Union
from stoobly_agent.config.constants import custom_headers

from stoobly_agent.lib.api.param_builder import ParamBuilder
from stoobly_agent.app.models.request_model import RequestModel
from stoobly_agent.app.proxy.intercept_settings import InterceptSettings
from stoobly_agent.app.settings import Settings

from .hashed_request_decorator import HashedRequestDecorator
from ..mitmproxy.request_facade import MitmproxyRequestFacade

class EvalRequestOptions(TypedDict):
    infer: bool
    retry: int

def inject_eval_request(
    request_model: RequestModel,
    intercept_settings: InterceptSettings,
):
    settings = Settings.instance()

    if not request_model:
        request_model = RequestModel(settings)

    if not intercept_settings:
        intercept_settings = InterceptSettings(intercept_settings)

    return lambda request, ignored_components, **options: eval_request(
        request_model, intercept_settings, request, ignored_components or [], **options 
    )

###
#
# @param settings [Settings.mode.mock | Settings.mode.record]
#
def eval_request(
    request_model: RequestModel,
    intercept_settings: InterceptSettings,
    request: MitmproxyRequest,
    ignored_components_list: List[Union[list, str, None]],
    **options: EvalRequestOptions
) -> Response:
    query_params = ParamBuilder()
    query_params.with_resource_scoping(intercept_settings)

    ignored_components = __build_ignored_components(ignored_components_list or [])
    query_params.with_params(__build_request_params(request, ignored_components))

    query_params.with_params(__build_optional_params(request, options))

    return request_model.response(**query_params.build())

def __build_ignored_components(ignored_components_list):
    ignored_components = []
    for el in ignored_components_list:
        if isinstance(el, bytes) or isinstance(el, str): 
            try:
                ignored_components += json.loads(el)
            except:
                pass
        elif isinstance(el, list):
            ignored_components += el
        elif isinstance(el, dict):
            ignored_components.append(el)

    return ignored_components

###
#
# Formats request into parameters expected by stoobly request_model
#
# @param request [lib.mitmproxy_request_adapter.MitmproxyRequestFacade]
# @param ignored_components [Array<Hash>]
#
# @return [Hash] query parameters to pass to stoobly request_model
#
def __build_request_params(request: MitmproxyRequest, ignored_components = []) -> dict:
    request = MitmproxyRequestFacade(request)
    hashed_request = HashedRequestDecorator(request).with_ignored_components(ignored_components)

    headers_hash = hashed_request.headers_hash()
    query_params_hash = hashed_request.query_params_hash()
    body_params_hash = hashed_request.body_params_hash()
    body_text_hash = hashed_request.body_text_hash()

    query_params = {}
    query_params['host'] = request.host
    query_params['path'] = request.path
    query_params['port'] = request.port
    query_params['method'] = request.method

    if len(headers_hash) > 0:
        query_params['headers_hash'] = headers_hash

    if len(query_params_hash) > 0:
        query_params['query_params_hash'] = query_params_hash

    # The problem here is that if a body_param_hash is not passed, then body_text_hash is checked
    # However, if body_params are ignored, then there may not be a body_param_hash
    #
    # If there are ignored body_params, this means there are body_params
    # Then we should use body_params_hash over body_text_hash
    if len(body_params_hash) > 0 or len(hashed_request.ignored_body_params) > 0:
        query_params['body_params_hash'] = body_params_hash

    if len(body_text_hash) > 0:
        query_params['body_text_hash'] = body_text_hash

    return query_params

def __build_optional_params(request: MitmproxyRequest, options: EvalRequestOptions):
    optional_params = {}

    if options.get('retry'):
        optional_params['retry'] = options['retry']

        if options.get('infer'):
            optional_params['infer'] = options['infer']

    headers = request.headers
    if custom_headers.MOCK_REQUEST_ID in headers:
        optional_params['request_id'] = headers[custom_headers.MOCK_REQUEST_ID]

    return optional_params