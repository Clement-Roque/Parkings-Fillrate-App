function get_datetime_diff_from_now_in_minutes(datetime){

	let datetime_to_diff = new Date(datetime);
	let now = Date.now();

	return Math.ceil((now-datetime_to_diff)/1000/60);
}


function create_parking_information_updated_datetime(updated_datetime_in_minutes){

	let parking_small_node = document.createElement("small"); 
	parking_small_node.className = "d-flex";
	let update_message = "Updated "+updated_datetime_in_minutes+" minutes ago";
	if (updated_datetime_in_minutes>=60){
		update_message = "Hasn't been updated for a while";
	}
	parking_small_node.appendChild(document.createTextNode(update_message));

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

function create_parking_fill_bar(){

	let parking_progressbar_node = document.createElement("div");
	parking_progressbar_node.setAttribute("aria-valuemax", "100");
	parking_progressbar_node.setAttribute("aria-valuemin", "0");
	parking_progressbar_node.setAttribute("aria-valuenow", "25");
	parking_progressbar_node.setAttribute("style", "width: 25%;");
	parking_progressbar_node.setAttribute("role", "progressbar");
	parking_progressbar_node.className = "progress-bar";
	parking_progressbar_node.appendChild(document.createTextNode("25%"));

	let parking_progress_node = document.createElement("div");
	parking_progress_node.className = "progress col-4 px-0";

	parking_progress_node.appendChild(parking_progressbar_node)

	return parking_progress_node

}

function create_parking_label_and_updated_datetime(parking_label, updated_datetime_in_minutes){

	let parking_div_node = document.createElement("div"); 
	parking_div_node.className = "d-flex justify-content-between";
	parking_div_node.appendChild(document.createTextNode(parking_label));

	let parking_fill_bar = create_parking_fill_bar();
	parking_div_node.appendChild(parking_fill_bar);


	let parking_updated_datetime = create_parking_information_updated_datetime(updated_datetime_in_minutes)
	parking_div_node.appendChild(parking_updated_datetime);

	return parking_div_node;
}

function create_parking_details(parking_label,parking_status,updated_datetime_in_minutes){

	let parking_information_status = create_parking_information_status(parking_status)

	let parking_label_and_updated_datetime = create_parking_label_and_updated_datetime(parking_label,updated_datetime_in_minutes)


	let parking_li_node = document.createElement("li"); 
	parking_li_node.className = "list-group-item";
	parking_li_node.appendChild(parking_label_and_updated_datetime);
	parking_li_node.appendChild(parking_information_status);

	return parking_li_node

}

async function add_parking_information(parking_label){

	const parking_informations = await get_parking_by_label(parking_label);

	const updated_datetime_in_minutes = get_datetime_diff_from_now_in_minutes(parking_informations.DateTime);

	const parking_details = create_parking_details(parking_label,parking_informations.Status,updated_datetime_in_minutes)

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

async function get_parking_informations() {

  const parking_labels = await get_all_parking_labels();

  parking_labels.forEach(parking_label => add_parking_information(parking_label));
 
}

export {get_parking_informations}