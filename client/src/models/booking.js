import bookingHelpers from "./booking_helpers";

function createBookings(rawJson) {
  return rawJson.data.map((booking) => {
    return _createBooking(booking);
  });
}

function createBooking(rawJson) {
  return _createBooking(rawJson.data)
}

function _createBooking(rawJson) {
  const { addMethods, formatter, addDates } = bookingHelpers;
  const newBooking = formatter(rawJson);
  addDates(newBooking);
  addMethods(newBooking);
  return newBooking;
}

export default { createBooking, createBookings };