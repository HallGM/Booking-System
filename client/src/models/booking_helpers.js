import moment from "moment";

function dateToString(date) {
  return moment(date).format("Do MMM YYYY");
}

function addMethods(booking) {
  booking.convertDatesToISO = function () {
    operationOnDates(this, function(date) {
      return moment(date).format("YYYY-MM-DD");
    }); 
  };
  booking.enquiry_date_string = function () {
    return dateToString(this.enquiry_date);
  };
  booking.event_date_string = function () {
    return dateToString(this.event_date);
  };
}

function formatter(raw) {
  raw.fields.id = raw.pk;
  return raw.fields;
}

function operationOnDates(booking, operation) {
  for (const key of ["event_date", "enquiry_date"]) {
      booking[key] = operation(booking[key]);
  }
}

function addDates(booking) {
  operationOnDates(booking, (date) => new Date(date));
}

export default { addMethods, formatter, addDates };
