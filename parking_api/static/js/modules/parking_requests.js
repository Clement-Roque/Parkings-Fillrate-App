function create_parking_information_updated_time(updated_time_in_seconds){

	const updated_time_in_minutes = updated_time_in_seconds/60;

	let parking_small_node = document.createElement("small"); 
	parking_small_node.className = "d-flex";
	parking_small_node.appendChild(document.createTextNode("Updated "+updated_time_in_minutes+" minutes ago"));

	return parking_small_node;
}

function create_parking_information_status(parking_status){

	let parking_span_node = document.createElement("span");
	if(parking_status == "Open"){

		parking_span_node.className = "badge badge-success badge-pill";
		parking_span_node.appendChild(document.createTextNode(parking_status));
	}
	else{

		parking_span_node.className = "badge badge-danger badge-pill";
		parking_span_node.appendChild(document.createTextNode("Closed"));
	}

	return parking_span_node;
}

function create_parking_label_and_updated_time(parking_label){

	let parking_div_node = document.createElement("div"); 
	parking_div_node.className = "d-flex justify-content-between";
	parking_div_node.appendChild(document.createTextNode(parking_label));

	let parking_updated_time = create_parking_information_updated_time(120)
	parking_div_node.appendChild(parking_updated_time);

	return parking_div_node;
}

function create_parking_details(parking_label,parking_status,updated_time_in_seconds){

	let parking_information_status = create_parking_information_status(parking_status)

	let parking_label_and_updated_time = create_parking_label_and_updated_time(parking_label,120)

	let parking_li_node = document.createElement("li"); 
	parking_li_node.className = "list-group-item";
	parking_li_node.appendChild(parking_label_and_updated_time);
	parking_li_node.appendChild(parking_information_status);

	return parking_li_node

}

async function add_parking_information(parking_label){

	const parking_informations = await get_parking_by_label(parking_label);

	const parking_details = create_parking_details(parking_label,parking_informations.Status,120)

	document.getElementById("parkings").appendChild(parking_details); 

}

function get_parking_by_label(parking_label){

	return new Promise((resolve, reject) => {
	    var parking_requests = new XMLHttpRequest();
	    parking_requests.responseType = "json"
	    parking_requests.open('GET', "http:\/\/127.0.0.1:5000/parking/"+parking_label);

	    parking_requests.onload = function() {
	      if (parking_requests.status == 200) {
	        resolve(parking_requests.response);
	      }
	      else {
	        reject(Error(parking_requests.statusText));
	      }
	    };

	    parking_requests.send();
	});
}


function get_all_parking_labels(){
	
	return new Promise((resolve, reject) => {
	    var parking_labels_requests = new XMLHttpRequest();
	    parking_labels_requests.responseType = "json"
	    parking_labels_requests.open('GET', "http:\/\/127.0.0.1:5000/parkings");

	    parking_labels_requests.onload = function() {
	      if (parking_labels_requests.status == 200) {
	        resolve(parking_labels_requests.response);
	      }
	      else {
	        reject(Error(parking_labels_requests.statusText));
	      }
	    };

	    parking_labels_requests.send();
	});
}

async function asyncCall() {

  const parking_labels = await get_all_parking_labels();

  parking_labels.forEach(parking_label => add_parking_information(parking_label));
 
}

export {asyncCall}