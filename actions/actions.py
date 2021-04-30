from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction



class ActionPizzaOrderForm(FormAction):
    
    def name(self) -> Text:
        return "action_pizza_order_form"


    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["pizza_size", "pizza_type", "pizza_amount"]


    def submit(self,
               dispatcher: "CollectingDispatcher",
               tracker: "Tracker",
               domain: "DomainDict",
        ) -> List[Dict]:
        
        pizza_size = tracker.get_slot('pizza_size')
        pizza_type = tracker.get_slot('pizza_type')
        pizza_amount = tracker.get_slot('pizza_amount')
        print(pizza_amount, pizza_size, pizza_type)

        message_to_user = f"ok Great. Your order is {pizza_amount} {pizza_type} pizza in {pizza_size} size. Can you please confirm your order?"

        dispatcher.utter_message(text=message_to_user)
        return []




class ActionWebSiteOrderForm(FormAction):
    
    def name(self) -> Text:
        return "action_web_site_order_form"


    @staticmethod
    def required_slots(tracker: "Tracker") -> List[Text]:
        return ["web_site_type"]


    def submit(self,
               dispatcher: "CollectingDispatcher",
               tracker: "Tracker",
               domain: "DomainDict",
        ) -> List[Dict]:
        
        web_site_type = tracker.get_slot('web_site_type')
        print(web_site_type)

        message_to_user = f"ok Great. Your order is a {web_site_type} web site. Can you please confirm your order?"

        dispatcher.utter_message(text=message_to_user)
        return []