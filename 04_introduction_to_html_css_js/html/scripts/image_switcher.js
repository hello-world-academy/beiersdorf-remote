// Image switcher code

var myImage = document.querySelector('img');

myImage.onclick = function() {
  var mySrc = myImage.getAttribute('src');
  if(mySrc === 'https://hello-world.academy/wp-content/uploads/2019/09/Beiersdorf-New-Headquarters.png') {
    myImage.setAttribute ('src','https://hello-world.academy/wp-content/uploads/2019/09/BDF_Logo.png');
  } else {
    myImage.setAttribute ('src','https://hello-world.academy/wp-content/uploads/2019/09/Beiersdorf-New-Headquarters.png');
  }
}