function get_datetime_diff_from_now_in_minutes(datetime_str){

	let datetime_to_diff = new Date(datetime_str);
	let now = Date.now();

	return Math.ceil((now-datetime_to_diff)/1000/60);
}


function create_parking_last_update(last_update){

	const last_update_minutes = get_datetime_diff_from_now_in_minutes(last_update);

	let parking_last_update = document.createElement("small"); 
	parking_last_update.className = "col text-right";

	let update_message = "Updated "+last_update_minutes+" minutes ago";

	if (last_update_minutes>=60){
		update_message = "Hasn't been updated for an hour";
	}
	parking_last_update.appendChild(document.createTextNode(update_message));

	return parking_last_update;
}

function create_parking_status(parking_status){

	let parking_information_status = document.createElement("span");
	if(parking_status == "Open"){

		parking_information_status.className = "badge badge-success badge-pill";
		parking_information_status.appendChild(document.createTextNode(parking_status));
	}
	else{

		parking_information_status.className = "badge badge-danger badge-pill";
		parking_information_status.appendChild(document.createTextNode("Closed"));
	}

	return parking_information_status;
}

function create_parking_fillrate_bar(free, total){

	const fillrate = Math.floor((free/total)*100);

	let class_attributes = "progress-bar"
	if(fillrate==100){
		class_attributes = class_attributes+" bg-danger"
	}
	else if (fillrate>=75){
		class_attributes = class_attributes+" bg-warning"
	}


	let parking_fillrate = document.createElement("div");
	parking_fillrate.setAttribute("aria-valuemax", "100");
	parking_fillrate.setAttribute("aria-valuemin", "0");
	parking_fillrate.setAttribute("aria-valuenow", fillrate);
	parking_fillrate.setAttribute("style", "width: "+fillrate+"%;");
	parking_fillrate.setAttribute("role", "progressbar");
	parking_fillrate.className = class_attributes;
	parking_fillrate.appendChild(document.createTextNode(fillrate+"%"));

	let parking_fillrate_bar = document.createElement("div");
	parking_fillrate_bar.className = "progress col-4 px-0";

	parking_fillrate_bar.appendChild(parking_fillrate)

	return parking_fillrate_bar;

}

function create_parking_label(parking_label){

	let parking_information_label =  document.createElement("p"); 
	parking_information_label.className = "col";
	parking_information_label.appendChild(document.createTextNode(parking_label));

	return parking_information_label;

}


function create_parking_informations(parking_data){

	let parking_informations = document.createElement("div"); 
	parking_informations.className = "row";

	let parking_information_label =  create_parking_label(parking_data.Label);
	

	let parking_fill_bar = create_parking_fillrate_bar(parking_data.Free, parking_data.Total);
	

	let parking_updated_datetime = create_parking_last_update(parking_data.DateTime)
	

	parking_informations.appendChild(parking_information_label);
	parking_informations.appendChild(parking_fill_bar);
	parking_informations.appendChild(parking_updated_datetime);

	return parking_informations;
}



function create_parking(parking_data){

	let parking = document.createElement("li"); 
	parking.className = "list-group-item";

	let parking_informations = create_parking_informations(parking_data)
	let parking_information_status = create_parking_status(parking_data.Status)

	parking.appendChild(parking_informations);
	parking.appendChild(parking_information_status);

	return parking;

}

async function add_parking_to_parking_list(parking_label){

	let parking_data = await get_parking_data_by_label(parking_label);
	parking_data.Label = parking_label;

	const parking = create_parking(parking_data)

	document.getElementById("parkings").appendChild(parking); 

}

function get_parking_data_by_label(parking_label){

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

  parking_labels.forEach(parking_label => add_parking_to_parking_list(parking_label));
 
}

export {get_parking_informations}