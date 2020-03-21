// Original JavaScript code by Chirp Internet: www.chirp.com.au
// Please acknowledge use of this code by including this header.

  function checkDate(field)
  {
    console.log("A01");     
    var allowBlank = false;
    var minYear = 1902;
    var maxYear = (new Date()).getFullYear();

    var errorMsg = "";

    // regular expression to match required date format
    re = /^(\d{1,2})\/(\d{1,2})\/(\d{4})$/;
    console.log(field.value);

    if(field.value != '') {
        console.log("A02");     
    if(regs = field.value.match(re)) {
            console.log("A03");     
        if(regs[2] < 1 || regs[2] > 31) {
              errorMsg = "Invalid value for day: " + regs[1];
                console.log("A04");     

            } else if(regs[1] < 1 || regs[1] > 12) {
              errorMsg = "Invalid value for month: " + regs[2];
            } else if(regs[3] < minYear || regs[3] > maxYear) {
 console.log("A05");     
  
                errorMsg = "Invalid value for year: " + regs[3] + " - must be between " + minYear + " and " + maxYear;
            }
          } else {
            errorMsg = "Invalid date format: " + field.value;
          }
    } else if(!allowBlank) {
      errorMsg = "Empty date not allowed!";
    }

    if(errorMsg != "") {
      alert(errorMsg);
      field.focus();
      return false;
    }

    return true;
  }
