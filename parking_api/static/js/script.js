import {get_parking_by_label} from "./modules/parking_requests.js"

{% for parking_label in parking_labels %}
    		get_parking_by_label({{parking_label}}) ;
{% endfor %}

