let month = [
{text:"january","value":"jan"},
{text:"february","value":"feb"},
{text:"march","value":"mar"},
{text:"april","value":"apr"},
{text:"may","value":"may"},
{text:"june","value":"jun"},
{text:"july","value":"jul"},
{text:"august","value":"aug"},
{text:"september","value":"sep"},
{text:"october","value":"oct"},
{text:"november","value":"nov"},
{text:"december","value":"dec"}
];
let list2 = document.getElementsByClassName("list2")[0];
for (let i = 0; i < month.length; i++) {
  let option = document.createElement("option");
  let text = document.createTextNode(month[i].text);
  option.appendChild(text);
  list2.appendChild(option);
}
