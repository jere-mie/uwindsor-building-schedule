function compare(a, b){
    let lookup = {"M":1, "MW":2, "T":3, "TTH":4, "W":5, "TH":6, "F":7};
    if(lookup[a['day']] > lookup[b['day']]){
        return 1;
    }else if(lookup[a['day']] < lookup[b['day']]){
        return -1;
    }
    // equal days, check AM/PM start times
    console.log(a['start'].slice(-2));
    console.log(b['start'].slice(-2));

    if (a['start'].slice(-2) > b['start'].slice(-2)) {
        return 1;
    } else if (a['start'].slice(-2) < b['start'].slice(-2)) {
        return -1;
    }
    // equal AM/PM, check actual start times
    if (a['start'] > b['start']) {
        return 1;
    } else if (a['start'] < b['start']) {
        return -1;
    }
    return 0;
}

let run = () => {
    let building = document.getElementById('building').value;
    let room = document.getElementById('room').value;
    let results = data.filter(item => item["building"] == building && item["room"] == room);
    let output = document.getElementById('output');
    let daylookup = {"M":"Monday", "MW":"Monday/Wednesday", "T":"Tuesday", "TTH":"Tuesday/Thursday", "W":"Wednesday", "TH":"Thursday", "F":"Friday"};

    if(results.length == 0){
        output.innerHTML = '<h1>Could not find any results :(</h1>';
        return false;
    }
    results = results.sort(compare)
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
            <td>${daylookup[element['day']]}</td>    
            <td>${element['start']}</td>    
            <td>${element['end']}</td>    
        </tr>
        `;
    }
    outHtml += '</table>';
    output.innerHTML = outHtml;
    return false;
}