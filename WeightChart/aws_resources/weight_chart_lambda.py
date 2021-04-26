# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
# Exception handlers
from exception_handlers.CatchAllExceptionHandler import CatchAllExceptionHandler
# Intent handlers
from request_handlers.CancelOrStopIntentHandler import CancelOrStopIntentHandler
from request_handlers.LaunchRequestHandler import LaunchRequestHandler
from request_handlers.HelloWorldIntentHandler import HelloWorldIntentHandler
from request_handlers.HelpIntentHandler import HelpIntentHandler
from request_handlers.SessionEndedRequestHandler import SessionEndedRequestHandler
from request_handlers.IntentReflectorHandler import IntentReflectorHandler
from request_handlers.AddWeightIntentHandler import AddWeightIntentHandler

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.
sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(AddWeightIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
