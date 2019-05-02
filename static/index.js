var msg = document.getElementById('msg');
var send_button = document.getElementById('send');
var chat_box = document.getElementById('msgs');

// sleeping
const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}



send_button.addEventListener('click', function (e) {
  var to_send = msg.value;
  if (to_send == '') {
    return;
  }
  to_send = encodeURIComponent(to_send);
  // console.log(to_send);
  var xhtttp = new XMLHttpRequest();
  xhtttp.open('GET', 'http://localhost:5000/send_message/chat/' + to_send, true);
  xhtttp.send()
  msg.value = '';
});

var get_messages = function () {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var rt = this.responseText;
      console.log(chat_box.innerHTML);
      console.log(rt);
      console.log(rt == chat_box.innerHTML);
      if (chat_box.innerHTML != rt) {
        chat_box.innerHTML = rt;
        chat_box.scrollTo(50000000000, 50000000000);
      }
      sleep(500).then(() => {
        requestID = window.requestAnimationFrame(get_messages);
      })
    }
  }
  xhttp.open('GET', 'http://localhost:5000/get_messages/chat', true);
  xhttp.send();
}

get_messages()
