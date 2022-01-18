window.onload = function() {
    let locateOrigin = window.location.origin;
//// task 1
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

//// task 2
        let url= locateOrigin + '/task2selector'
        sendRequest(url,'GET', function(){
            console.log(this.response);
            for(i=0;i<this.response.length;i++){
                $('#task2selector').append($('<option>', {
                    value: this.response[i][0],
                    text: `${this.response[i][1]}(${this.response[i][2]})`
                }));
            }
        })  
        $('#task2').click(function(){
            let url= locateOrigin + '/task2' + '?' + 'region_id='+ $('#task2selector').val() + '&name=' + $('#task2name').val() + '&height=' + $('#task2height').val()
            sendRequest(url,'GET', function(){
                if(this.responce="ok"){
                    showSwal('auto-close');
                    setTimeout(function() {
                        window.location.reload()
                  }, 3000);
                  
                }else{
                    showSwal('');
                }
            })

        })
  //// task 3 
  $(".button-edit").on('click', function(event){
        console.log(this.response);
    url = locateOrigin + '/searchmtn' + "?id=" + event.target.dataset.mtn
    sendRequest(url,'GET', function(){
        let url= locateOrigin + '/task2selector'
        sendRequest(url,'GET', function(){
            console.log(this.response);
            for(i=0;i<this.response.length;i++){
                $('#task3selector').append($('<option>', {
                    value: this.response[i][0],
                    text: `${this.response[i][1]}(${this.response[i][2]})`
                }));
            }
        })
        $('#task3selector').val(this.response[3])
        $('#task3name').val(this.response[1])
        $('#task3height').val(this.response[2])
        document.querySelector('#send-edit').dataset.mtn=this.response[0]
    });
    $('#send-edit').on('click', function(event){
        let url= locateOrigin + '/task3' + '?' + 'region_id='+ $('#task3selector').val() + '&name=' + $('#task3name').val() + '&height=' + $('#task3height').val() + '&id=' + event.target.dataset.mtn;
        sendRequest(url,'GET', function(){
            if(this.responce==="ok"){
                showSwal('edited');
            }else{
                showSwal('');
            }
        })
    })
});
//// task 4
$('#task4').click(function(){
    let url= locateOrigin + '/task4' + '?' +'start=' + $('#task41').val() + '&end=' + $('#task42').val() 
    sendRequest(url,'GET', function(){
        console.log(this.response);
        document.getElementById('task4table').innerHTML='';
        var table = $('<table>').addClass('table');
        var thead = $('<thead>').addClass('thead-dark');
        var row = `<tr><th scope="col">`+ 'First name' +`</th><th scope="col">`+ 'Last name' +`</th></tr>`
        thead.append(row);
        table.append(thead);
        var tbody = $('<tbody>');
        for(i=0; i<this.response.length; i++){
            var row =  `<tr><td>${this.response[i][0]}</td><td>${this.response[i][1]}</td></tr>`
            console.log(row)
            tbody.append(row);
        }
        table.append(tbody);
        $('#task4table').append(table);
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

(function($) {
    showSwal = function(type) {
    'use strict';
    if (type === 'auto-close') {
    swal({
    title: 'Добавлено!',
    text: 'Это сообщение закроется через 2 секунды.',
    timer: 2000,
    button: false
    })
    }else if (type==='edited'){
        swal({
            title: 'Отредактировано!',
            text: 'Это сообщение закроется через 2 секунды.',
            timer: 2000,
            button: false
            })
    }else{
    swal("Произошла ошибка!");
    }
    }
    
    })(jQuery);