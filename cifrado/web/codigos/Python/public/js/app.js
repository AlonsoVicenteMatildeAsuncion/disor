$(document).ready(function() {

  $("#text").keyup(function(e) {
    $.ajax({
               data:  {
                 "text" : $("textarea[name='text']").val(),
                 "displacement" : $("input[name='displacement']").val(),
                 "groups" : $("input[name='groups']").val()
               }, //datos que se envian a traves de ajax
               url:   '/generator', //archivo que recibe la peticion
               type:  'post', //método de envio
               dataType: "json",
               success:  function (response) { //una vez que el archivo recibe el request lo procesa y lo devuelve
                    console.log(response[0]);
                    $("#encryption-text").html(response[0]);
                    $("#invert-text").html(response[1]);
                    $("#groups-text").html(response[2]);
               }
       });
    e.preventDefault();
  });

  $("#displacement").click(function(e) {
    $.ajax({
               data:  {
                 "text" : $("textarea[name='text']").val(),
                 "displacement" : $("input[name='displacement']").val(),
                 "groups" : $("input[name='groups']").val()
               }, //datos que se envian a traves de ajax
               url:   '/generator', //archivo que recibe la peticion
               type:  'post', //método de envio
               dataType: "json",
               success:  function (response) { //una vez que el archivo recibe el request lo procesa y lo devuelve
                    console.log(response[0]);
                    $("#encryption-text").html(response[0]);
                    $("#invert-text").html(response[1]);
                    $("#groups-text").html(response[2]);
               }
       });
    e.preventDefault();
  });

  $("#displacement").keyup(function(e) {
    $.ajax({
               data:  {
                 "text" : $("textarea[name='text']").val(),
                 "displacement" : $("input[name='displacement']").val(),
                 "groups" : $("input[name='groups']").val()
               }, //datos que se envian a traves de ajax
               url:   '/generator', //archivo que recibe la peticion
               type:  'post', //método de envio
               dataType: "json",
               success:  function (response) { //una vez que el archivo recibe el request lo procesa y lo devuelve
                    console.log(response[0]);
                    $("#encryption-text").html(response[0]);
                    $("#invert-text").html(response[1]);
                    $("#groups-text").html(response[2]);
               }
       });
    e.preventDefault();
  });

  $("#groups").click(function(e) {
    $.ajax({
               data:  {
                 "text" : $("textarea[name='text']").val(),
                 "displacement" : $("input[name='displacement']").val(),
                 "groups" : $("input[name='groups']").val()
               }, //datos que se envian a traves de ajax
               url:   '/generator', //archivo que recibe la peticion
               type:  'post', //método de envio
               dataType: "json",
               success:  function (response) { //una vez que el archivo recibe el request lo procesa y lo devuelve
                    console.log(response[0]);
                    $("#encryption-text").html(response[0]);
                    $("#invert-text").html(response[1]);
                    $("#groups-text").html(response[2]);
               }
       });
    e.preventDefault();
  });

  $("#groups").keyup(function(e) {
    $.ajax({
               data:  {
                 "text" : $("textarea[name='text']").val(),
                 "displacement" : $("input[name='displacement']").val(),
                 "groups" : $("input[name='groups']").val()
               }, //datos que se envian a traves de ajax
               url:   '/generator', //archivo que recibe la peticion
               type:  'post', //método de envio
               dataType: "json",
               success:  function (response) { //una vez que el archivo recibe el request lo procesa y lo devuelve
                    console.log(response[0]);
                    $("#encryption-text").html(response[0]);
                    $("#invert-text").html(response[1]);
                    $("#groups-text").html(response[2]);
               }
       });
    e.preventDefault();
  });
});
