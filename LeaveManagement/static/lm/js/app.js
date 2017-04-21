function calculate_date(){
    var d = document.getElementById('startdate').value();
    var num_of_days = document.getElementById('num_of_days').value();
    console.write(d);
    console.write(num_of_days);
    d.setDate(d.getDate() + num_of_days);
    document.getElementById("end_date").innerHTML = d;
  }