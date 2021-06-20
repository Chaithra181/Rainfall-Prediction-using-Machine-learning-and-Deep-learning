let states = [
{"text":"	ANDAMAN & NICOBAR ISLANDS	", "value":"	AND	"},
{"text":"	ARUNACHAL PRADESH	", "value":"	ARU	"},
{"text":"	ASSAM & MEGHALAYA	", "value":"	ASS	"},
{"text":"	BIHAR	", "value":"	BIH	"},
{"text":"	CHHATTISGARH	", "value":"	CHH	"},
{"text":"	COASTAL ANDHRA PRADESH	", "value":"	COA	"},
{"text":"	COASTAL KARNATAKA	", "value":"	COA	"},
{"text":"	EAST MADHYA PRADESH	", "value":"	EAS	"},
{"text":"	EAST RAJASTHAN	", "value":"	EAS	"},
{"text":"	EAST UTTAR PRADESH	", "value":"	EAS	"},
{"text":"	GANGETIC WEST BENGAL	", "value":"	GAN	"},
{"text":"	GUJARAT REGION	", "value":"	GUJ	"},
{"text":"	HARYANA DELHI & CHANDIGARH	", "value":"	HAR	"},
{"text":"	HIMACHAL PRADESH	", "value":"	HIM	"},
{"text":"	JAMMU & KASHMIR	", "value":"	JAM	"},
{"text":"	JHARKHAND	", "value":"	JHA	"},
{"text":"	KERALA	", "value":"	KER	"},
{"text":"	KONKAN & GOA	", "value":"	KON	"},
{"text":"	LAKSHADWEEP	", "value":"	LAK	"},
{"text":"	MADHYA MAHARASHTRA	", "value":"	MAD	"},
{"text":"	MATATHWADA	", "value":"	MAT	"},
{"text":"	NAGA MANI MIZO TRIPURA	", "value":"	NAG	"},
{"text":"	NORTH INTERIOR KARNATAKA	", "value":"	NOR	"},
{"text":"	ORISSA	", "value":"	ORI	"},
{"text":"	PUNJAB	", "value":"	PUN	"},
{"text":"	RAYALSEEMA	", "value":"	RAY	"},
{"text":"	SAURASHTRA & KUTCH	", "value":"	SAU	"},
{"text":"	SOUTH INTERIOR KARNATAKA	", "value":"	SOU	"},
{"text":"	SUB HIMALAYAN WEST BENGAL & SIKKIM	", "value":"	SUB	"},
{"text":"	TAMIL NADU	", "value":"	TAM	"},
{"text":"	TELANGANA	", "value":"	TEL	"},
{"text":"	UTTARAKHAND	", "value":"	UTT	"},
{"text":"	VIDARBHA	", "value":"	VID	"},
{"text":"	WEST MADHYA PRADESH	", "value":"	WES	"},
{"text":"	WEST RAJASTHAN	", "value":"	WES	"},
{"text":"	WEST UTTAR PRADESH	", "value":"	WES	"}
];

let list = document.getElementsByClassName("list")[0];
for (let i = 0; i < states.length; i++) {
  let option = document.createElement("option");
  let text = document.createTextNode(states[i].text);
  option.appendChild(text);
  list.appendChild(option);
}
