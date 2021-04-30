from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionConfirm(Action):

    def name(self) -> Text:
        return "action_confirm"

    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
        ) -> List[Dict[Text, Any]]:

        service = tracker.get_slots('service')
        p_count = tracker.get_slots('p_count')
        print(service, p_count)

        message_to_user = f"Hi there!! You booked {p_count} {service} tickets. Please confirm your booking."

        dispatcher.utter_message(text=message_to_user)

        return []



