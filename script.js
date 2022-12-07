let run = () => {
    let building = document.getElementById('building').value;
    let room = document.getElementById('room').value;
    let results = F22data.filter(item => item["building"] == building && item["room"] == room);
    let output = document.getElementById('output');
    if(results.length == 0){
        output.innerHTML = '<h1>Could not find any results :(</h1>';
        return false;
    }
    outHtml = `
    <h1>Results For ${building} Room ${room}</h1>
    <table class="outtable">
        <tr>
            <th>Day</th>
            <th>Start</th>
            <th>End</th>
        </tr>`;
    for(const element of results){
        outHtml += `
        <tr>
            <td>${element['day']}</td>    
            <td>${element['start']}</td>    
            <td>${element['end']}</td>    
        </tr>
        `;
    }
    outHtml += '</table>';
    output.innerHTML = outHtml;
    return false;
}