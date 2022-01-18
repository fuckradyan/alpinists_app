window.onload = function() {
    let locateOrigin = window.location.origin;

    $('#task1').click(function(){
        let url= locateOrigin + '/task1'
        sendRequest(url,'GET', function(){
            console.log(this.response);
            document.getElementById('task1table').innerHTML='';

            var table = $('<table>').addClass('table');
            var thead = $('<thead>').addClass('thead-dark');

            var row = `<tr><th scope="col">`+ 'Mountain' +`</th><th scope="col">`+'Group' +`</th><th scope="col">`+'Start' +`</th><th scope="col">`+'End' +`</th></tr>`
            thead.append(row);
            table.append(thead);
            var tbody = $('<tbody>');
            for(i=0; i<this.response.length; i++){
                var row =  `<tr><th scope="row">${this.response[i][0]}</th><td>${this.response[i][1]}</td><td>${this.response[i][2]}</td><td>${this.response[i][3]}</td></tr>`
                console.log(row)
                tbody.append(row);
            }
            table.append(tbody);
            $('#task1table').append(table);
        })  
    })
    
}


function sendRequest(url, method, onloadHandler, params){
    let xhr = new XMLHttpRequest();
    xhr.open(method, url);
    xhr.responseType = 'json';
    xhr.onload = onloadHandler;
    xhr.send(params);

}