addUnit = function(side) {
	let nation = getNation(side);
	let allUnitsWrapper = document.getElementById(`${side}_army`);
    let newId = allUnitsWrapper.childNodes.length;
	let newFieldName = `${side}_army-${newId}`;
	let unitOptions = getUnitListOptions(nation);
	allUnitsWrapper.insertAdjacentHTML('beforeend',
        `<li><label for="${newFieldName}">${side == "attacker" ? "Attacking" : "Defending"} Unit</label> <select id="${newFieldName}" name="${newFieldName}">${unitOptions}</select></li>`
	);
}

getNation = function(side) {
	let wrapper = document.getElementById(side);
	return wrapper.options[wrapper.selectedIndex].value
}

// I'll split this up better into what nations can truly use some of these, but for now, these are base
const BASE_UNITS = [
	'Militia', 'Infantry', 'Airbourne Infantry', 'Marine', 'Mountain Infantry',
    'Cavalry', 'Motorized Infantry', 'Mechanized Infantry', 'Tank Destroyer', 'Light Tank', 'Medium Tank',
    'Artilery', 'Self-Propelled Artillery', 'Anti-Aircraft Artillery',
    'Fighter', 'Tactical Bomber', 'Medium Bomber', 'Strategic Bomber', 'Seaplane', 'Air Transport',
    'Torpedo Boat Destroyer', 'Destroyer', 'Coastal Defense Ship', 'Light Cruiser', 'Heavy Cruiser',
    'Battlecruiser', 'Battleship', 'Light Carrier', 'Fleet Carrier', 'Coastal Submarine', 'Submarine',
    'Naval Transport'
];

getUnitListOptions = function(nation) {
	units = BASE_UNITS

    // Add the advanced units from technology that only major powers could have
    if (['USA', 'Great Britain', 'FEC', 'ANZAC', 'France', 'Germany', 'Japan', 'Italy', 'KMT Major Power', 'Russia', 'CCP'].includes(nation)) {
        units.push(...['Elite Airborne Infantry', 'Advanced Mechanized Infantry', 'Heavy Tank', 'Advanced Artillery',
            'Advanced Self-propelled Artillery', 'Jet Fighter', 'Heavy Strategic Bomber', 'Heavy Air Transport',
            'Heavy Battleship', 'Heavy Fleet Carrier', 'Advanced Submarine', 'Attack Transport']);
    }

    if (nation === 'Germany') {
        units.push(...['Panzer-grenadier', 'Tiger I']);
    }

    if (nation === 'Russia') {
        units.push(...['T-34', 'Katyusha']);
    }

    if (['FEC', 'ANZAC', 'France', 'Great Britain', 'Italy'].includes(nation)) {
        units.push('Colonial Infantry');
    }

    if (['France', 'Vichy Frnace'].includes(nation)) {
        units.push('Foreign Legion');
    }

    if (nation === 'FEC') {
        units.push('Gurkha');
    }

    if (nation === 'KMT') {
        units = ['Cavalry', 'Militia', 'Infantry']
    }

	output = '';
	for(let i = 0; i < units.length; i++) {
		output += `<option value="${units[i]}">${units[i]}</option>`
	}
	return output;
}

