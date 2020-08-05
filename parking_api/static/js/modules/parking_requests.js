function get_parking_by_label(parking_label){
	var parking_node = document.createElement("li"); 
	var parking_text_node = document.createTextNode(parking_label);
	parking_node.appendChild(parking_text_node);  

	document.getElementById("parkings").appendChild(parking_node); 

}

function get_all_parkings(parking_labels){


	parking_labels.forEach(parking_label => get_parking_by_label(parking_label));
}


function get_all_parking_labels(){
	let request = new Request("http:\/\/127.0.0.1:5000/parkings/labels");

	fetch(request)
	  .then(response => {
	    if (response.status === 200) {
	      return response;
	    } else {
	      throw new Error('Something went wrong on api server!');
	    }
	  })
	  .then(response => {
	    console.debug(response);
	    // ...
	  }).catch(error => {
	    console.error(error);
	  });
}
