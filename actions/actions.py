from cgitb import text
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher



class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_intent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #SlotSet('inw_roucon_trigger_intent_name', tracker.latest_message["intent"]["name"])
        intent =  tracker.latest_message['intent'].get('name')
        last_intent = tracker.latest_message["intent"]["name"]
       # dispatcher.utter_message(last_intent)
        if intent=="Job_seeker":
            message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        # "title": "Carousel 1",
                        # "subtitle": "$10",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqhmyBRCngkU_OKSL6gBQxCSH-cufgmZwb2w&usqp=CAU",
                        "buttons": [ 
                            {
                            "title": "IT",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=it",
                            "type": "web_url"
                              },
                            {
                           "title": "Sales &amp; Marketing",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=sales-marketing",
                            "type": "web_url"
                            },
                            
                          
                            {
                           "title": "Others",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=others",
                            "type": "web_url"
                            },
                            {
                           "title": "Health Care",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=health-care",
                            "type": "web_url"
                            },
                            {
                           "title": "Government",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=government",
                            "type": "web_url"
                            },
                            {
                           "title": "Education Training",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=education-training",
                            "type": "web_url"
                            },
                            {
                           "title": "Shop Jobs",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=shop-jobs",
                            "type": "web_url"
                            },
                            {
                           "title": "Banking",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=banking",
                            "type": "web_url"
                            },
                            {
                           "title": "Automotive Jobs",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=automotive-jobs",
                            "type": "web_url"
                            },
                            {
                           "title": "Telecommunication",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=telecommunication",
                            "type": "web_url"
                            },
                            {
                           "title": "Accounting / Finance",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=accounting-finance",
                            "type": "web_url"
                            },
                            {
                           "title": "Hotel Jobs",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=hotel-jobs",
                            "type": "web_url"
                            },
                            {
                           "title": "Modeling/ Casting",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=modeling-casting",
                            "type": "web_url"
                            },
                             {
                           "title": "Construction/ Facilities",
                            "url": "https://jobayi.com/jobs-listing/?sector_cat=construction-facilities",
                            "type": "web_url"
                            }
                            
                        ]
                    }
                    
                ]
                }
        }
               
           
         
            
            dispatcher.utter_message(attachment=message)
         


        else:
            dispatcher.utter_message(text="hi")
        return [ ]
