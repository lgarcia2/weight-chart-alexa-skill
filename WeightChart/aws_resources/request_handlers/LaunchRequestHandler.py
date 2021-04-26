
print("Test Import Launch Request Handler")
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
import ask_sdk_core.utils as ask_utils
print("Imported Launch Request Handler")

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = "Welcome, you can say Hello or Help. Which would you like to try?"
        speak_output = "Welcome, to weight chart. I can help you view your weight over time. You can say 'I weigh x pounds' or 'show my weight'. Which would you like to try?"
        #speak_output = "hello there, lil pidge"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
