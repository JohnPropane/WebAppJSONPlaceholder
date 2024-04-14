function validateInputs() {
  var input1 = document.getElementById('floatingInput2');
  var input2 = document.getElementById('floatingInput3');

  if (parseFloat(input1.value) > parseFloat(input2.value)) {
        input2.value = input1.value;
}
  if(parseFloat(input2.value) < parseFloat(input1.value)){
        input1.value = input2.value;
}

}