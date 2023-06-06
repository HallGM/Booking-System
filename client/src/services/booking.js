import axios from "axios";
import bookingModel from "../models/booking";

const URL = "http://127.0.0.1:8000/booking";
const errorCatch = (error) => console.error(error);

function getAll() {
  return axios
    .get(URL)
    .then((response) => bookingModel.createBookings(response))
    .catch(errorCatch);
}

function get(id) {
  return axios
    .get(URL + "/" + id)
    .then((res) => bookingModel.createBooking(res))
    .catch(errorCatch);
}

function add(booking) {
  return axios
    .post(URL + "/", booking)
    .then((res) => res.data)
    .catch(errorCatch);
}

function destroy(id) {
  return axios
    .delete(URL + "/" + id)
    .then((res) => res.data)
    .catch(errorCatch);
}

function edit(id, data) {
  return axios
    .put(URL + "/" + id, data)
    .then((res) => res.data)
    .catch(errorCatch);
}

export default { getAll, add, get, destroy, edit };
