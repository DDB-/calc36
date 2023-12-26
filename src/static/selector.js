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

const BASE_UNITS = [
	'Militia', 'Infantry', 'Airbourne Infantry', 'Elite Airbourne Infantry', 'Marine', 'Mountain Infantry'
];

getUnitListOptions = function(nation) {
	units = BASE_UNITS

	output = '';
	for(let i = 0; i < units.length; i++) {
		output += `<option value="${units[i]}">${units[i]}</option>`
	}
	return output;
}

