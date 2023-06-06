export function newBlankBooking() {
  return {
    status: "",
    paid_deposit: false,
    paid_in_full: false,
    enquiry_method: "",
    enquiry_date: "",
    enquiry_name: "",
    enquiry_email: "",
    set_option: "",
    travel_cost: 0,
    quote: 0,
    event_type: "",
    event_date: "",
    venue: "",
    contact_full_names: "",
    contact_address: "",
    contact_telephone: "",
    song_request: "",
    setup_info: "",
    music_between_sets: "",
    wedding_theme: "",
    introduced_as: "",
    timings: "",
    any_other_info: "",
  };
}

export function defaultFixTheMusic(booking){
    booking.status = "enquired";
    booking.paid_deposit = false;
    booking.paid_in_full = false;
    booking.enquiry_method = "Fix The Music";
    booking.enquiry_email = "hello@fixthemusic.com";
    booking.contact_full_names = "Fix The Music";
    booking.contact_address = "N/A";
    booking.contact_telephone = "+44 20 7193 0615";
}