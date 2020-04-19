var raz = document.getElementsByName('raz');
for (var i = 0; i < raz.length; i++) {
  raz[i].onclick = function() {
    localStorage.setItem('IRadioRaz', this.value);
  }
}
if(localStorage.getItem('IRadioRaz')) {
  var IRadioRaz = localStorage.getItem('IRadioRaz');
  document.querySelector('input[name="raz"][value="' + IRadioRaz + '"]').setAttribute('checked','checked');
}
