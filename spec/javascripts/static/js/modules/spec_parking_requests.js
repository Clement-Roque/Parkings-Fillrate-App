describe('Testing the request functions ', function() {

    it('Should retrieve the parking labels list', async function() {
        let parking_labels = [
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
        ];

    let requested_parking_labels = await get_all_parking_labels();
    console.log(requested_parking_labels)

    expect(requested_parking_labels.length).toBe(parking_labels.length);
    expect(requested_parking_labels).toEqual(parking_labels);

  })

})