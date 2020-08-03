var parkings_labels = [
    'Antigone',
    'Comédie',
    'Corum',
    'Europa',
    'Foch',
    'Gambetta',
    'Gare',
    'du Triangle',
    'Arc de Triomphe',
    'Pitot',
    'Circe',
    'Sabines',
    'Garcia Lorca',
    'Sablassou',
    'Mosson',
    'Saint Jean Le Sec',
    'Euromédecine',
    'Occitanie',
    'Vicarello',
    'Gaumont EST',
    'Gaumont OUEST',
    'Charles de Gaulle',
]

function get_parking_by_label(parking_label){
	var parking_node = document.createElement("li"); 
	var parking_text_node = document.createTextNode(parking_label);
	parking_node.appendChild(parking_text_node);  

	document.getElementById("parkings").appendChild(parking_node); 

}

function get_all_parkings_labels(parkings_labels){
	parkings_labels.forEach(parking_label => get_parking_by_label(parking_label));
}

get_all_parkings_labels(parkings_labels);

