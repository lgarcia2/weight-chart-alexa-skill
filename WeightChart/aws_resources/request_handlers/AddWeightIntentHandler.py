
print("Test Import Add Weight Intent Handler")
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
import ask_sdk_core.utils as ask_utils
print("Imported Add Weight Intent Handler")

class AddWeightIntentHandler(AbstractRequestHandler):
    """Handler for Add Weight Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AddWeightIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print('handling weight')
        intent_name = ask_utils.get_intent_name(handler_input)
        print(f'triggered intent {intent_name}')

        weight_value_slot = ask_utils.get_slot(handler_input, "USER_WEIGHT_VALUE")
        print(f'got weight value slot: {weight_value_slot.name} {weight_value_slot.value} {weight_value_slot.confirmation_status}')
        weight_units_slot = ask_utils.get_slot(handler_input, "USER_WEIGHT_UNITS")
        print(f'got weight units slot: {weight_units_slot.name} {weight_units_slot.value} {weight_units_slot.confirmation_status}')


        speak_output = f"I'm adding the weight {weight_value_slot.value} {weight_units_slot.value}"
        print(speak_output)

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )